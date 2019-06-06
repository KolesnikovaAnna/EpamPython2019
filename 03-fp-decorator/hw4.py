'''Переписать функцию make_cache, которая сохраняет
результаты предыдущих вызовов оборачиваемой функции,
таким образом, чтобы она сохраняла результаты в своем
хранилищe на определенное время, которое передается
параметром (аргументом) в декоратор.


Плюс придумать некоторый полезный юзкейс и заимплементировать функцию slow_function
'''

def make_cache(a_function_to_decorate):
    def some_function():
        cache = []
        for i in range(0,5):
            cache.append(a_function_to_decorate(i))
        print (cache)
    return some_function

@make_cache
def slow_function(num = 0):
    '''Function that return list'''
    print ("Make a list in slow_function", num)
    array = [x for x in range(num)]
    return array
 
slow_function()