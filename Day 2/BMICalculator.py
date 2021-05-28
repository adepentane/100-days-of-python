# Don't change the code below
height = input("Enter your Height in m: ")
weight = input("Enter your Weight in kg: ")
# Don't change the code above

BMI = int(weight)/float(height)** 2
BMI_as_int = int(BMI)

print("Your BMI is : " + str(BMI_as_int))
