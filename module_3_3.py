def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = ['cat', False, 123]
values_dict = {'a': 'fox', 'b': False, 'c': 456}
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(b=25, c=[1, 2, 3])

print_params(values_list)
print_params(*values_list)
print_params(values_dict)
print_params(**values_dict)
# print_params(*values_list,**values_dict)#print_params(*values_list,**values_dict)
# TypeError: print_params() got multiple values for argument 'a'
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
