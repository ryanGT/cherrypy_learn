import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!, 0.0.0.0"

if __name__ == '__main__':
    conf = {'server.socket_host': '0.0.0.0'} 
    cherrypy.config.update(conf)
    cherrypy.quickstart(HelloWorld())
