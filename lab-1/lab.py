
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
            val = restriction_dict[0].get('x'+ str(i+1))
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