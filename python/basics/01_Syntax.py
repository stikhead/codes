# Python uses indentation (whitespace) to define blocks instead of {}
# Like javascript, we dont declare types
# Python integers have arbitrary precision i.e they never overflow, no need of long long unlike c++
# Logical operators uses words: and, or, not
# Division (/) always returns float type ( use // to return integer type)

a = 0
b = -1
print(a/b) # 1.2
print(a//b) # 1

print(a)
print(b)
print('swapping...')
a, b = b, a

print(a)
print(b)