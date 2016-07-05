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
                <form method="get" action="myfunc2">
                    <button type="submit">button2</button>
                </form>
                <form method="get" action="myfunc3">
                    <button type="submit">button3</button>
                </form>
            </body>
        </html>"""


    @cherrypy.expose
    def generate(self, text_input='hello'):
        msg = 'You sent me this text_input: %s' % text_input
        return msg


    @cherrypy.expose
    def myfunc2(self):
        msg = 'You pressed button 2'
        return msg


    @cherrypy.expose
    def myfunc3(self):
        msg = 'You pressed button 3'
        return msg

    
if __name__ == '__main__':
    conf = {'server.socket_host': '0.0.0.0'} 
    cherrypy.config.update(conf)
    cherrypy.quickstart(StringGenerator(),config={'/':conf})
