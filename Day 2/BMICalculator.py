# Don't change the code below
height = input("Enter your Height in m: ")
weight = input("Enter your Weight in kg: ")
# Don't change the code above

#BMI = int(weight)/(float(height)*float(height))print("BMI is: ",int(BMI))

BMI = int(weight)/float(height)*float(height)

print("Your BMI is : " + str(BMI))
