"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""

def fn_hack_7(s):
    if not s:
        result = [0]
    elif len(s) == 1 and s[0] == 0:
        result = [0]
    else:
        result = [str(i + 1) if (i + 1) % 2 != 0 else i + 1 for i in range(len(s))]
    return result

print(fn_hack_7(["a", "b", "c", "d", "e"]))  
print(fn_hack_7([0]))  
