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
    
countdown = Countdown(5)
for number in countdown:
    print("Задание 4",number)