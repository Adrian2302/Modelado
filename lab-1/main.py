from lab import *

if __name__ == "__main__":

    equation = "x1 -x2 <= 40"
    #parse_restriction(equation)

    restrictions_list = ["x1 + x2 <= 7", 
                         "4x1 + 10x2 <= 40", 
                         "10x1 >= 30"]
    result = parse_problem("30x1 + 100x2", restrictions_list, True)

    print(result[0])
    print(result[1])
    print(result[2])