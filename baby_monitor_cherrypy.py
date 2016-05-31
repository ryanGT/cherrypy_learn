import random
import string

import cherrypy

import time, os, glob

foldername = time.strftime('%m_%d_%y')# specify folder name based on
                                      # date when script is run, mm_dd_yy
                                      

def image_name_to_time_stamp(relpath):
    """Convert an image file name to an easier to read time stamp
    string; filenames use the format image_HH_MM_SS_PM.jpg"""
    fmt = 'image_%I_%M_%S_%p.jpg'
    folder, fn = os.path.split(relpath)# break image path into folder
                                       # and filename
    time_struct = time.strptime(fn, fmt)# convert string to time variable
    # convert time variable into a string with a different format
    # (HH:MM:SS PM):
    time_stamp = time.strftime('%I:%M:%S %p', time_struct)
    return time_stamp


class StringGenerator(object):
    def find_img_folder(self):
        """Find folder for current date in the img directory.  The
        return string should be img/mm_dd_yy, for example img/05_31_16
        for May 31, 2016"""
        date_folder_rel = os.path.join('img',foldername)# foldername
                                                        # is generated
                                                        # above

        # throw an error if the date folder doesn't exist:
        assert os.path.exists(date_folder_rel), "folder not found: " + \
                   date_folder_rel

        return date_folder_rel


    def find_images(self, date_folder):
        """Find all image matching the pattern image_*.jpg in the
        date_folder"""
        pat = os.path.join(date_folder, 'image_*.jpg')
        jpeg_list = glob.glob(pat)
        jpeg_list.sort()
        return jpeg_list
    

    @cherrypy.expose
    def show_image(self, img_index=-1):
        """Serve a webpage that displays date folder, filename, and
        time stamp along with the latest image (or an older image if
        img_index is not -1)"""
        img_index = int(img_index)# if passed in using query string, this
                          # would be a string; make sure it is an
                          # integer
                          
        # html header string:
        header = """ <html>
        <head>
        <title>CherryPy Baby Monitor</title>
        </head>
        <html>
        <body>"""
        date_folder = self.find_img_folder()# get date folder relative path
        jpeg_list = self.find_images(date_folder)# find all images in
                                                 # date folder
        jpeg_relpath = jpeg_list[img_index]# get specific image specified
                                           # by img_index; -1 is the last one
                                           # (most recent)

        # build the text part of the webpage to be displayed above the
        # picture:
        top_part = "date folder: %s" % date_folder
        # note that html uses <br> for break or linefeed or newline:
        top_part += " <br>\n filename: %s" % jpeg_relpath
        # get easy to read time stamp from file name
        time_stamp = image_name_to_time_stamp(jpeg_relpath)
        top_part += " <br>\n time stamp: %s" % time_stamp
        jpeg_path = '/' + jpeg_relpath# cherrpy requires a leading /
                                      # on relative paths
        # html code to display the image:
        img_part = '<img src="%s" width=600px>' % jpeg_path
        # closing html code:
        footer = """</body>\n</html>"""
        # join strings together with <br> in between parts:
        out = " <br>\n".join([header, top_part, img_part, footer])
        return out

        
    @cherrypy.expose
    def index(self):
        #return "Hello world!"
        raise cherrypy.HTTPRedirect("/show_image")

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    conf = {'/': {
                'tools.sessions.on': True, \
                'tools.staticdir.root': os.path.abspath(os.getcwd()), \
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

    
