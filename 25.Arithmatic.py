# def arithmetic_arranger(problems, show_answers = True):

#     if len(problems) > 5:
#         return "Error: Too many problems."

#     first_operands = [] 
#     second_operands = [] 
#     operators = [] 
#     results = []

#     for problem in problems:
        
#         parts = problem.split()
        
#         if len(parts) != 3:
#             return "Error: Invalid Problem."

#         if parts[1] != '+' and parts[1] != '-':
#             return "Error: Operator must be '+' or '-'."
        
#         if not parts[0].isdigit() or not parts[2].isdigit():
#             return "Error: Numbers must only contain digits."
    
#         if len(parts[0]) > 4 or len(parts[2]) > 4:
#             return "Error: Numbers cannot be more than four digits."
        
#         num1 = parts[0] 
#         operator = parts[1]
#         num2 = parts[2] 
        
#         # print(num1, " ", operator, " ", num2)
        
#         first_operands.append(num1)
#         operators.append(operator)
#         second_operands.append(num2)
        
#         if show_answers:
            
#             if operator == '+':
#                 results.append(str(int(num1) + int(num2)))
#             if operator == '-':
#                 results.append(str(int(num1) - int(num2)))

#     # print(first_operands[1])

#     # print(type(first_operands))
    
#     max_width = max(len(num) for num in first_operands + second_operands) + 2

#     # print(maxWidth)
#     # num1 = first_operands[0].rjust(maxWidth)
#     # print(num1)    

#     first_line = ''
#     second_line = ''
#     third_line = ''
#     answer_line = ''
    
#     for i in range(len(problems)):
#         num1 = first_operands[i].rjust(max_width)
#         num2 = second_operands[i].rjust(max_width - 1)
#         operator = operators[i]
#         result = results[i] if show_answers else ""
        
#         first_line += num1 + "    "
#         second_line += operator + "" + num2 + "    "
#         third_line += "-" * max_width + "    "
#     #   # print("-" * 5)
        
#         if show_answers:
#             answer_line += result.rjust(max_width) + "    "
         
#     # print(first_line)
#     # print(second_line)
#     # print(third_line)
#     # print(answer_line)
          
#     if show_answers:
#         return f"{first_line}\n{second_line}\n{third_line}\n{answer_line}"
#     else:
#         return f"{first_line}\n{second_line}\n{third_line}"

# print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
# print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
# print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
# print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
# print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))






def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."

    first_lines = []
    second_lines = []
    third_lines = []
    answer_lines = []

    for problem in problems:
        
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid Problem."
        
        num1, operator, num2 = parts
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Determine the width for this problem
        width = max(len(num1), len(num2)) + 2
        
        # Format each line for the current problem
        first_lines.append(num1.rjust(width))
        second_lines.append(operator + num2.rjust(width - 1))
        third_lines.append("-" * width)
        
        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answer_lines.append(result.rjust(width))
    
    # Join each part with 4 spaces in between
    arranged_first = "    ".join(first_lines)
    arranged_second = "    ".join(second_lines)
    arranged_third = "    ".join(third_lines)
    
    if show_answers:
        arranged_answer = "    ".join(answer_lines)
        return f"{arranged_first}\n{arranged_second}\n{arranged_third}\n{arranged_answer}"
    else:
        return f"{arranged_first}\n{arranged_second}\n{arranged_third}"

# Example calls:
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))  

