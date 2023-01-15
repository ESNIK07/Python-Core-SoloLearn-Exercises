"""
Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
"""

def mayor_ext(lineas):
    tamaños = [len(i) for i in lineas]
    return lineas[tamaños.index(max(tamaños))]

txt = input()

lineas = txt.split(' ')
palabra = mayor_ext(lineas)
print(palabra)
