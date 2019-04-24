# -*- coding: utf-8 -*-

_NUM_SIGNATURE_BYTES = 262
def get_signature_bytes(path):
    with open(path, 'rb') as fp:
        return bytearray(fp.read(_NUM_SIGNATURE_BYTES))
def signature(array):
    length = len(array)
    index = _NUM_SIGNATURE_BYTES if length > _NUM_SIGNATURE_BYTES else length
    return array[:index]
def get_bytes(obj):
    try:
        obj = obj.read(_NUM_SIGNATURE_BYTES)
    except AttributeError:
        pass
    kind = type(obj)
    if kind is bytearray:
        return signature(obj)
    if kind is str:
        return get_signature_bytes(obj)
    if kind is bytes:
        return signature(obj)
    if kind is memoryview:
        return signature(obj).tolist()
    raise TypeError('Unsupported type as file input: %s' % kind)
