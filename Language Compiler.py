from itertools import permutations

RUNNING = True

strs='quit'
quit_vars=[''.join(x)for x in  permutations(list(strs)+list(strs.upper()),4) if ''.join(x).lower()=='quit']

strs='print'
print_vars=[''.join(x)for x in  permutations(list(strs)+list(strs.upper()),5) if ''.join(x).lower()=='print']

strs='comb'
comb_vars=[''.join(x)for x in  permutations(list(strs)+list(strs.upper()),4) if ''.join(x).lower()=='comb']

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def check(List):
    global RUNNING
            
    if len(List) > 6:
        if List[0] + List[1] + List[2] + List[3] + List[4] in print_vars:
            temp_string = ""
            if List[5] == " ":
                num_val = 6
            else:
                num_val = 5
            for letter in List:
                if num_val == 0:
                    temp_string += letter
                else:
                    num_val -= 1

            print("\n" + temp_string + "\n")
            
    if len(List) == 4:
        if List[0] + List[1] + List[2] + List[3] in quit_vars:
            RUNNING = False

    if List[0] in nums:
        temp_num1 = ""
        temp_num2 = ""
        number = 1
        operation = ""
        for index in List:
            if operation == "division" and (index == "r" or index == "R"):
                    operation = "remainder"
            if index != " " and index in nums:
                if number == 1:
                    temp_num1 += str(index)
                elif number == 2:
                    temp_num2 += str(index)
            elif index == "+":
                operation = "additive"
                number += 1
            elif index == "-":
                operation = "subtractive"
                number += 1
            elif index == "*":
                operation = "multiplication"
                number += 1
            elif index == "/":
                operation = "division"
                number += 1
            elif index == "^":
                operation = "power"
                number += 1
            

        if operation == "additive":
            temp_num3 = int(temp_num1) + int(temp_num2)
        elif operation == "subtractive":
            temp_num3 = int(temp_num1) - int(temp_num2)
        elif operation == "multiplication":
            temp_num3 = int(temp_num1) * int(temp_num2)
        elif operation == "division":
            temp_num3 = int(temp_num1) / int(temp_num2)
        elif operation == "power":
            temp_num3 = int(temp_num1) ** int(temp_num2)
        elif operation == "remainder":
            temp_num3 = int(temp_num1) / int(temp_num2)
            temp_num3 = round(temp_num3, 0)
            temp_num3 = str(temp_num3)[:-2]
            temp_num4 = int(temp_num1) % int(temp_num2)

        if operation == "remainder":
            print("\n" + str(temp_num3) + " Rem. " + str(temp_num4) + "\n")
        else:
            print("\n" + str(temp_num3) + "\n")

while RUNNING:
    string = input("Input your code:\n")
    if string != None:
        letters = []
        for letter in str(string):
            letters.append(letter)
        check(letters)
