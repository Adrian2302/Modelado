from lab import *
import numpy
if __name__ == "__main__":

    #equation = "x1 -x2 <= 40"
    # parse_restriction(equation)
    objective = "2.7x1 + 1.87x2"
    restrictions_list = ["6x1 + x2 <= 360",
                         "x1 + 5x2 <= 350",
                         "x1 + 2x2 >= 20"]
    maximize = False

    problem = parse_problem(objective, restrictions_list, maximize)
    simplex = simplex(problem[0], problem[1], problem[2], maximize)
