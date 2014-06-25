import os 
import sys
import cherrypy
import ConfigParser
import urllib2
import json
import webtools
import requests


class SetlistServer(object):
    def __init__(self, config):
        self.production_mode = config.getboolean('settings', 'production')
        self.total_calls = 0


    @cherrypy.tools.caching(delay=3600 * 24)
    def query(self, q):
        cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
        cherrypy.response.headers['Content-Type']= 'application/json'

        if 'setlist.fm' in q:
            r = requests.get(q)
            print "calling setlist.fm", self.total_calls
            self.total_calls += 1
            return r.text.encode('utf8')
        else:
            return '{}'
    query.exposed = True

if __name__ == '__main__':
    urllib2.install_opener(urllib2.build_opener())
    conf_path = os.path.abspath('web.conf')
    print 'reading config from', conf_path
    cherrypy.config.update(conf_path)

    config = ConfigParser.ConfigParser()
    config.read(conf_path)
    production_mode = config.getboolean('settings', 'production')

    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Set up site-wide config first so we get a log if errors occur.

    if production_mode:
        print "Starting in production mode"
        cherrypy.config.update({'environment': 'production',
                                'log.error_file': 'simdemo.log',
                                'log.screen': True})
    else:
        print "Starting in development mode"
        cherrypy.config.update({'noenvironment': 'production',
                                'log.error_file': 'site.log',
                                'log.screen': True})

    conf = webtools.get_export_map_for_directory("static")
    cherrypy.quickstart(SetlistServer(config), '/SetlistServer', config=conf)

