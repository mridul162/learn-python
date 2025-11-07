Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = ["hey", "bro", "you'r", "awesome"]
for i in a:
    print(i)

    
hey
bro
you'r
awesome
dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
itr = iter(a)
itr
<list_iterator object at 0x000001EEC7D7EC50>
next(itr)
'hey'
next(itr)
'bro'
next(itr)
"you'r"
next(itr)
'awesome'
next(itr)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    next(itr)
StopIteration
>>> dir(itr)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
>>> itr = reversed(a)
>>> next(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    next(a)
TypeError: 'list' object is not an iterator
>>> for i in a:
...     print(i)
... 
...     
hey
bro
you'r
awesome
>>> itr = iter(a)
>>> itr = reversed(a)
>>> next(iter)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    next(iter)
TypeError: 'builtin_function_or_method' object is not an iterator
>>> next(itr)
'awesome'
>>> next(itr)
"you'r"
>>> next(itr)
'bro'
>>> next(itr)
'hey'
>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
