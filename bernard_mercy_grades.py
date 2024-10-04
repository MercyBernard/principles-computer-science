grades = [83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]

attendance_day1 = {"Mary", "Jake", "Sam", "Alex", "Percy", "Jessica", "Trent", "Mahmoud"}

attendance_day2 = {"Jake", "Sam", "Alex", "Percy", "Mahmoud", "Trent", "Caleb", "Zayne"}

num_student_exam = len(grades)
highest_grade = max(grades)
lowest_grade = min(grades)
average_grade = sum(grades) / num_student_exam

print(f"{num_student_exam} Students took the exam.")
print(f"The highest grade was a {highest_grade}")
print(f"The lowest grade was a {lowest_grade}")
print(f"The average grade for the exam was a {average_grade:.1f}")

print()

num_student_class = len(attendance_day1.union(attendance_day2))
attended_both_days = attendance_day1.intersection(attendance_day2)
attended_one_day = attendance_day1.symmetric_difference(attendance_day2)

print(f"{num_student_class} students attended the class.")
print(f"{attended_both_days} attended both class days.")
print(f"{attended_one_day} attended one class day.")