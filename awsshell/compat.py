import sys

PY3 = sys.version_info[0] == 3

if PY3:
    from html.parser import HTMLParser
    text_type = str
    from io import StringIO
else:
    from HTMLParser import HTMLParser
    text_type = unicode
    from cStringIO import StringIO