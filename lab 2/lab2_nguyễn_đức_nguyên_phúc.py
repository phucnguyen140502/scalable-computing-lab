# -*- coding: utf-8 -*-
"""Lab2 Nguyễn Đức Nguyên Phúc.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p4wiH6t_djCwUlO0j6KKeXoa8TXdtMtK

1) Create an iterator that takes in a list and when iterated over, it returns the information in a reverse order.

Hint: When accepting arguments into an iterator, you need to use the init method, as well as iter and next.

The call below should result in `5, 4, 3, 2, 1`.
"""

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)  # Start at the end of the list

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:  # StopIteration when all elements are iterated
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


# Example usage
my_list = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(my_list)

for value in reverse_iter:
    print(value)

"""2) Create a generator that acts like the range function, except it yields a squared number every time.

The result of the call below should be `0, 1, 4, 16`.
"""

def squared_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current ** 2  # Yield the square of the current number
        current += step

# Example usage
for value in squared_range(0, 5):
    print(value)

"""3) Develop a function to compute the finonacci series based on `generator`."""

def fibonacci_series(n):
    # Khởi tạo danh sách để lưu dãy Fibonacci
    fib_sequence = []

    # Nếu n = 0, trả về danh sách rỗng
    if n == 0:
        return fib_sequence

    # Nếu n >= 1, thêm số đầu tiên của dãy Fibonacci
    fib_sequence.append(0)

    # Nếu n >= 2, thêm số thứ hai của dãy Fibonacci
    if n > 1:
        fib_sequence.append(1)

    # Tính các số tiếp theo từ số thứ ba trở đi
    while len(fib_sequence) < n:
        # Số Fibonacci tiếp theo là tổng của hai số trước đó
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    # Trả về danh sách dãy Fibonacci
    return fib_sequence

# Sử dụng hàm
n = 10  # Số lượng số Fibonacci muốn tính
result = fibonacci_series(n)
print(result)

"""4) Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n."""

class DivisibleBySeven:
    def __init__(self, n):
        """
        Initialize the class with an upper limit `n`.
        """
        self.n = n

    def generate_numbers(self):
        """
        Generator to yield numbers divisible by 7 from 0 to `n`.
        """
        for i in range(self.n + 1):  # Iterate from 0 to n (inclusive)
            if i % 7 == 0:          # Check if the number is divisible by 7
                yield i             # Yield the number if divisible

# Using the class
n = 50  # Define the upper limit
divisible_gen = DivisibleBySeven(n)  # Create an instance of the class

print(f"Numbers divisible by 7 between 0 and {n}:")
for number in divisible_gen.generate_numbers():
    print(number)

"""5) Define a class named `American` and its subclass `NewYorker`.

Hints:

Use class `Subclass(ParentClass)` to define a subclass.

"""

class American:
    """
    A class to represent an American.
    """
    def __init__(self):
        self.nationality = "American"

    def speak(self):
        return "I am an American."

class NewYorker(American):
    """
    A subclass of American to represent a New Yorker.
    """
    def __init__(self):
        super().__init__()  # Call the initializer of the parent class
        self.city = "New York"

    def speak(self):
        return "I am a New Yorker!"

# Example usage
american = American()
new_yorker = NewYorker()

print(american.speak())  # Output: I am an American.
print(new_yorker.speak())  # Output: I am a New Yorker!

"""6) Define a class named `Circle` which can be constructed by a radius. The `Circle` class has a method which can compute the area."""

import math

class Circle:
    """
    A class to represent a circle with a given radius.
    """
    def __init__(self, radius):
        """
        Initialize the Circle with a radius.
        """
        self.radius = radius

    def compute_area(self):
        """
        Compute and return the area of the circle.
        Formula: area = π * radius^2
        """
        return math.pi * (self.radius ** 2)

# Example usage
circle = Circle(5)  # Create a Circle with radius 5
print(f"The area of the circle with radius {circle.radius} is: {circle.compute_area():.2f}")

"""7) Define a class named `Rectangle` which can be constructed by a `length` and `width`. The `Rectangle` class has a method which can compute the area."""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3)
print(f"The area of the rectangle is: {rectangle.compute_area()}")

"""8) Define a class Person and its two child classes: `Male` and `Female`. All classes have a method `getGender` which can print `Male` for `Male` class and `Female` for `Female` class."""

class Person:
    def getGender(self):
        print("Unknown")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

gender = Person()
gender.getGender()

male = Male()
male.getGender()

female = Female()
female.getGender()