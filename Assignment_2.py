# ASSIGNMENT 2 

# Lists

# 1. Creation

age_list = [24, 25, 26, 27, 28]
name_list = ["Arun", "Bala", "Charan", "Divya", "Esha"]

# 2. Operations
name_list.append("Yazhini")            # a
age_list.insert(2, 30)                 # b -> [24, 25, 30, 26, 27, 28]
name_list.remove("Yazhini")            # c
age_list.pop()                         # d (remove 28)
age_list.extend([29, 30, 26])          # e
age_list.sort(reverse=True)            # f
print("Sorted ages:", age_list)
print("Max:", max(age_list))           # g
print("Min:", min(age_list))
print("Sum:", sum(age_list))

# 3. Accessing
print(name_list[0])                    # a. first
print(name_list[-1])                   # b. last
print(name_list[2:5])                  # c. index 2 to 4
print(name_list[::-1])                 # d. reverse


# Dictionary 

student_marks = {"Ravi": 78, "Meena": 91, "Karthik": 65, "Priya": 88, "Sanjay": 72}  # a
print(student_marks["Meena"])          # b
student_marks["Janani"] = 80           # c
student_marks["Ravi"] = 82             # d
print(student_marks.keys())            # e
print(student_marks.values())
print(student_marks.items())


# Sets 

# a. Duplicates are removed; sets are unordered, so order may vary
my_set = set(['a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'])
print(my_set)   # e.g. {'u', 'a', 'i', 'e', 'o'}

# b. Sets don't support indexing/item assignment
try:
    my_set[4] = 's'
except TypeError as e:
    print("Error:", e)   # 'set' object does not support item assignment

# c, d
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}
print("Union:", set1 | set2)           # or set1.union(set2)
print("Intersection:", set1 & set2)    # or set1.intersection(set2)


# ---------- Performance Category ----------

score = float(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a value between 0 and 10.")
elif score > 7:
    print("Above Average: Excellent work! Keep up the great performance.")
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve your performance, consistent practice will lead to better results.")