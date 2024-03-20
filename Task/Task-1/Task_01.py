# Problem-1
x = input("First number: ")
y = input("\nSecond number: ")

z = float(x) + float(y)

print("The sum of {0} and {1} is {2}" .format(x, y, z))
#-------------------------------------------------------#

# Problem-2
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
#-------------------------------------------------------#

# Problem-3
import sys
print(sys.modules)
#-------------------------------------------------------#

# Problem-4
print('Hello', end='')
print('World')
#-------------------------------------------------------#

# Problem-5
x = int(input("Enter a number: "))
if x % 2 ==0:
    print("This is an even number.")
else:
    print("This is an odd number.")
#-------------------------------------------------------#

# Problem-6
X = int( input("enter value for X: "))  
Y = int( input("enter value for Y: "))  

temp = X  
X = Y
Y = temp
   
print ("The Value of X after swapping: ", X)  
print ("The Value of Y after swapping: ", Y) 
#-------------------------------------------------------#

# Problem-7
A = [2, 1, 4, 5, 6, 3]

for num in A:
    
	if num % 2 == 0:
		print(num, end=" ")
#-------------------------------------------------------#

# Problem-8
A = input("Input a letter of the alphabet: ")

if A in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % A)
else:
	print("%s is a consonant." % A) 
#-------------------------------------------------------#

# Problem-9
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
#-------------------------------------------------------#

# Problem-10
s = "The quick brown fox jumps over the lazy dog."  
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
print(s.count("o"))
#-------------------------------------------------------#

# Problem-11
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the said list: ",new_nums)
#-------------------------------------------------------#

# Problem-12
def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
#-------------------------------------------------------#

# Problem-13
A = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0

for num in A:

	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
#-------------------------------------------------------#

# Problem-16
numbers = [45, 12, 67, 89, 34, 23, 1, 78, 56]
largest_number = max(numbers)
smallest_number = min(numbers)

print("Largest number in the list:", largest_number)
print("Smallest number in the list:", smallest_number)
#-------------------------------------------------------#

# Problem-17
#-------------------------------------------------------#
