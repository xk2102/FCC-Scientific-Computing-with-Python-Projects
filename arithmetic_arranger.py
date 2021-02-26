

def arithmetic_arranger(problems, solutions=False):

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    
    if len(problems) > 5:
      return 'Error: Too many problems.'

    for x in problems:
      y = x.split()

      if y[1] != '+' and y[1] != '-':
        return "Error: Operator must be '+' or '-'."
      
      if not y[0].isdigit() or not y[2].isdigit():
        return "Error: Numbers must only contain digits."

      if len(y[0]) > 4 or len(y[2]) > 4:
        return "Error: Numbers cannot be more than four digits." 

      if y[1] == "+":
        solution = int(y[0]) + int(y[2])
      else:
        solution = int(y[0]) - int(y[2]) 

      list1.append(y[0])
      list2.append(y[1])
      list3.append(y[2])
      list4.append(solution)

    print("LISTS: ")
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print("---------------------------------------")

    for x in range(0, len(list1)):

      width = max(len(list1[x]), len(list3[x]))
      
      line1 = line1 + (str(list1[x])).rjust(width + 2) + "    "
      line2 = line2 + str(list2[x]) + " " + (str(list3[x])).rjust(width) + "    "
      line3 = line3 + ("-"*(width + 2)).rjust(width) + "    "
      line4 = line4 + (str(list4[x]).rjust(width + 2)) + "    "
      


    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

    if solutions:
      arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()

    print("SOLUTION: ")
    # print(arranged_problems)
    return arranged_problems
    

# Error: Too many problems.
# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 - 2000", "1+1"], True))
# Error: Operator must be '+' or '-'.
# print(arithmetic_arranger(["32 + 698", "3801 * 2", "45 + 43", "123 + 49", "1 - 2000"], True))
# Error: Numbers must only contain digits.
# print(arithmetic_arranger(["32 + a698", "3801 * 2", "45 + 43", "123 + 49", "1 - 2000"], True))
# Error: Numbers cannot be more than four digits.
# print(arithmetic_arranger(["32 + 11698", "3801 * 2", "45 + 43", "123 + 49", "1 - 2000"], True))

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))