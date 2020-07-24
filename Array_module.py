import array

#Append function
def Append(Array,Value):
    updatedArray=list(Array)+[Value]
    
    return array.array(Array.typecode,updatedArray)
    

#Pop element from array
def Pop(Array,Index=None):
    
    #If index is not pass in function call then pop last element of Array
    
    if Index==None:        
        updatedArrayList=Array[:-1]
        
        return array.array(Array.typecode,updatedArrayList)

    #Check Negative Indexing
    
    if Index<0:     
        Index=len(Array)+Index
        
    if Index<0 or Index>=len(Array):
        raise IndexError("Index range out of Bound")

    updatedArray=[value for index,value in enumerate(Array) if index!=Index]
    
    return array.array(Array.typecode,updatedArray)
    
        
#Remove first occurence of given value
def Remove(Array,Value):
    for index,value in enumerate(Array):
        if value==Value:
            return Pop(Array,index)
        
    return Array


#Insert new element by index
def Insert(Array,Index,Value):

    #Check negative indexing
    
    if Index<0:     
        Index=len(Array)+Index
        if Index<0:
            Index=0

    updatedArray=list(Array[:Index])+[Value]+list(Array[Index:])

    return array.array(Array.typecode,updatedArray)
    

#Frequency of given value in array
def Count(Array,Value):
    count=0
    for value in Array:
        if value==Value:
            count+=1
            
    return count


#Extend new Array
def Extend(Array,NewArray):
    updatedArray=list(Array)+list(NewArray)
    
    return array.array(Array.typecode,updatedArray)


#Convert Array to list
def ToList(Array):
    
    return list(Array)

#Append list at end of array
def FromList(Array,list_):
    updatedArray=list(Array)+list_
    
    return array.array(Array.typecode,updatedArray)


#Return Index of first occurence of given value
def Index(Array,Value):
    for index,value in enumerate(Array):
        if value==Value:
            return index
        
    raise ValueError(str(Value)+" is not present in Array")


#Reverse array
def Reverse(Array):
    updatedArray=Array[::-1]
    
    return array.array(Array.typecode,updatedArray)

    
#Append unicode string
def FromUnicode(Array,Value):
    if Array.typecode!='u':
        raise ValueError("FromUnicode() may only be called on unicode type arrays")
    updatedArray=""
    for char in Array:
        updatedArray+=char
    for char in Value:
        updatedArray+=char
        
    return array.array(Array.typecode,updatedArray)
    

#Convert Unicode array to Unicode string
def ToUnicode(Array):
    if Array.typecode!='u':
        raise ValueError("ToUnicode() may only be called on unicode type arrays")
    unicodeList=list(Array)
    unicodeString="".join(unicodeList)
    
    return unicodeString
    


Array=array.array('i',[3,54,6,2,3,5])
print("Array  : ",Array,end="\n\n")
print("Append : ",Append(Array,90),end="\n\n")
print("Pop without index : ",Pop(Array),end="\n\n")
print("Pop with index : ",Pop(Array,3),end="\n\n")
print("Remove : ",Remove(Array,3),end="\n\n")
print("Insert : ",Insert(Array,3,100),end="\n\n")
print("Count : ",Count(Array,3),end="\n\n")

NewArray=array.array('i',[100,200,300])
print("Extend array : ",Extend(Array,NewArray),end="\n\n")
print("Convert array to list : ",ToList(Array),end="\n\n")

list_=[500,600,700]
print("Append list in array : ",FromList(Array,list_),end="\n\n")
print("First occurent of value : ",Index(Array,54),end="\n\n")
print("Reverse Array : ",Reverse(Array),end="\n\n")

string=" International pvt ltd"
arr=array.array('u','Xpanxion')
print("Append unicode string : ",FromUnicode(arr,string),end="\n\n")
print("Convert unicode array to unicode string : ",ToUnicode(arr),end="\n\n")


















