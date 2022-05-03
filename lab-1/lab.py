
def parse_equation(equation):
    result = equation.replace('+', '')
    d = dict(x.split('x') for x in result.split())

    d = {f"x{v}": k for k, v in d.items()}

    for key, value in d.items():
        if value == '-':
            d[key] = -1
        if value == '':
            d[key] = 1

    return d


def parse_restriction(restriction):

    upper_bound = False

    equation = restriction.split('<=' or '>=')
    d = parse_equation(equation[0])

    if(restriction.find('<')):
        upper_bound = True

    equation[1] = equation[1].replace(' ', '')

    return(d, upper_bound, equation[1])
