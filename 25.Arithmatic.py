
def arithmetic_arranger(problems, show_answers = False):

    if len(problems) > 5:
        return "Error: Too many problems."


    first_operands = [] 
    second_operands = [] 
    operators = [] 
    results = []

    for problem in problems:
        parts = problem.split()

        if parts[1] != '+' and parts[1] != '-':
            return "Error: Operator must be '+' or '-'."
        
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."
    
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_line = '' 
        second_line = '' 
        dashes_line = '' 
        results_line = ''

        pass
    # return "All problems are valid."


print(f'arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])')