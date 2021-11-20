
''' data = [{"name": "Max", "age": 6},
        {"name": "Ivan", "age": 13},
        {"name": "John", "age": 8}]

sorted_data = sorted(data, key="age")
print(sorted_data)
'''

'''dict1 = {1: 1, 2: 9, 3: 4}
sorted_dict = {}

sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = dict1[w]

print(sorted_dict) # {1: 1, 3: 4, 2: 9}
'''

l = [1,2,3,4,5,6,7,8]
es = filter(lambda x: x%2==0, l)
res = (list(es))
print(res)
print(res)


