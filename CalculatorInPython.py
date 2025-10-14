#building a basic calculator
First_Value=int(input('enter the first number'))
Second_Value=int(input('enter the secont values'))
sign=input('enter the operator of the function that you want to perform ')
if type(First_Value)==str or type(Second_Value)==str or type(First_Value)==bool or type(Second_Value)==bool:
    print('you cannot  enter the string or boolean value') 
elif sign=='+':
 print(First_Value+Second_Value) 
elif sign=='-':
 print(First_Value-Second_Value) 
elif sign=='*':
 print(First_Value*Second_Value) 
elif sign=='/':
 print(First_Value/Second_Value) 
else:
  print('looks like  you did not enter any valid operator')
  print('try again and enter any of these operator +,-,*,/')