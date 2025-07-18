import art


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

calc_dict = {
    "+" : add ,
    "-" : sub ,
    "*" : multi ,
    "/" : div ,
}



def calc():
    print(art.logo)
    should_accumulate = True
    num_1 = int(input("What is you first number ?"))

    while should_accumulate :
        for symbol in calc_dict:
            print (symbol)
        operation_symbols = input("Pick you operation ")
        num_2 = int(input("What is you second number ?"))
        answer = calc_dict[operation_symbols](num_1, num_2)
        print(f"{num_1}{operation_symbols}{num_2} = {answer}")


        choice = input("Type y to continue , n to discontinue")

        if choice == "y":
            num_1 = answer

        if choice == "n":
            should_accumulate = False
            print("\n*20")
            calc()

calc()






