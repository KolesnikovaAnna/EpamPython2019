"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на место отведенное под него
В конечном варанте кода будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools

def my_decorator(func):
    def atributs(*args, **kwargs):
        # atributs.__doc__ = func.__doc__
        # atributs.__name__ = func.__name__
        # atributs.__original_func = func
        # print(atributs.__name__, atributs.__doc__)

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(result)
            wrapper.__doc__ = func.__doc__
            wrapper.__name__ = func.__name__
            wrapper.__original_func = func
            #   print(wrapper.__name__, wrapper.__doc__)
            return wrapper
        return wrapper

        #return atributs
    return atributs

def print_result(func):
    @my_decorator(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)

if __name__ == '__main__':
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    print(custom_sum.__original_func) 
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)