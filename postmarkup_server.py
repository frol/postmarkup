import cherrypy
import postmarkup
import os

class Root(object):

    def index(self):
        return open("index.htm").read()
    index.exposed = True

    def getbbcode(self, bbcode=""):
        html = postmarkup.render_bbcode(bbcode, clean=True)
        return html
    getbbcode.exposed = True


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Set up site-wide config first so we get a log if errors occur.
    cherrypy.config.update({'environment': 'production',
                            'log.error_file': 'site.log',
                            'log.screen': True})

    conf = {'/': {'tools.staticdir.root':current_dir},
            '/static': {'tools.staticdir.on': True,
                     'tools.staticdir.dir': os.path.join(current_dir, 'static')},}


    cherrypy.quickstart(Root(), '/', config=conf)
