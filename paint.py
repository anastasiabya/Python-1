"""
Нарисовать рамочку шириной w символов и
высотой h символов
"""

def f1(w,h):
    if h>1 and w>1:
        print(w*"*")
        for i in range(h-2):
            print("*"+(w-2)*" "+"*")
        print(w * "*")
    else:
        print("Недопустимые значения")

print("Задание 1")
w=4
h=3
f1(w,h)

"""
Пускай символ, которым рисуется рамочка –
тоже входной параметр.
"""

def f2(w,h,s):
    if h>1 and w>1:
        print(w*s)
        for i in range(h-2):
            print(s+(w-2)*" "+s)
        print(w * s)
    else:
        print("Недопустимые значения")

print("Задание 2")
w=4
h=3
s="y"
f2(w,h,s)

"""
Нарисовать рамочку шириной w символов и
высотой h символов, и толщиной f символов.
(оформить в виде функции)
"""

def f3(w,h,f):
    for i in range(f):
        print(w*"*")
    for i in range(h-2*f):
        print(f*"*"+(w-2*f)*" "+f*"*")
    for i in range(f):
        print(w*"*")


print("Задание 3")
w=5
h=6
f=2
f3(w,h,f)