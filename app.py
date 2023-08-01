#Maximum no. of input should be 40
#Shold display average marks at the end
#Display highest mark in the end

total_marks = 0
no_inputs = 0
max_mark = 0
for i in range(0, 40):
    user_marks = input("Enter marks : ")
    marks = float(user_marks)
    if marks < 0 or marks > 100:
        print("Invalid marks")
        continue

    total_marks += marks
    no_inputs += 1
    max_mark = max(max_mark, marks)
    if marks < 40:
        print("Grade : F")
        print("Description: Failure")
    elif marks < 55:
        print("Grade : D")
        print("Description: Odinary pass")

    elif marks < 65:
        print("Grade : C")
        print("Description: Credit pass")

    elif marks < 75:
        print("Grade : B")
        print("Description: Very GOOD Pass")

    else:
        print("Grade : A")
        print("Description: Excellent pass")

    answer = input("May I continue? (Y/N): ")
    if answer == "N":
        break

print("")
print(" END RESULT  ")
print("")
Average = total_marks / no_inputs
print("Average of all students : " + str(Average))
print("Maximum mark is : " + str(max_mark))
print("Thank you.")




