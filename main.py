#задание 1
sqares = [x**2 for x in range(1,11)]
print(sqares)

#задание 2
even_numbers={x for x in range(1,20) if x%2==0}
print(even_numbers)

#задание 3
words = ["python", "Java", "c++", "Rust", "go"]
new_list = [word.upper() for word in words if len(word)>3]
print(new_list)