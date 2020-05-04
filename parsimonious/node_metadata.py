"""Node metadata specific to a node belonging to one text
"""
from inspect import isfunction
from sys import version_info, exc_info

from six import reraise, python_2_unicode_compatible, with_metaclass, \
    iteritems

from parsimonious.exceptions import VisitationError, UndefinedLabel


@python_2_unicode_compatible
class NodeMetadata(object):
    __slots__ = ['start', # The position in the text where that expr started matching
                 'end',   # The position after start where the expr first didn't
                          # match. [start:end] follow Python slice conventions.
                 'children']  # list of child parse tree nodes mapping to list of children

    def __init__(self, start, end, children=None):
        self.start = start
        self.end = end
        self.children = children or []
