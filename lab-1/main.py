from lab import *
import numpy
if __name__ == "__main__":

    #equation = "x1 -x2 <= 40"
    # parse_restriction(equation)
    objective = "30x1 + 100x2"
    restrictions_list = ["x1 + x2 <= 7",
                         "4x1 + 10x2 <= 40",
                         "10x1 >= 30"]
    maximize = True

    problem = parse_problem(objective, restrictions_list, maximize)
    simplex = simplex(problem[0], problem[1], problem[2], maximize)
