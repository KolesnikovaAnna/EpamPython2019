'''Некоторые встроенные функции в Python имеют нестандартное поведение, когда
дело касается аргументов и их значений по умолчанию.
Например, range, принимает от 1 до 3 аргументов, которые обычно называются
start, stop и step и при использовании всех трех, должны указываться
именно в таком порядке. При этом только у аргументов start и step есть значения
по умолчанию (ноль и единица), а у stop его нет, но ведь аргументы без значения
по умолчанию, то есть позиционные аргументы, должны указываться до именнованных,
а stop указывается после start. Более того, при передаче функции только одного
аргумента он интерпретируется как stop, а не start.
Подумайте, каким образом, можно было бы добиться такого же поведения для
какой-нибудь нашей пользовательской функции.
Напишите функцию letters_range, которая ведет себя похожим на range образом,
однако в качестве start и stop принимает не числа, а буквы латинского алфавита
(в качестве step принимает целое число) и возвращает не перечисление чисел, а
список букв, начиная с указанной в качестве start (либо начиная с 'a',
если start не указан), до указанной в качестве stop с шагом step (по умолчанию
равным 1). Добавить возможность принимать словарь с заменами букв для подобия траслитерации.
Т.е. замена символов из оригинального алфавита другими, возможно несколькими символами.
'''
def is_int(n):
    return not(n%1)
#letters = ['abcdefghijklmnopqrstuvwxyz']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def letters_range(*args, **kwargs):
    #start = 0
    array = []
    if (len(args)>3 or len(args)==0):
        print("Error")
        return
    if (len(args)==3):
        if args[0] in letters and args[1] in letters:
            start = args[0]
            stop = args[1]
        else:
            print("Error")
            return
        if args[2] > 0 and is_int(args[2]):
            step = args[2]
        elif args[2] < 0:
            step = -1 * args[2]
            index_start, index_stop = letters.index(start), letters.index(stop)
            while index_start > index_stop:
                array.append(letters[index_start])
                index_start -= step
            return array
        else:
            print("Error")
            return
        index_start, index_stop = letters.index(start), letters.index(stop)
    if (len(args)==2):
        step = 1
        index_start, index_stop = letters.index(args[0]), letters.index(args[1])
    if (len(args)==1):
        index_start, index_stop, step = 0, letters.index(args[0]), 1
    
    #index_start, index_stop = letters.index(start), letters.index(stop)
    while index_start < index_stop:
        array.append(letters[index_start])
        index_start += step

    if len(kwargs) > 0:
        for i in kwargs:
            ind = array.index(i)
            array[ind] = kwargs[i]
    return array

'''
Пример:
>>>letters_range('b', 'w', 2)
['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v']
'''
print(letters_range('b', 'w', 2))

'''
>>>letters_range('g')
['a', 'b', 'c', 'd', 'e', 'f']
'''
print(letters_range('g'))

'''
>>>letters_range('g', 'p')
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
'''
print(letters_range('g', 'p'))

'''
>>>letters_range('g', 'p', **{'l': 7, 'o': 0})
['g', 'h', 'i', 'j', 'k', '7', 'm', 'n', '0']
'''
print(letters_range('g', 'p', **{'l': 7, 'o': 0}))

'''
>>>letters_range('p', 'g', -2)
['p', 'n', 'l', 'j', 'h']
'''
print(letters_range('p', 'g', -2))

'''
>>>letters_range('a')
[]
'''
print(letters_range('a'))