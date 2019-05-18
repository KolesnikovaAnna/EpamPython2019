"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""

def is_permutation(a: str, b: str) -> bool:
    # Нужно проверить, являются ли строчки 'a' и 'b' перестановками
	a = ''.join(sorted(a))
	b = ''.join(sorted(b))
	print(a, b)
	if a == b:
		print("T")
		return True
	else:
		print("F")
		return False

assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')