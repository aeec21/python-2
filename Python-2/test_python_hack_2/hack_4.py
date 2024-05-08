"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    palabra = s.split()
    result = ""
    for palabra in palabra:
        if len(palabra) > 0:
            if palabra[0] == 'f':
                palabra = palabra[1:]
            if palabra[0] == 'b':
                palabra = palabra[1:]    
            if palabra[-1] == 'n':
                palabra = palabra[:-1]
        result += palabra + " "
    return result.strip()

print(fn_hack_4("fooziman"))  
print(fn_hack_4("barziman"))  
print(fn_hack_4("qux"))       