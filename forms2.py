import random
import string

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
            <head>
            <link href="/static/css/style.css" rel="stylesheet">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <body>
                <form method="get" action="respond">
                    <input type="text" value="test" name="text_input" />
                    <button type="submit" style="font-size:40px">Submit</button>
                </form>
                <form method="get" action="myfunc2">
                    <button type="submit" style="font-size:40px;min-width: 200px; width:300px;">
                        button2</button>
                </form>
                <form method="get" action="myfunc3">
                    <button type="submit" style="font-size:40px">button3</button>
                </form>
            </body>
        </html>"""


    @cherrypy.expose
    def respond(self, text_input='hello'):
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
