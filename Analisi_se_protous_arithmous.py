def NextPrime(y): #finds the next prime number#
    x=y+1
    while True:
        
        counter = 0
        for i in range(1,x+1):
            if x%i==0: counter +=1
        if counter==2:break
        else: x +=1
    return x


while True:
    number=int(input("Give an integer,greater than 1 and lesser than 1.000.000. "))
    if number>1 and number<=1000000:break

counter =0
for i in range(1,number+1):
    if number%i==0: counter +=1

if counter==2: print(number," is a prime number itself.It cannot be analysed in prime numbers.")
else:
    
    number1=number
    primeNumbers=[]
    appearances=[]
    prime = 2  #first prime number#

    
    flag=False
    q = 0
    
    while True:
        if number%prime==0:
            if flag==False:
                primeNumbers.append(prime)
                flag=True
            number = number//prime
            q +=1

        else:
            if flag==True:
                appearances.append(q)
                q=0
                flag=False
            elif number==1:
                primeNumbers.append(1)
                appearances.append(1)
                break
            else:
                y=0
                for i in range(1,number+1):
                    if number%i==0:y +=1
                if y==2:
                    primeNumbers.append(number)
                    appearances.append(1)
                    break
                else:
                    while True:
                        prime=NextPrime(prime)
                        if number%prime==0:break
            
            
    
    #=====print the analysis=====#

    mystr=""
    openp="("
    closep=")"
    multiply="**"
    for i in range(0,len(appearances)):
        if appearances[i]!=1:
            mystr1=str(appearances[i])
            mystr2=str(primeNumbers[i])
            mystr += openp+mystr2+multiply+mystr1+closep
        else:
            mystr2=str(primeNumbers[i])
            mystr +=openp+mystr2+closep
    
    print (mystr)     
      
            


