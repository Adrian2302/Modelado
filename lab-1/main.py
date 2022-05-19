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

    solution = simplex_solver(objective, restrictions_list, maximize)
    print(
        f"Simplex call:\nSol: {solution[0]}\nOptimized max/min: {solution[1]}")
