# -*- coding: utf-8 -*-

from __future__ import absolute_import
from types import AUDIO as audio_matchers
from types import TYPES
from utils import get_bytes
def match(obj, matchers=TYPES):
    buf = get_bytes(obj)
    for matcher in matchers:
        if matcher.match(buf):
            return matcher
    return None

def audio(obj):
    return match(obj, audio_matchers)
