### print words in a string that starts witg "s"

string = "This is sad world with super and savage people who are interested in sassy things"
newstr = string.split()
for letter in newstr:
  if letter[0] == "s":
    print(letter)
	
	
## alternative method

string = "This is sad world with super and savage people who are interested in sassy things"

for letter in string.split(): ## using split directly with string
  if letter[0] == "s":
    print(letter)
	
## if upper case "S" ?

string = "This is sad world with super and Savage people who are interested in sassy things"

for letter in string.split(): ## using split directly with string
  if letter[0].lower() == "s":
    print(letter)
	
## find even number using range()#

for num in range(0,11): ## though this is not recommend while using range() # see below another example##
  if num%2==0:
    print(num)
	
## alternate correct method with range 

for num in range(0,11,2):
    print(num)

	
## use list comprehension to create list btwn 1 to 51 that are divisible by 3

mylist = [num for num in range(1,51) if num%3==0]
print(mylist)

## print the word "even!" for each word which has even length

st = "Print every word in this sentence that has an even number of letters"

for word in st.split():
  if len(word)%2 == 0:
    print("Even!")
  else:
    print(word)
	
## write program that prints the integer from 1 to 100. but for mul of three print "fizz", mul of five print"buzz" and mul of both print "FizzBuzz"

for num in range(1,101):
  if num%15==0:
    print("FizzBuzz")
  elif num%5==0:
    print("Buzz")
  elif num%3==0:
    print("Fizz")
  else:
    print(num)
	
## alternative

for num in range(1,101):
  if num%5==0 and num%3==0:  ## here using "and" operator 
    print("FizzBuzz")
  elif num%5==0:
    print("Buzz")
  elif num%3==0:
    print("Fizz")
  else:
    print(num)