Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def remote_control_next():
...     yield "atn"
...     yield "btv"
... 
...     
>>> itr = remote_control()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    itr = remote_control()
NameError: name 'remote_control' is not defined. Did you mean: 'remote_control_next'?
>>> itr = remote_control_next()
>>> itr
<generator object remote_control_next at 0x0000026228CAA1F0>
>>> next(itr)
'atn'
>>> next(itr)
'btv'
>>> next(itr)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    next(itr)
StopIteration
>>> for c in remote_control_next():
...     print(c)
... 
...     
atn
btv
