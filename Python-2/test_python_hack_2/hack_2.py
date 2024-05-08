"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    vowels = "aeiou"
    return "".join([char for char in s if char not in vowels])


print(fn_hack_2("fooziman"))  
print(fn_hack_2("barziman"))  
print(fn_hack_2("qux"))       

