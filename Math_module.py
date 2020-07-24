

#Set Constants
PI=3.141592653589793
e=2.718281828459045

#Calculate power
def Pow(base,exp): # exp:Exponent
    
    if exp==0:
        return 1
    if exp%2==0:
        return Pow(base,exp//2)*Pow(base,exp//2)
    
    return base*Pow(base,exp//2)*Pow(base,exp//2)


#Calculate square root        
def Sqrt(n):

    if n<0:
        raise ValueError("number should be positive ")

    x=n
    y=(x+1)*0.5
    while y<x:
        x=y
        y=(x+n/x)*0.5
        
    return x


#Calculate euclidean distance of Multiple Dimenstions
def Dist(Point_1,Point_2):

    if len(Point_1)!=len(Point_2):
        raise ValueError("Both points must have the same number of dimensions")

    distance=0
    for cordinate_1,cordinate_2 in zip(Point_1,Point_2):

        distDifference=cordinate_2-cordinate_1
        squaredDistance=(distDifference**2)
        distance+=squaredDistance

    distance=Sqrt(distance)

    return distance



#Calculate Factorial of a number
def Factorial(num):

    if num<0:
        raise ValueError("Factorial() not defined for negative value")

    if num==1 or num==0:
        return 1

    return Factorial(num-1)*num


#Number of  ways to choose K items from N items
def Combination(n,k):

    if n<0 or k<0:
        raise ValueError("n and k should be positive integer")

    if n<k:
        return 0

    numberOfWays=1

    for i in range(n,max(n-k,k),-1): #Finding max(n-k,k) reduce the number of loops
        numberOfWays*=i

    numberOfWays//=Factorial(min(n-k,k))
    
    return numberOfWays


#Number of ways to choose K items from N items
def Permutation(n,k):

    if n<0 or k<0:
        raise ValueError("n and k should be positive integer")

    if n<k:
        return 0
    
    numberOfWays=Factorial(n)
    numberOfWays//=Factorial(n-k)

    return numberOfWays


#Complex number
def Complex(a=None,b=None):

    if a==None and b==None:
        return 0j

    if b==None:
        return a+0j

    if b<0:
        return str(a)+str(b)+"j"
    
    return str(a)+str("+")+str(b)+"j"



#Get real number of complex number as float value
def Real(num):

    isNegative=False
    if num[0]=='-':
        num=num[1:]
        isNegative=True

    real=""
    for char in num:

        if char=="-" or char=="+":
            break
            
        real+=char

    if isNegative:
        return float(real)*-1
    
    return float(real)    


#Get imaginary number of complex number as float value
def Imag(num):

    isNegative=False
    
    imag=""
    num=num[:-1]

    i=len(num)-1
    while True:
        
        char=num[i]
        if char=="-":
            isNegative=True
            break
        elif char=="+":
            break
            
        imag+=char
        i-=1

    imag=imag[::-1]
    if isNegative:
        return float(imag)*-1
    
    return float(imag)


#Calculate Absolute value
def Abs(num):

    if num<0:
        return num*-1

    return num


#Compare value
def Compare(a,b):

    if (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float):
        
        if a==b:
            return 0    #If both are equal

        if a>b:
            return 1    #If first number is greater than second
        
        return -1       #If second number is greate than first

    raise ValueError("Input values should be either int or float")



#Calculate Gcd (Greatest common divisior) of a number
def gcd(num_1,num_2):  
    if num_1==0 : 
        return num_2  
      
    return gcd(num_2%num_1,num_1)



#Calculate the sum of iterable objects
def Sum(iterableObject):

    Sum=0
    for value in iterableObject:
        Sum+=float(value)

    return Sum



#Convert degree to radians
def Radians(degree):

    return (degree/180)*PI


#Convert radian to degree
def Degrees(radian):

    return 180/PI*radian


#Check Prime number
def CheckPrime(num):
    
    if num<=0:
        raise ValueError("Input should be positive integer")
    
    if num==1:
        return False
    if num==2:
        return True

    i=2
    while i*i<=num:
        
        if num%i==0:
            return False    #Number is not Prime
        i+=1

    return True
            
        
#Floor value of number (Greatest integer less than or equal to input number)
def Floor(num):

    if type(num)==int:
        return num
    
    if num>=0:
        return int(num)

    return int(num)-1


#Ceil value of number (Smallest integer greater than or equal to input number)
def Ceil(num):
    
    if type(num)==int:
        return num
    
    if num==0:
        return 0
    if num>0:
        return int(num)+1

    return int(num)


#Convert decimal to binary
def Bin(num):

    if num==0:
        return "0"

    isNegative=False
    if num<0:
        isNegative=True
        num=Abs(num)

    binary=""

    while num>0:
        
        binary+=str(num%2)
        num//=2

    binary=binary[::-1]

    if isNegative:
        return "-"+binary
    
    return binary


#Convert decimal to octal
def Oct(num):

    if num==0:
        return "0"

    isNegative=False
    if num<0:
        isNegative=True
        num=Abs(num)

    octal=""

    while num>0:
        
        octal+=str(num%8)
        num//=8

    octal=octal[::-1]

    if isNegative:
        return "-"+octal
    
    return octal


#Convert decimal to hexamdecimal
def Hex(num):

    if num==0:
        return "0"

    isNegative=False
    if num<0:
        isNegative=True
        num=Abs(num)

    hexa=""

    while num>0:

        if num%16>=10:
            hexa+=chr(num%16+55)
        else:
            hexa+=str(num%16)
        num//=16

    hexa=hexa[::-1]

    if isNegative:
        return "-"+hexa

    return hexa



print("Power : ",Pow(2,7))
print("Square root : ",Sqrt(361))
print("Euclidean Distance : ",Dist([2,4,5,1,4],[4,1,5,1,4]))
print("Factorial : ",Factorial(8))
print("Combination : ",Combination(23,14))
print("Permutation : ",Permutation(21,10))
print("Complex Number : ",Complex(5,-4.58))

complex_=Complex(5,-4.58)
print("Real Number of complex number : ",Real(complex_))
print("Imaginary Number of complex number : ",Imag(complex_))
print("Absolute value : ",Abs(-56.454))
print("Compare : ",Compare(43.22,43.22))
print("Greatest common divisior : ",gcd(70,28))
print("Sum : ",Sum([2,3,5,3,6.5]))
print("Degree to radians : ",Radians(60))
print("Radians to Degree : ",Degrees(70))
print("Check Prime number : ",CheckPrime(37))
print("Floor : ",Floor(5.3))
print("Ceil : ",Ceil(22.5))
print("Decimal to Binary : ",Bin(58))
print("Decimal to Octal : ",Oct(95))
print("Decimal to Hexadecimal : ",Hex(69754))

