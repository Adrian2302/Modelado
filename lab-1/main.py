from lab import *
import numpy
if __name__ == "__main__":

    #equation = "x1 -x2 <= 40"
    # parse_restriction(equation)
    objective = "x1 + 4x2"
    restrictions_list = ["-10x1 + 20x2 <= 22",
                         "5x1 + 10x2 <= 49",
                         "x1 <= 5"]
    maximize = True

    problem = parse_problem(objective, restrictions_list, maximize)
    simplex = simplex(problem[0], problem[1], problem[2], maximize)
