"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

def fn_hack_8(s):
    result = [f"{val}-{len(s) - idx}" if len(s) % 2 != 0 else str(len(s) - idx) for idx, val in enumerate(s[::-1])]
    return result  


print(fn_hack_8(["a", "b", "c", "d", "e"]))  
print(fn_hack_8(["a", "b", "c"]))             
print(fn_hack_8(["a", "b", "c", "d"]))        
print(fn_hack_8(["a", "b"]))          
