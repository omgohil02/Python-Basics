#if elif and else statements in Python

#Python uses structural logic blocks to make code execute only when specific conditions are met. Indentation (4 spaces) is strictly mandatory to define these code blocks.

score = int(input("Enter your score: "))  #EX:input: 85

if score >= 90:
    print("Grade: A")  #EX:output: Grade: A

elif score >= 80:
    print("Grade: B")  #EX:output: Grade: B
    
else:
    print("Grade: C")  #EX:output: Grade: C
