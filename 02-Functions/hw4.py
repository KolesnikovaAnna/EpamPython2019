# Напишите функцию modified_func, которая принимает функцию (обозначим ее func),
# а также произвольный набор позиционных (назовем их fixated_args) и именованных
# (назовем их fixated_kwargs) аргументов и возвращает новую функцию,
# которая обладает следующими свойствами:

# 1.При вызове без аргументов повторяет поведение функции func, вызванной
# с fixated_args и fixated_kwargs.
# 2.При вызове с позиционными и именованными аргументами дополняет ими
# fixed_args (приписывает в конец списка fixated_args), и fixated_kwargs
# (приписывает новые именованные аргументы и переопределяет значения старых)
# и далее повторяет поведение func с этим новым набором аргументов.
# 3.Имеет __name__ вида func_<имя функции func>
# 4.Имеет docstring вида:
# """
# """
# A func implementation of <имя функции func>
# with pre-applied arguments being:
# <перечисление имен и значений fixated_args и fixated_kwargs>
# source_code:
#    ...
# """
# """
# Для того, чтобы получить имена позиционных аргументов и исходный код, советуем использовать
# возможности модуля inspect.

# Попробуйте применить эту функцию на написанных функциях из дз1, дз2, дз3. К функциям min, max, any() ?

"""
A func implementation of <name_of_func>
with pre-applied arguments being:
<fixated_args>
<fixated_kwargs>
source_code: 
<source_code>
"""

import inspect

def some_func(*args, **kwargs):
    print(args,kwargs)

def modified_func(func, *fixated_args, **fixated_kwargs):
   def new_func(*args, **kwargs):
      nonlocal fixated_args
      nonlocal fixated_kwargs
      a = []
      for i in args:
         a.append(i)
      fixated_args += tuple(a,)
      fixated_kwargs.update(kwargs)
      func(*fixated_args, **fixated_kwargs)

      new_func.__name__ = 'func_' + func.__name__
      source_code = inspect.getsource(new_func)
      new_func.__doc__ = __doc__.replace('<name_of_func>', new_func.__name__)
      new_func.__doc__ = new_func.__doc__.replace('<fixated_args>', str(fixated_args))
      new_func.__doc__ = new_func.__doc__.replace('<fixated_kwargs>', str(fixated_kwargs))
      new_func.__doc__ = new_func.__doc__.replace('<source_code>', source_code)
   return new_func

mod_func = modified_func(some_func, 1, 2, kwargs1 = 'a', kwargs2 = 'b')
mod_func(3, 4, kwargs3 = 'c', kwargs4 = 'd')
print(mod_func.__doc__)