#!/usr/bin/python
"""
GPT generated function for changing values in a nested tuple
since the returned mms object have multiple layers of nested tuples, this is 
useful when you want to change a field to see how the byte representation 
changes
"""

d = ('confirmedResponsePdu', {'invokeID': 55, 'confirmedServiceResponse': ('read', {'listOfAccessResult': [('success', ('bit-string', (bytearray(b'\x80'), 2))), ('success', ('bit-string', (bytearray(b'\x00\x00'), 13)))]})})

print(d)

def set_in(obj: Any, path: Sequence[Any], value: Any) -> Any:
    """
    Return a new object like `obj` but with the element at `path` replaced by `value`.
    Path elements:
      - int => index into tuple/list
      - any other hashable => key into dict
    Works with nested tuples, lists, and dicts. Leaves other objects unchanged
    except when path is empty (then returns value).
    """
    if not path:
        return value

    head, *rest = path

    if isinstance(obj, tuple):
        if not isinstance(head, int):
            raise TypeError("tuple index must be int")
        if head < 0 or head >= len(obj):
            raise IndexError("tuple index out of range")
        items = list(obj)
        items[head] = set_in(items[head], rest, value)
        return tuple(items)

    if isinstance(obj, list):
        if not isinstance(head, int):
            raise TypeError("list index must be int")
        if head < 0 or head >= len(obj):
            raise IndexError("list index out of range")
        items = list(obj)
        items[head] = set_in(items[head], rest, value)
        return items

    if isinstance(obj, dict):
        if head not in obj:
            raise KeyError(f"key {head!r} not found in dict")
        newd = obj.copy()
        newd[head] = set_in(newd[head], rest, value)
        return newd

    # If we still have path elements but obj is a leaf, it's an error:
change_tuple(d, [1, 'confirmedServiceResponse', 1, 'listOfAccessResult', 1, 1], bytearray(b'@'))

path = [1, 'confirmedServiceResponse', 1, 'listOfAccessResult', 0, 1, 1, 0]

new_d = set_in(d, path, bytearray(b'@'))
print(new_d)
