def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(5)
print_params(7, 'новая строка')
print_params(10, 55, 'теперь строка')
# проверка вызовов
print_params(b = 25)
print_params(c = [1, 2, 3])
# распаковка параметров
values_list = [5, 'list string', False]
values_dict = {'a':15, 'b':'dict string', 'c': True}
print_params(*values_list)
print_params(**values_dict)
#Распаковка + отдельные параметры
values_list_2 =[True, 'list2 string']
print_params(*values_list_2, 42)  # Работает!
