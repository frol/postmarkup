"""BBCode to (X)HTML rendering engine

Converts BBCode (http://en.wikipedia.org/wiki/BBCode) in to HTML and
XHTML snippets. Always outputs valid XHTML, even from badly nested BBCode.
"""

VERSION = "1.2.0"

classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Programming Language :: Python
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
License :: OSI Approved :: Python Software Foundation License
Operating System :: OS Independent
Topic :: Text Processing :: Markup
"""

from setuptools import setup
import sys

doclines = __doc__.split("\n")

extra = {}
if sys.version_info >= (3,):
    extra["use_2to3"] = True

setup( install_requires=['setuptools'],
       name='postmarkup',
       version = VERSION,
       author = 'Will McGugan',
       author_email = 'will@willmcgugan.com',
       license = "Python Software Foundation License",
       url = 'http://code.google.com/p/postmarkup/',
       download_url = 'http://code.google.com/p/postmarkup/downloads/list',
       platforms = ['any'],
       description = doclines[0],
       long_description = '\n'.join(doclines[2:]),       
       packages = ["postmarkup"],       
       classifiers = classifiers.splitlines(),       
       **extra
       )
