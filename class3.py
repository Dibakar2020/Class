# using keyword argument

def adder(*args, good=1, bad=2, ugly=3):
    return sum(args) + good + bad + ugly

if __name__ == "__main__":
    # Testing the adder function with keyword arguments
    result_keywords = adder(ugly=1,good=5)

    print("Result for adder with keyword arguments:", result_keywords)
