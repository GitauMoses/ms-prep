# d = {"a": 4, "b": 2,"c": 3}
# list = ["a","b"]
# for k, v in d.items():
#     if k not in list:
#         print(k,v)

# names  = ["Moses", "John"]
# scores = [95, 87, 80]

# for name, score in zip(names, scores):
#     print(name, score) 

# for i in range(5):
#     for j in range(5):
#         if i == j == 2:
#             break
#     print(i, j)

# x = 10

# def add(a, b=5):
#     result = a + b + x
#     return result

# print(add.__code__)      # the compiled bytecode object
# print(add.__globals__)   # the module's global namespace  
# print(add.__defaults__)  # (5,)  ← the default for b
# print(add.__closure__)   # None  ← no closure yet


# x = [1,2,3,4]

# y = tuple(x)
# print (type(y))

# numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# # sort by value — pass a lambda as the key function:
# sorted_nums = sorted(numbers)
# print(sorted_nums) 

# def foo():
#     pass

# print(foo())

# def add(*args):
#     print(type(args))
#     return sum(args)

# print(add(1, 2, 3))
# print(add(1, 2, 3, 4, 5))

# def add5(a, b=5):
#     return a + b

# print(add5(1))
# print(add5(3))
# print(add5(4))

# numbers = [5, 2, 8, 1, 9, 3]

# a = sorted(numbers, key=lambda x: x)
# b = sorted(numbers, key=lambda x: -x)

# print(a)
# print(b)

def foo(lst=[]):
    lst.append(1)
    return lst

a = foo()
b = foo()
c = foo([])

print(a)
print(b)
print(c)
print(a is b)
print(a is c)