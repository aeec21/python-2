"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

def fn_hack_10(s):
    result = []
    for antes in s:
        ahora = {}
        for k, v in antes.items():
            if isinstance(v, str):
                nueva_v = str(ord(v) - ord('a') + 1)
            else:
                nueva_v = str(ord(list(v)[0]) - ord('a') + 1)
            ahora[str(ord(k) - ord('a') + 1)] = nueva_v
        result.append(ahora)
    return result

s = [{"a": "b"}, {"c": "d"}, {"e": "f"}]
output = fn_hack_10(s)
print(output)  


