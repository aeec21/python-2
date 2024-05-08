"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

def fn_hack_6(s):
    result = []
    if not s:
        result = ["0"]
    else:
        result = [str(i + 1) if (i + 1) % 2 != 0 else "-" for i in range(len(s))]
    return result


print(fn_hack_6(["a", "b", "c", "d", "e"]))  
print(fn_hack_6([]))                        


