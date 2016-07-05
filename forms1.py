import random
import string

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
            <head></head>
            <body>
                <form method="get" action="respond">
                    <input type="text" value="test" name="text_input" />
                    <button type="submit">Submit</button>
                </form>
            </body>
        </html>"""

    @cherrypy.expose
    def respond(self, text_input='hello'):
        msg = 'You sent me this text_input: %s' % text_input
        return msg


if __name__ == '__main__':
    conf = {'server.socket_host': '0.0.0.0'} 
    cherrypy.config.update(conf)
    cherrypy.quickstart(StringGenerator(),config={'/':conf})
