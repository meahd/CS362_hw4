#HW4-Q4
#David Meah - CS362 - 2/7/2021

#Input validation function
def IntInputValidationForElements(user_input):
    while True: #Loops till right input is entered
        try:
            tempVal = int(input(user_input))
            if(tempVal <= 0):
                raise ValueError("No Numbers 0 and under ")
        except ValueError:
            print("Error: Invalid Input")
            print("Try again")
            continue
        else:
            return tempVal #If not ValueErrors then break out of loop
            break

def floatInputValidation(user_input):
    while True: #Loops till right input is entered
        try:
            tempVal = float(input(user_input))
        except ValueError:
            print("Error: Invalid Input")
            print("Try again")
            continue
        else:
            return tempVal #If not ValueErrors then break out of loop
            break

def average(lst):
    return sum(lst)/len(lst)
#Main

lst = []
numInList = IntInputValidationForElements("Number of Elements: ")

for i in range(0, numInList):
    ele = floatInputValidation("Enter Element: ")
    lst.append(ele)

print("List: ",lst)
print("Average: ", round(average(lst),2))
