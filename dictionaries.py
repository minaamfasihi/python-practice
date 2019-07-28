my_dict = {'k1': 123, 'k2': 3.4, 'k3': 'string'}
print(my_dict['k3'])

print(my_dict['k3'][::-1]) # output: gnirts

print(my_dict['k3'].upper())

my_dict['k1'] += 10
print(my_dict['k1'])

my_dict['animal'] = 'Dog'
print(my_dict['animal'])

d = {'k1': {'nestkey': {'subnestkey': 'value'}}}
print(d['k1']['nestkey']) # {'subnestkey': 'value'}
print(d['k1']['nestkey']['subnestkey']) # value
print(d.keys()) # output: dict_keys(['k1'])
print(d.values()) # output: dict_values([{'nestkey': {'subnestkey': 'value'}}])

print(my_dict.items())