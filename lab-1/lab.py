import numpy as np


def parse_equation(equation):
    result = equation.replace('+ ', '')
    result = result.replace('- ', '-')

    d = {}
    for word in result.split():
        key = word[-2:]
        value = word[:-2]
        d[key] = value

    for key, value in d.items():
        if value == '-':
            d[key] = -1
        if value == '':
            d[key] = 1
    return d


def parse_restriction(restriction):
    upper_bound = False
    if('<' in restriction):
        equation = restriction.split('<=')
        upper_bound = True
    else:
        equation = restriction.split('>=')

    d = parse_equation(equation[0])

    equation[1] = equation[1].replace(' ', '')

    return(d, upper_bound, equation[1])


def parse_problem(objective, restrictions, maximize):
    list_obj = []
    list_var = []
    list_rest = []

    equation = parse_equation(objective)
    for key, value in equation.items():
        list_obj.append(value)
        list_var.append(key)

    n_variables = len(list_var)

    for x in restrictions:
        restriction_dict = parse_restriction(x)
        restriction = []
        for i in range(n_variables):
            val = restriction_dict[0].get('x' + str(i+1))
            if (val != None):
                restriction.append(val)
            else:
                restriction.append(0)
            if(i == n_variables-1):
                restriction.append(restriction_dict[2])

        list_rest.append(restriction)
    n_restrictions = len(list_rest)

    iteration = 1
    for x in restrictions:
        restriction_dict = parse_restriction(x)

        if(restriction_dict[1] == True):
            list_var.append('s' + str(iteration))
            list_obj.append(0)
            i = 0
            while i < n_restrictions:
                if(i == iteration-1):
                    list_rest[i].insert(len(list_rest[i])-1, 1)
                else:
                    list_rest[i].insert(len(list_rest[i])-1, 0)
                i += 1

        else:
            list_var.append('s' + str(iteration))
            list_var.append('a' + str(iteration))
            list_obj.append(0)
            if(maximize == True):
                list_obj.append(-1000000000000)
            else:
                list_obj.append(1000000000000)
            i = 0
            while i < n_restrictions:
                if(i == iteration-1):
                    list_rest[i].insert(len(list_rest[i])-1, -1)
                    list_rest[i].insert(len(list_rest[i])-1, 1)
                else:
                    list_rest[i].insert(len(list_rest[i])-1, 0)
                    list_rest[i].insert(len(list_rest[i])-1, 0)
                i += 1
        iteration += 1

    return(list_obj, list_rest, list_var)


def simplex(objective, restrictions, variables, maximize) -> (dict[str, float], float):
    # Primero tenemos que "armar" la tabla simplex, pasamos todo a np array
    restrictions = np.array(restrictions)
    # objective en realidad no es la funcion objetivo, son los valores de las variables (error de enunciado?)
    values = np.array(objective)
    num_restrictions = len(restrictions)
    # Armamos la columna Cb y var, filas Zj y Z-zj
    cb_col = np.array([None]*num_restrictions)
    var_col = np.array([None]*num_restrictions)
    zj_row = np.empty_like(values)
    z_zj_row = np.empty_like(values)
    # Se agregan las restricciones
    for r in range(0, num_restrictions):
        cb_col[r] = values[r]
        var_col[r] = variables[r]
    # Se prefieren las variables artificiales en var_col y cb_col
    artifical_vars = [v for v in variables if "a" in v]
    art_start_index = len(variables) - len(artifical_vars)
    for a in artifical_vars:
        sub_index = int(a[1:])-1
        var_col[sub_index] = a
        cb_col[sub_index] = values[art_start_index]
        art_start_index += 1

    return solve_simplex_r(values, variables, restrictions, cb_col, var_col, zj_row, z_zj_row, maximize)


def solve_simplex_r(values, variables, restrictions, cb_col, var_col, zj_row, z_zj_row, maximize) -> (dict[str, float], float):
    # Se calcula zj
    for i in range(0, len(zj_row)):
        zj_row[i] = np.dot(cb_col, restrictions[:, i])
    # Se calcula z - zj
    z_zj_row = np.subtract(values, zj_row)

    # Se verifica condición de parada

    if maximize:
        if z_zj_row <= 0:
            return  # hay que calcular el resultado
    else:
        if z_zj_row >= 0:
            return  # hay que calcular el resultado

    # Se calcula la columna del pivote
    pivot_col = -1
    if maximize:
        pivot_col = np.argmax(z_zj_row)
    else:
        pivot_col = np.argmin(z_zj_row)
    col_values = restrictions[:, pivot_col]
    # Se calculan los ratios
    # :, -1 es la columna B
    ratios = np.divide(restrictions[:, -1], col_values)
    # Se calcula la fila del pivote
    pivot_row = -1
    lowest_ratio = 1000000
    for i in range(len(restrictions)):
        val = [i]
        if val > 0 and val < lowest_ratio:
            pivot_row = i
    # Ya se tiene el pivote, se pone en 1 la fila del pivote si no lo esta
    if col_values[pivot_row] != 1:
        for i in range(0, len(restrictions[0])):
            restrictions[pivot_row][i] = restrictions[pivot_row][i] / \
                restrictions[pivot_row][pivot_col]
    # Se colocan las demás filas en 0.
    for row in range(0, len(col_values)):
        if row != pivot_row:
            difference = col_values[row] - col_values[pivot_row]
            multiplied_difference = np.multiply(
                restrictions[pivot_row, :], difference)
            restrictions[row] = np.subtract(
                restrictions[0], multiplied_difference)

    return solve_simplex_r(values, variables, restrictions, cb_col, var_col, zj_row, z_zj_row, maximize)
