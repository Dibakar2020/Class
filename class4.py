# arbitrary number of keyword argument

def adder(*args,**keyw):
    return sum(args)+sum(keyw.values())
if __name__=="__main__":
    # Testing the generalized adder function with arbitrary keyword arguments
    result_arbitrary_keywords=adder(good=1,better=2,bad=1,argy=2)
    print("Result for adder with arbitrary keyword arguments:", result_arbitrary_keywords)
    