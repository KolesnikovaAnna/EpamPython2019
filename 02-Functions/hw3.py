'''Напишите реализацию функции make_it_count, которая принимает в качестве
аргументов некую функцию (обозначим ее func) и имя глобальной переменной
(обозначим её counter_name), возвращая новую функцию, которая ведет себя
в точности как функция func, за тем исключением, что всякий раз при вызове
инкрементирует значение глобальной переменной с именем counter_name.
'''

counter_name = 1
global_variable = 5

def func():
    return "Bla bla bla"

def make_it_count(func, counter_name):
    def new_func():
        func()
        nonlocal counter_name
        counter_name += global_variable
        print(counter_name)
        return counter_name
    return new_func

new_func = make_it_count(func,counter_name)
new_func()