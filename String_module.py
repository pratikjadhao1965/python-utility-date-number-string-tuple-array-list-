#.returns a string converted to Uppercase
def uppercase(string):
    updated_string=""
    for char in string:
        if ord(char) not in range(97,123):
            updated_string+=char
        else:
            updated_string+=chr(ord(char)-32)
    return updated_string

#returns a string converted to Lowercase
def lowercase(string):
    updated_string=""
    for char in string:
        if ord(char) not in range(65,91):
            updated_string+=char
        else:
            updated_string+=chr(ord(char)+32)
    return updated_string

#.returns length of string
def length(string):
    count=0
    for i in string:
        count+=1
    return count

#returns first letter of string converted to Uppercase.
# (first need to run uppercase,lowercase functions above as they are used in this function)
def strcapitalize(string):
    return uppercase(string[:1])+lowercase(string[1:])

#returns count of occurences of word in a string
# (if needed we can provide starting and ending index)
# (first need to run length function above as it is used in this function)
def strcount(string,word,start=None,end=None):
    count=0
    if start==None:
        start=0
    if end==None:
        end=length(string)-length(word)
    for i in range(start,end+1):
        if string[i:i+length(word)]==word:
            count+=1
    return count

# returns index of first occurenece of word in a string
# (if needed we can provide starting and ending index)
# (first need to run length function above as it is used in this function)
def strfind(string,word,start=None,end=None):
    pos=-1
    if start==None:
        start=0
    if end==None:
        end=length(string)-length(word)
    for i,char in enumerate(string):
        if string[i:i+length(word)]==word:
            pos=i
            break
    return pos

#returns centered string
def strcenter(string,width=1,fillchar=" "):
    return f'{string:{fillchar}^{width}s}'

#retunrns True if string is alphanumeric else False
def strisalphanum(string):
    for char in string:
        if ord(char) not in range(48,58) and ord(char) not in range(65,91) and ord(char) not in range(97,123):
            return False
    return True

#returns a string by joining the all elements of an iterable(such as list, string and tuple).
def strjoin(string,iterable):
    updated_string=""
    if len(iterable)!=0 and type(iterable[0])==type(""):
        updated_string=iterable[0]
    for i in iterable[1:]:
        updated_string+=string+i
    return updated_string

#breaks up a string at the specified separator and returns a list of strings(we can specify max. splits to perform).
def strsplit(string,seperator=None,maxsplit=-1):
    split_string=[]
    if seperator==None:
        seperator=" "
    loop=True
    while loop:
        f=strfind(string,seperator)
        if f!=-1 and maxsplit!=0:
            split_string.append(string[:f])
            string=string[f+length(seperator):]
            maxsplit-=1
        else:
            loop=False       
    split_string.append(string)
    return split_string

#.returns a string with first letter of each word capitalized.(first need to run uppercase,lowercase functions)
def strtitle(string):
    updated_string_list=[]
    tmp=""
    for char in string:
        if char==" ":
            updated_string_list.append(uppercase(tmp[0])+lowercase(tmp[1:]))
            tmp=""
        else:
            tmp+=char
    if tmp:
        updated_string_list.append(uppercase(tmp[0])+lowercase(tmp[1:]))
    return strjoin(" ",updated_string_list)

#returns a copy of the string where all occurrences of a substring is
#  replaced with another substring.(we can specify count 
# which decides how many replacement function needs to perform)
def strreplace(string,oldstring,newstring,count=-1):
    for i in range(length(string)):
        if string[i:i+length(oldstring)]==oldstring and count!=0:
            string=string[:i]+newstring+string[i+len(oldstring):]
            count-=1
    return string

#returns the given string into a nicer output.(first need to run strreplace fuction used here)
def strformat(string,*args,**kwargs): 
    for word in args:
        string=strreplace(string,"{}",word,count=1)
    for key, value in kwargs.items(): 
        string=strreplace(string,"{"+key+"}",value,count=1)
    return string   

#strisdigit return true is string contains any digit
def strisdigit(string):
    for char in string:
        if char not in "1234567890":
            return False
    return True

#strisaplha() method returns true if string contains any character
def strisalpha(string):
    for char in string:
        if ord(char) not in range(65,91) and ord(char) not in range(97,123):
            return False
    return True

#The strstrip() method returns a copy of the string by removing both 
# the leading and the trailing characters (based on the string argument passed).
def strstrip(string,chars=" "):
    for s in string:
        if s in chars:
            string=strreplace(string,s,"",1)      
        else:
            break
    for s in string[::-1]:
        if s in chars:
            string=strreplace(string[::-1],s,"",1)[::-1]
        else:
            break
        
    return string

#The strpartition() method splits the string at the first occurrence of the argument
# string and returns a tuple containing the part the before separator, 
# argument string and the part after the separator.
def strpartition(string,seperator):
    split_string=[]
    index=strfind(string,seperator)
    if index!=-1:
        split_string.append(string[:index])
        split_string.append(seperator)
        string=string[index+length(seperator):] 
    split_string.append(string)
    return split_string

print(uppercase("xyz"))
print(length("abcdef"))
print(strcapitalize("abc aAA"))
print(strcount("abba","a",0,2))
print(strfind("hi there","t"))
print(strcenter("aad",24,"0"))
print(strisalphanum("a1ad0akjsc"))
print(strjoin("ax",("ab","bc")))
print(strsplit("hi there,my name is xyz","name",4))
print(strtitle("hello worlD"))
print(strreplace("hello xyz,xyz is from abc town ","xyz","abc",1))
print(strformat("this is py{}.A very {key1} {key2}","thon",key2="language",key1="popular"))
print(strisdigit("11892123"))
print(strisalpha("wq"))
print(strstrip("android is awesome","an"))
print(strpartition("hjvsa a abc","y"))
