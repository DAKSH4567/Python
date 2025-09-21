# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths : "))
english = int(input("english : "))
science = int(input("science : "))
hindi = int(input("hindi : "))

# Let's calculate the percentage of marks
total = math + english + science + hindi
print("Sum of math, english, science and hindi =", total)

perc = (total / 400) * 100

print("Percentage Mark =", perc)
