def calc_bmi(height, weight):
    try:
        bmi = weight / height ** 2
    except:
        print('>>> Error! Oops)))')
    if bmi < 18:
        print(f"Your bmi: {bmi}\nYou're underweight!")
    elif bmi > 18 and bmi < 24.9:
        print(f"Your bmi: {bmi}\nYour BMI is fine!")
    elif bmi > 25 and bmi < 29.9:
        print(f"Your bmi: {bmi}\nYou are overweight!")
    else:
        print(f"Your bmi: {bmi}\nYou're obese! You need to lose weight!")
 
height = float(input('>>> Enter your height in metres \n(example: 1.70): '))
weight = float(input('>>> Enter your weight in kg: '))

calc_bmi(height, weight)