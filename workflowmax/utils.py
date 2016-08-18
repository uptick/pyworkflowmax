import json
import re
from collections import defaultdict


def xml_to_dict(xml):
    nodes = re.findall('(<([^>]*)>(.*?)</\\2>)', xml, re.DOTALL)
    if len(nodes) == 0:
        return xml
    d = defaultdict(list)
    for node in nodes:
        d[node[1]].append(xml_to_dict(node[2]))

    # Yucky, but easiest way to convert nested default dict to nested dict.
    d = json.loads(json.dumps(d))

    return d
