from operator import methodcaller

class Example:
    def greet(self, name):
        return f"Hello, {name}!"

# Create an instance of the class
example = Example()

# Create a methodcaller for the 'greet' method
greet_caller = methodcaller('greet', 'Alice')

# Call the method
result = greet_caller(example)
print(result) 