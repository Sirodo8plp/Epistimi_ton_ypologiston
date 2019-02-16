#n0=number 0 , n1=number 1 etc. etc.

def zero():
    return 0

def one():
    return 1

def two():
    return 2
   
def three():    
    return 3

def four():
    return 4
   
def five():
    return 5

def six():
    return 6

def seven():
    return 7

def eight():
    return 8

def nine():
    return 9

#prosthesi
def plus(number1,number2):
    sum=number1+number2
    return sum

#pollaplasiasmos

def times(number1,number2):
    product=number1*number2
    return product

#afairesh

def minus(number1,number2):
    sum=number1-number2
    return sum

#diairesh

def divided(number1,number2):
    counter=0
    while((number1-number2)>=0):
        counter +=1
        number1 -=number2
    return counter



order=input("Give me an order.The order must have the form of 'print five(times(seven()))',for example. ")

while ("print " not in order):
    order=input("The order must have the form of 'print five(times(seven()))',for example.Give me an order again! ")

#brisko tous arithmous kai thn zitoumeni praksi kai ta apothikeuo se metablites
#tha ftiaxo enan pinaka me deka theseis(10 arithmoi)
#kathe thesi tha exei eite -1 eite enan arithmo x>0
#o opoios deixnei th thesi enos arithmou
#meta tha kano sort me auksousa seira gia na bro ton number1
#gia ton number2 tha kano sort me fthinousa seira
#metrao enas  o pinakas matrix exei 2 thetikous arithmous giati enan o xristis grapsei four(times(four())) tote tha mpei mono mia thetiki timi ston pinaka


numbers=['zero','one','two','three','four','five','six','seven','eight','nine']

matrix=[0]*10
matrix1=[0]*10
for i in range(0,10):
    matrix[i]=order.find(numbers[i])
    matrix1[i]=numbers[i]

counter=0
position=0
for i in range(0,10):
    if matrix[i]>0:
        counter +=1
        position=i

if counter==1:
    number1=eval(matrix1[position])()
    number2=eval(matrix1[position])()
else:
    for i in range(1,10):
        for j in range(9,i,-1):
            if matrix[j-1]>matrix[j]:
                tmp=matrix[j-1]
                matrix[j-1]=matrix[j]
                matrix[j]=tmp

                tmp=matrix1[j-1]
                matrix1[j-1]=matrix1[j]
                matrix1[j]=tmp


    number1=eval(matrix1[8])()
    number2=eval(matrix1[9])()



if 'times' in order:
    print(times(number1,number2))
elif 'plus' in order:
    print(plus(number1,number2))
elif 'minus' in order:
    print(minus(number1,number2))
elif 'divided' in order:
    print(divided(number1,number2))
else:
    print("Something is wrong!Please,restart the aplication and try again!")





