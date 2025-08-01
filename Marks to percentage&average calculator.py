print("Marks Percentage Calculator")

subjects = int(input("Enter number of subjects: "))
max_marks = float(input("Enter maximum marks for each subject (like 100, 120, 200): "))

marks = []
for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    if mark > max_marks:
        print("Entered marks cannot be more than maximum marks!")
        exit()
    marks.append(mark)

total = sum(marks)
average = total / subjects
percentage = (total / (subjects * max_marks)) * 100

print("\n--- Result ---")
print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", round(percentage, 2), "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")
