'''Напишите реализацию функции atom, которая инкапсулирует некую переменную,
предоставляя интерфейс для получения и изменения ее значения,
таким образом, что это значение нельзя было бы получить или изменить
иными способами.
Пусть функция atom принимает один аргумент, инициализирующий хранимое значение
(значение по умолчанию, в случае вызова atom без аргумента - None),
а возвращает 3 функции - get_value, set_value, process_value, delete_value,такие, что:

get_value - позволяет получить значение хранимой переменной;
set_value - позволяет установить новое значение хранимой переменной,
	возвращает его;
process_value - принимает в качестве аргументов сколько угодно функций
	и последовательно (в порядке перечисления аргументов) применяет эти функции
	к хранимой переменной, обновляя ее значение (перезаписывая получившийся
	результат) и возвращая получишееся итоговое значение.
delete_value - удаляет значение'''


def atom(arg = None):
    def get_value():
        return arg

    def set_value(new_arg):
        nonlocal arg 
        arg = new_arg
        return arg

    def process_value(*args):
        nonlocal arg 
        for function in args:
            arg = function(arg)    
        return arg

    def delete_value():
        nonlocal arg
        del(arg)
    
    return get_value, set_value, process_value, delete_value

def f1(arg):
	return arg * 2

def f2(arg):
	return arg * 5

a, b, c, d = atom(5)
print(a(), b(2), c(f1, f2), d()) 