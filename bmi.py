def BMI(height,weight):
    bmi=weight/(height**2)
    return bmi
height=1.79832
weight=70

bmi=BMI(height,weight)
print("the BMI is",format(bmi), "so",end='')
if(bmi<18.5):
  print("underweight")
  print("malnutrition risk")
elif(bmi>=18.5 and bmi<24.9):
  print("normal weight")
  print("low risk")
elif(bmi>=25 and bmi<29.9):
  print("overweight")
  print("enhanced risk")
elif(bmi>=30 and bmi<34.9):
  print("moderately obese")
  print("medium risk")
elif(bmi>=35 and bmi<39.9):
  print("severely obese")
  print("high risk")
elif(bmi>=40):
  print("very severely obese")
  print("very high risk")
