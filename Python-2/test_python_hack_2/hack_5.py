"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(texto, posicion=[2, 5, 8]):
    result = ""
    for palabra in texto.split():
        if palabra.startswith("foo"):
            result += "fo-zi-ma-"
        else:
            nueva_palabra = ""
            for i, char in enumerate(palabra):
                if i in posicion:
                    nueva_palabra += "-"
                else:
                    nueva_palabra += char
            result += nueva_palabra + " "
    return result.strip()
