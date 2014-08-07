import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options


counter = 0

captions = range(4)

define("port", default=8080, help="run on the given port", type=int)

class MyStaticFileHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        # Disable cache
        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')


class Application(tornado.web.Application):
    def __init__(self):

        settings = dict(
        debug=True,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        )

        handlers = [
            (r"/", IndexHandler),
            (r"/upload", UploadHandler),
            (r"/error", ErrorHandler),
            (r'/uploads/(.*)', MyStaticFileHandler, {'path': './uploads'}),
            (r'/static/(.*)', MyStaticFileHandler, {'path': './static'}),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)

import os

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        global captions
        print captions

        print 'Yolo!!!'
        print os.getcwd()
        self.render("test.html", main_title='Volepsou', captions=captions)


from PIL import Image, ImageOps
import StringIO
import os
import datetime

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        print 'bad picture'
        self.write('problem')

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        # get data from post
        try:
            caption = self.request.arguments['text1'][0]
        except KeyError:
            pass
        file1 = self.request.files['file1'][0]
        original_fname = file1['filename']
        extension = os.path.splitext(original_fname)[1]

        # clean data or exit
        im = Image.open(StringIO.StringIO(file1['body']))
        (lenght,height) = im.size

        # if lenght > height: # redirect to error message
        #     self.redirect('/error')
        #     return
        if caption == '':
            caption = '...'

        global captions
        captions.pop()
        captions.insert(0, str(datetime.datetime.now()) + ' - ' + caption)

        os.rename('uploads/3.jpg', 'uploads/4.jpg')
        os.rename('uploads/2.jpg', 'uploads/3.jpg')
        os.rename('uploads/1.jpg', 'uploads/2.jpg')

        size = 360, 540
        im.thumbnail(size, Image.ANTIALIAS)

        # size = 340, 520
        # im.thumbnail(size, Image.ANTIALIAS)
        # im_with_border = ImageOps.expand(im,border=20,fill='black')

        im.save('uploads/1.jpg')

        # im.crop((0, 0, 200, 200)).save('uploads/new.jpg')
        # else: # portrait
        # self.render("test.html", main_title='Volepsou')


        self.redirect('/') # if error redirect to error with reason
        # and possibility to get back to root


        # fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        # final_filename= fname+extension

        # save the file
        # final_filename = "onlyfile"+extension
        # output_file = open("uploads/" + final_filename, 'w')
        # output_file.write(file1['body'])
        # self.finish("file" + final_filename + " is uploaded")

        # render the image
        # self.render("photomaton.html")

# def crop_image():



def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == "__main__":
    main()
