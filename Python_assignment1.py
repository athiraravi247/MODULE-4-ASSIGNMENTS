############# ASSIGNMENT 1 - Data Structures - Strings & Tuples #############
 
# 1. String Concatenation

string1="Hello"
string2=input("Please enter your name")
result =string1 + string2
print(result)

string3= ",Welcome to Python programming"
result=result+string3
print(result)

# 2. Slicing and Indexing 

print("a.", result[0])            # first character
print("b.", result[-1])           # last character
print("c.", result[:5])           # first 5 characters
print("d.", result[-11:])         # last 11 characters
print("e.", result[::-1])         # reversed string
start = result.find("Python")
print("f.", result[start:start + 6])  # the word "Python"

# 3. String Methods 

strM = "Python beginner tutorial"
print("a.", strM.upper())
print("b.", strM.lower())
print("c.", strM.lower().capitalize())   # get back to original form
print("d.", strM.count("t"))
print("e.", strM.replace("Python", "Machine Learning"))

# 4. Tuples 
t1 = (10, 20, 30)
t2 = (40, 50, 60)

t_combine = t1 + t2
print("a.", t_combine)
print("b.", t_combine * 3)
print("c.", t_combine[2])       # 3rd element
print("d.", t_combine[:3])      # first three
print("e.", t_combine[-3:])     # last three
