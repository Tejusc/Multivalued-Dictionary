from collections import UserDict

START_POS = 'S'
END_POS = 'E'

'''This is a Multivalued Dictionary with the following methods
    Keys : to get the all the keys from the dict
    pop : to remove all items for a key
    popitem : to remove items that are present last in the dictionar
    getitem : to get all values for a particular key
    clear : to clear the dictionary
    copy : a copy fuction to help us copy all the items in the dictionary
    items: gives all items in the dictionary
    count: gives the count of values for a key
'''

class multivalued_dict(UserDict):

    from collections import defaultdict
    from collections.abc import Iterable


    __marker = object()

    @classmethod
    def fromkeys(cls, iterable, value=None):
        dict_var = dict.fromkeys(iterable, value)
        return cls(dict_var)

    def __init__(self, *args, **kwargs):

        len_of_args = len(args)
        if len_of_args > 1:
            raise TypeError('multivalued_dict expected at most 1 arguments, got {len_of_args}')
        else:
            if not hasattr(self, 'data'):
                self.data = self.defaultdict(list)
            if len_of_args == 1:
                initial_items = args[0]
                if isinstance(initial_items, dict):
                    for _key, _value in initial_items.items():
                        if isinstance(_value, (tuple, list)):
                            self.data[_key].extend(_value)
                        else:
                            self.data[_key].append(_value)
                else:
                    self.update(initial_items)
        if kwargs != dict():
            self.__init__(kwargs)

    def __repr__(self):

        return 'multivalued_dict({dict(self.data)})'

    def __iter__(self):
        return iter(self.data.items())

    def __len__(self):

        return self.data.__len__()

    def getitem(self, key):

        if key in self.data:
            return self.data[key]
        else:
            raise KeyError(key)

    def __eq__(self, other):

        return self.data.__eq__(other)

    def __contains__(self, key):

        return self.data.__contains__(key)

    def __delitem__(self, key):

        self.data.__delitem__(key)

    def __setitem__(self, key, item):

        self.data.__setitem__(key, [item])

    def __lenvalue__(self, key=__marker):

        if key is self.__marker:
            return sum(map(len, self.data.values()))
        else:
            return len(self.data[key])

    def __matchkv__(self, key, value):

        return value in self.data[key]

    def __delkv__(self, key, value, allkv=True, direction=START_POS):

        assert allkv in (True, False), '"allkv" can only be True or False'
        assert direction in (START_POS, END_POS), '"direction" can only be START_POS or END_POS'

        if allkv:
            while value in self.data[key]:
                self.data[key].remove(value)
        else:
            if direction == START_POS:
                self.data[key].remove(value)
            elif direction == END_POS:
                value_len = len(self.data[key])
                for i in range(value_len):
                    if self.data[key][-1 - i] == value:
                        self.data[key].__delitem__(-1 - i)
                        break

    def __reverse__(self):
        for _key in reversed(tuple(self.data.keys())):
            self.data[_key] = self.data.pop(_key)

    def count(self, key, value):

        return self.data[key].count(value)

    def add(self, key, value):

        if value in self.data[key]:
            return "Error : value already exists"
        else:
            self.data[key] = value
            return "Success"

    def keyexists(self, key):

        if key in self.data:
            return key," exists in the dictionary"
        else:
            return key," does not exists"

    def setdefault(self, key, default=None):

        return self.data.setdefault(key, [default])

    def pop(self, key, default=__marker):

        if default is self.__marker:
            return self.data.pop(key)
        else:
            return self.data.pop(key, [default])

    def popitem(self):

        return self.data.popitem()

    def removeall(self,key):
        return self.data[key].clear()

    def copy(self):

        return multivalued_dict(self.data)

    def items(self):

        return self.data.items()

    def keys(self):

        return self.data.keys()

    def values(self):

        return self.data.values()

    def clear(self):

        self.data.clear()
