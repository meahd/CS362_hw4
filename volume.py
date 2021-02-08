#HW4-Q4
#David Meah - CS362 - 2/7/2021

#Input validation function
def floatInputValidation(user_input):
    while True: #Loops till right input is entered
        try:
            tempVal = float(input(user_input))
            if(tempVal < 0):
                raise ValueError("No Negative Numbers")
        except ValueError:
            print("Error: Invalid Input")
            print("Try again")
            continue
        else:
            return tempVal #If not ValueErrors then break out of loop
            break


def calcVol(w,l,h):
    return w*l*h

#Main
print("\n<<Cube Volume Calculator Application >>")

width = floatInputValidation("Width: ")
length = floatInputValidation("Length: ")
height = floatInputValidation("Height: ")

print("Volume: ", calcVol(width,length,height))
