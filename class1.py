# math_operations.py

def adder(x, y):
    return x + y

if __name__ == "__main__":
    # Testing the adder function
    result_string = adder("Hello ", "world!")
    result_list = adder([9, 5, 3], [8, 5, 6])
    result_floats = adder(3.14, 2.71)
    print("Result for string addition:", result_string)
    print("Result for list addition:", result_list)
    print("Result for floats addition:", result_floats)
