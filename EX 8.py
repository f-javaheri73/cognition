"""
#069
countries = ('usa','uk','iran', 'lebanon','austria')
print(countries)
choice = input('enter one of the countries: ')
print(countries.index(choice))
"""
"""
#070
countries = ('usa','uk','iran', 'lebanon','austria')
print(countries)
choice = input('enter on of the countries: ')
print(countries.index(choice))
choice2 = int(input("hal shomareye yek keshvar ra vared konid: "))
print(countries[choice2])
"""
"""
#071
sports = ['footbal','boxing']
print(sports)
fav = input('what is your favorite sport? ')
sports.append(fav)
sports.sort()
print(sports)
"""
"""
#072
sub = ['chemistry','math','physics','philosophy','biology', 'psychology']
print(sub)
dislike = input("what of these subs you don't like? ")
sub.remove(dislike)
print(sub)
"""
"""
#073
d = {}
foods1 = input("enter a food:: ")
d[1] = foods1
foods2 = input("enter a food:: ")
d[2] = foods2
foods3 = input("enter a food:: ")
d[3] = foods3
foods4 = input("enter a food:: ")
d[4] = foods4
print(d)
getrid = int(input("which one do you want get rid of? "))
del d[getrid]
print(sorted(d.values()))
"""
"""
#074
colors = ['red','yellow','blue','purple','black','white', 'grey','pink','orange','green']
print(colors)
start = int(input("enter a number between 0,4: "))
end = int(input("enter a number between5,9: "))
print(colors[start:end])
"""
"""
#075
nums = [364,345,243,798]
print(*nums,sep = '\n')
enter = int(input("enter a three-digit number: "))
if enter in nums:
    print(nums.index(enter))
else:
    print("That is not in the list")
"""
"""
#076
d = []
for i in range(1,4):
    names = input("name 3 people ypu wnat to invite: ")
    d.append(names)
answer = input("do you want invite another person? ")
while answer == 'yes':
    add = input("enter name: ")
    d.append(add)
    answer = input("do you want invite another person? ")
print(d)
"""
"""
#076-2
d = []
count = 0
for i in range(1,4):
    names = input("name 3 people ypu wnat to invite: ")
    d.append(names)
    count = count + 1
answer = input("do you want invite another person? ")
while answer == 'yes':
    add = input("enter name: ")
    d.append(add)
    count = count + 1
    answer = input("do you want invite another person? ")

print("you invited",count,"guests.")
"""
"""
#076-3
name1 = input("enter a name you want invite: ")
name2 = input("enter anothr name: ")
name3 = input("enter a third person: ")
party = [name1,name2,name3]
another = input("do you want another person? y/n : ")
while another == 'y':
    newname = party.append(input("enter another name: "))
    another = input("do you want another person? y/n : ")
print("you have", len(party),"people coming to your party")
"""
"""
#077
name1 = input("enter a name you want invite: ")
name2 = input("enter anothr name: ")
name3 = input("enter a third person: ")
party = [name1,name2,name3]
another = input("do you want another person? y/n : ")
while another == 'y':
    newname = party.append(input("enter another name: "))
    another = input("do you want another person? y/n : ")
print(party)
typein = input("enter a name in the list: ")
print(party.index(typein))
q = input("do you still want him to come? ")
if q == 'no':
    party.remove(typein)
print(party)
"""
"""
#078
tvshow = ['footbal','seral','sinamai','akhbar']
print(*tvshow, sep = "\n")
anothershow = input("add another show: ")
position = int(input("whre do you want it? "))
tvshow.insert(position,anothershow)
print(*tvshow, sep = "\n")
"""
"""
#079
nums = []
for i in range(1,3):
    numbers = nums.append(int(input("add numbers: ")))
    print(nums)
numbers1 = int(input("add numbers: "))
nums.append(numbers1)
print(nums)
question = input ("do you want your last number? ")
if question == 'no':
    nums.remove(numbers1)
    print(nums)
else:
    print(nums)
"""
"""
#079-2
nums = []
count = 0
while count < 3:
    num = int(input("add numbers: "))
    nums.append(num)
    print(nums)
    count = count + 1
lastnum = input("Do you still want the last number? ")
if lastnum == 'n':
    nums.remove(num)
print(nums)
"""
