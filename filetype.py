# -*- coding: utf-8 -*-

from __future__ import absolute_import
from match import match
from types import TYPES, Type
types = TYPES
def guess(obj):
    return match(obj) if obj else None
def guess_mime(obj):
    kind = guess(obj)
    return kind.mime if kind else kind