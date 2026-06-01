num_str = '2732231212132211112212422212212212252211118112911521121122112121261222'
print("Length:", len(num_str))
print("Count of 2:", num_str.count('2'))
print("Count of 3:", num_str.count('3'))
for d in ['1', '4', '5', '6', '7', '8', '9']:
    print(f"Count of {d}:", num_str.count(d))

num = int(num_str)
for i in range(2, 10):
    print(f"Divisible by {i}:", num % i == 0)