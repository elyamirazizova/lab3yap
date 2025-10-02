#задание 1
sqares = [x**2 for x in range(1,11)]
print("Задание 1",sqares)

#задание 2
even_numbers={x for x in range(1,20) if x%2==0}
print("Задание 2",even_numbers)

#задание 3
words = ["python", "Java", "c++", "Rust", "go"]
new_list = [word.upper() for word in words if len(word)>3]
print("Задание 3",new_list)

#задание 4
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
    
print("Задание 4")
    
countdown = Countdown(5)
for number in countdown:
    print(number)

#задание 5
def fibonacci(n):
    a,b = 0,1
    count = 0
    while count < n:
        yield a
        a,b = b, a+b
        count+=1

print("задание 5")

for num in fibonacci(5):
    print(num)  