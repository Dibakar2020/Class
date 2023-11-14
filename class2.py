# arbitrary number of argument 

def adder(*arg):
    return sum(arg)

if __name__ == "__main__":
    # Testing the adder function
    result_floats = adder(3.14, 2.71,1.41,10)
    print("Result for floats addition:", result_floats)
