"""
Simplistic implementation to make it easier to create safe lucene
queries.
"""
import re

def _field(name, value):
    return '%s:%s' % (name, value)

def field(name, value):
    return _field(name, quoted(value))

def _range(name, start, end):
    return _field(name, '[%s TO %s]' % (start, end))

def _star_or_quoted(s):
    if s is None:
        return '*'
    return quoted(s)

def text_range(name, start, end):
    return _range(name, _star_or_quoted(start), _star_or_quoted(end))

def _star_or_isoformat(dt):
    if dt is None:
        return '*'
    return dt.isoformat() + 'Z'

def date_range(name, start, end):
    return _range(name, _star_or_isoformat(start), _star_or_isoformat(end))

def and_(*args):
    return '(%s)' % ' AND '.join(args)

def or_(*args):
    return '(%s)' % ' OR '.join(args)

_to_escape = ['+', '-', '&', '|', '!', '(', ')', '{', '}',
             '[', ']', '^', '"', '~', '*', '?', ':', '\\']

_escape_re = '|'.join([(re.escape(c)) for c in _to_escape])
_escape_re_compiled = re.compile('(%s)' % _escape_re)

def _escape(match):
    return '\\' + match.group()

def escape(s):
    return _escape_re_compiled.sub(_escape, s)

def quoted(value):
    return '"%s"' % escape(value)
