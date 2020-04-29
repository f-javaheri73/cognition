"""
#045
total = 0
while total <= 50:
    num = int(input("enter a number: "))
    total = total + num
print(total)
"""
"""
#046
num = 0
while num < 5:
    num = int(input("Enter a number: "))
print("the latest number you entered was" , num)
"""
"""
#047
num = int(input("Enter a number: "))
total = num
answer = 'y'
while answer == 'y':
    num2 = int(input("Enter another one: "))
    total = total + num2
    answer = input("do you want add another? ")
print(total)
"""
"""
#048
count = 0
answer = 'yes'
while answer == 'yes':
    name = input("enter a name that you want to invite: ")
    print(name,"has now been invited")
    count = count + 1
    answer = input("want to invite sombody else: ")
print(count)
"""
"""
#049
compnum = 50
count = 0
guess = 0
while guess != compnum:
    guess = int(input("Enter a Guess: "))
    if guess < compnum:
        print("too low")
    elif guess > compnum:
        print("too high")
    count = count + 1
print("well done, you took",count,"attempts")
"""
"""
#050
num = int(input(" enter a number between 10 and 20: "))
while num<10 or num >20:
    if num<10:
        print("too low")
    elif num>20:
        print("too high")
    num = int(input("try again: "))
print("thank you")
"""
"""
#051
num = 10
while num>0:
    print("there are",num,"green bottles hanging on the wall,\n",
    num,"green bottle hanging on the wall,\n"
      "if 1 green bottle should accidentally fall\n",)
    num = num-1
    answer = int(input("how many green bottles will be hanging on the wall? "))
    if answer == num:
        print("there will be",num,"green bottles on the wall")
    else:
        while answer!= num:
            answer = int(input("no, try again: "))
print("there are no more green bottles hanging on the wall.")
"""

    

