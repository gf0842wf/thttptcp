# -*- coding: utf-8 -*-

def named_any(name):
    """ 参照from twisted.python.reflect import namedAny
    @param name: The name of the object to return.
    @return: the Python object identified by 'name'.
    """
    names = name.split(".")
    if " " in names:
        raise ValueError("name has space character!")
    
    for i in xrange(len(names)):
        try:
            return __import__(".".join(names[i:]))
        except:
            continue
        
        raise ValueError("can't import!")