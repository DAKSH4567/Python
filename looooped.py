# Count total digits in a number using while loop

num = int(input("Enter a number: "))
count = 0

# Handle the case if number is 0
if num == 0:
    count = 1
else:
    # Make sure to work with positive numbers
    if num < 0:
        num = -num

    while num > 0:
        num = num // 10
        count += 1

print("Total digits:", count)

