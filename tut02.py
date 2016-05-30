import random
import string
import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!, 0.0.0.0"

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))


if __name__ == '__main__':
    conf = {'server.socket_host': '0.0.0.0'} 
    cherrypy.config.update(conf)
    cherrypy.quickstart(HelloWorld())
