# LESSON 4 STARTER CODE: VARIABLES AND DATA TYPES

# ========================================
# PART 1: Creating Variables Practice
# ========================================
name = "Swijish"
age = 100
gpa = 3.999
grade = 100001


print("Student name: " + name)
print("Student age: ",age)

# vairables can change
age = 17
 # multiple assignments
subject, period = "CS100", 1

# ========================================
# PART 2: Data Types Practice
# ========================================
# Four main(primitive) data types
name = "Swijish" #String(str)
age = 100  #integer(int)
gpa = 3.999 #float(decimal)
is_present = True #bool(Boolean)

#Check Data types via type() fuction
print(f"Name:{name} Type: {type(name)}")
print(f"Age:{age} Type: {type(age)}")
print(f"GPA:{gpa} Type: {type(gpa)}")
print(f"Present:{is_present} Type: {type(is_present)}")



# ========================================
# PART 3: Type Conversion Practice
# ========================================

#convert between types
grade_text ="95"
# grade_text2 ='"95"'
print(f"Original:{grade_text} {type(grade_text)}")
grade_number = int(grade_text)
print(f"As Number:{grade_number} {type(grade_number)}")
gpa_number = float(gpa)
print(f"GPA: {gpa_number} {type(gpa_number)}")
gpa_text = str(gpa_number)


# practice with bool() function
print(f"bool(0) - {bool(0)}") # false
print(f"bool(0) - {bool(1)}") # true
print(f"bool(0) - {bool(10)}") # true
print(f"bool('hi') - {bool('hi')}") # true
print(f"bool(' ') - {bool(' ')}") # true


# ========================================
# PART 4: Variable Operations Practice  
# ========================================

#Swapping variables
color1 = "blue"
color2 = "red"
color1, color2, = color2, color1

print(f"Color2: {color2}")
