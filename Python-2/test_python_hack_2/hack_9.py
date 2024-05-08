"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(palabras, cambio="ook"):
    res = {key.capitalize(): valor.replace("k", "").capitalize() for key, valor in palabras.items() if cambio in valor}
    return res

datos = {"foo": "fookziman", "bar": "barziman"}
respuesta = fn_hack_9(datos)
print(respuesta)  
