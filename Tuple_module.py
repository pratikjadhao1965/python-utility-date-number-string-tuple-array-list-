tuple_name=("I","N","D","I","A")


#index(): Index of first occurrence of value
def index(tuple_name,value):
    for i in range(len(tuple_name)):
        if(tuple_name[i]==value):
            return i
        i+=1

print (index(tuple_name, "A"))



#count(): count the number of occurrences of given element
def count( tuple_name ,value):
    count=0
    for i in range(len(tuple_name)):
        if(tuple_name[i]==value):
            count+=1   
    return count

print(count(tuple_name,"I"))


# delete element  using index slicing (but it is tuple)
# def delete(tuple_name,index):
#     y=tuple_name[:index] + tuple_name[index+1:]
#     return y

# print(delete(tuple_name,2))
