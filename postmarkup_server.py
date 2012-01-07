"""This is a WSGI server that runs a very simple application to test Postmarkup

You can find it on http://postmarkup.willmcgugan.com

"""

from postmarkup import render_bbcode

from os.path import basename, dirname, join
try:
    from fs.osfs import OSFS
except ImportError:
    print("Get PyFilesystem from http://code.google.com/p/pyfilesystem/")
    raise
import mimetypes

def application(environ, start_response):
    fs = OSFS(join(dirname(__file__), "static"))
    path = environ["PATH_INFO"]      
    if path in ("", "/"):        
        path = "index.html"
    if path == "/getbbcode":
        bbcode = unicode(environ["wsgi.input"].read(), 'utf-8')
        html = render_bbcode(bbcode, clean=True, paragraphs=True, render_unknown_tags=True)
        start_response("200 OK", [("Content-type", "text/html; charset=utf-8")])
        return [html.encode("utf-8")]
    mime_type, _encoding = mimetypes.guess_type(basename(path))
    if not fs.isfile(path):
        start_response("404 NOT FOUND", [])
        return ["Nobody here but us chickens: %s" % path]
    start_response("200 OK", [("Content-type", mime_type)])    
    return [fs.getcontents(path)]
    
        
if __name__ == "__main__":
    from paste import httpserver
    httpserver.serve(application)
