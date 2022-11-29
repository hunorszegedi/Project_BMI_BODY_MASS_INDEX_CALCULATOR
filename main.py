your_weight = input("Enter your weight: ")
your_height = input("Enter your height: ")

BMI = (int)((int)(your_weight) / (float)(your_height) ** 2)

if BMI <= 18.5:
    print(BMI, " You are underweight!\n")
elif BMI >= 18.5 and BMI <= 25:
    print(BMI, " You are normal weight!\n")
elif BMI >= 25 and BMI <= 30:
    print(BMI, " You are overweight!\n")
elif BMI >= 30:
    print(BMI, " You are obesse!\n")
else: print("Error!\n")
