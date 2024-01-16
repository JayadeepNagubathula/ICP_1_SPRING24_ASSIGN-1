def char(string, x, y): # defining the function to remove the characters
    a = string.replace(x,'') # removing the 1st character
    b = a.replace(y,'') #removing the 2nd character
    return b # returning the result to the function created thatis char.
string = input("Enter a string: ") #taking the input as string from the user
x= input("Enter the character to remove: ")# taking the 1st character from the user
y= input("Enter the character to remove: ")#taking the 1st character from the user

b = char(string, x, y) #calling the function
print(f"String after removing '{x}','{y}' : {b}")# printing the string after removing the characters
print("the reversed string is:" + b[::-1]) # reverse the string.


