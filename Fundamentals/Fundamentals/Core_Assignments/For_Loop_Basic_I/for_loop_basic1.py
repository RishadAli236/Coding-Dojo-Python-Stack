# Basic - Print all integers from 0 to 150

for integer in range(151):
    print(integer)

# Multiples of 5 - Print all multiples of 5 from 5 to 1000

for multiple_of_5 in range(5,1001,5):
    print(multiple_of_5)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for integer in range(1,101):
    if integer % 10 == 0:
        print("Coding Dojo")
    elif integer % 5 == 0:
        print("Coding")
    else:
        print(integer)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for odd_integer in range(1,500000,2):
    sum += odd_integer
print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for numbers in range(2018,0,-4):
    print(numbers)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

low_num = 2
high_num = 9
mult = 3
for integer in range(low_num,high_num+1):
    if integer % mult == 0:
        print(integer)
