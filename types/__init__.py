# -*- coding: utf-8 -*-

from __future__ import absolute_import

from . import audio
from .base import Type  # noqa
AUDIO = (
    audio.Midi(),
    audio.Mp3(),
    audio.M4a(),
    audio.Ogg(),
    audio.Flac(),
    audio.Wav(),
    audio.Amr(),
)

TYPES = list(AUDIO)
