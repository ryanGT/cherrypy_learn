import random
import string

import cherrypy

import time, os, glob
foldername = time.strftime('%m_%d_%y')

def image_name_to_time_stamp(relpath):
    """Convert an image file name to an easier to read time stamp
    string"""
    fmt = 'image_%I_%M_%S_%p.jpg'
    folder, fn = os.path.split(relpath)
    time_struct = time.strptime(fn, fmt)
    time_stamp = time.strftime('%I:%M:%S %p', time_struct)
    return time_stamp


class StringGenerator(object):
    def find_img_folder(self):
        date_folder_rel = os.path.join('img',foldername)

        if not os.path.exists(date_folder_rel):
            print('problem with relpath for date folder: ' + date_folder_rel)
        else:
            return date_folder_rel

    def find_images(self, date_folder):
        pat = os.path.join(date_folder, 'image_*.jpg')
        jpeg_list = glob.glob(pat)
        jpeg_list.sort()
        return jpeg_list
    
        #        img_part = """<img src="/img/webtest.png" width=600px>


    @cherrypy.expose
    def show_image(self, index=-1):
        header = """ <html>
        <head>
        <title>CherryPy Baby Monitor</title>
        </head>
        <html>
        <body>"""
        date_folder = self.find_img_folder()
        print('date_folder: ' + date_folder)
        jpeg_list = self.find_images(date_folder)
        jpeg_relpath = jpeg_list[index]
        top_part = "filename: %s" % jpeg_relpath
        time_stamp = image_name_to_time_stamp(jpeg_relpath)
        top_part += " <br> time stamp: %s" % time_stamp
        jpeg_path = '/' + jpeg_relpath
        print('jpeg_path: ' + jpeg_path)
        img_part = '<img src="%s" width=600px>' % jpeg_path
        footer = """</body>
        </html>"""
        out = " <br> ".join([header, top_part, img_part])
        return out

        
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
    ## img_key = '/' + date_folder
    ## img_rel = '.' + img_key
    ## removed from conf:
    ## img_key: {
    ## "tools.staticdir.on": True,
    ## "tools.staticdir.dir": img_rel,
    ## }, \

    conf = {'/': {
                'tools.sessions.on': True, \
                'tools.staticdir.root': os.path.abspath(os.getcwd()), \
                'tools.staticdir.debug': True, \
                'log.screen': True
                }, \
            '/static': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': './public',
                }, \
            '/img': {
                "tools.staticdir.on": True,
                "tools.staticdir.dir": './img',
                }, \
            '/data': {
                "tools.staticdir.on": True,
                "tools.staticdir.dir": './data',
                }
            }
    cherrypy.config.update(conf)
    cherrypy.config.update({'server.socket_host':'0.0.0.0'})
    cherrypy.quickstart(StringGenerator(), '/', conf)

    
