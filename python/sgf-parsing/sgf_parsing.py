import re
from collections import defaultdict

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if not input_string or input_string.islower():
        raise ValueError("invalid string")
    else:
        pattern = re.compile(r'([A-Z]+)(\[(\w+)\]){1,}')
        match_data = re.findall(pattern, input_string)
        if not match_data:
            raise ValueError("invalid string")
        else:
            d = defaultdict(list)
            for k, _, v in match_data:
                d[k].append(v)
            return SgfTree(properties=d)
