list_name=[1,2,3, 3 , 3]

# 1] append() : add item at the end of list

def append(list_name, z):
    y = list_name + [z]
    return y 

list_name=append(list_name,4)
print (list_name)


#2] insert(): insert item at perticular location

def insert(list_name,value,index):
    y = list_name[:index] + [value] + list_name[index:]
    return y
   
list_name = insert( list_name, 5, 1)
print (list_name)



#3] remove() : remove item from the list
def remove(list_name,x):
    y=[list_name[i] for i in range(len(list_name)) if(list_name[i]!=x)]
    return y 
    
list_name= remove(list_name, 5)  
print (list_name)      


#4] pop():pop item from given index
def pop(list_name,index):
    y=[list_name[i] for i in range(len(list_name)) if(i!=index)]
    return y
     
list_name= pop(list_name, 3)  
print (list_name)  


#5] reverse(): reverse list 
def reverse(list_name):
    y=list_name[::-1]
    return y

list_name= reverse(list_name)
print(list_name)



#6] len() : finding length of list
def len(list_name):
    count=0
    for i in list_name:
        count+=1
        i+=1
    return count

print(len(list_name))


#7] count(): count the number of occurrences of given element
def count( list_name ,x):
    count=0
    for i in range(len(list_name)):
        if(list_name[i]==x):
            count+=1
        
    return count

print(count(list_name,3))

#8] copy(): copying list to another
new_list=[]
def copy(list_name,new_list):
    new_list=list(list_name)
    return new_list

print(copy(list_name, new_list))


#9] index():Returns the index of the first element with the specified value
def index(list_name,value):
    for i in range(len(list_name)):
        if(list_name[i]==value):
            return i
        i+=1

print (index(list_name, 3))

