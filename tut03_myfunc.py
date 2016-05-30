import random
import string

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


    @cherrypy.expose
    def myfunc(self, a=1, b=2):
        a = float(a)
        b = float(b)
        c = a + b
        line1 = 'a = %s' % a
        line2 = 'b = %s' % b
        line3 = 'c = %s' % c
        mylist = [line1, line2, line3]
        outstr = ' <br> '.join(mylist)
        return outstr


if __name__ == '__main__':
    conf = {'server.socket_host': '0.0.0.0'} 
    cherrypy.config.update(conf)
    cherrypy.quickstart(StringGenerator())

    
