"""
# age predictor
from datetime import date

def hundred(var):

    if var > 150:
        year = var
        year_hundred = year+100
        print(year_hundred)
        age_input = int(input("enter the year in which you would like to know your age :"))
        future_age = age_input-year
        print(future_age)

    else:
        age = var
        year_hundred = date.today().year - age + 99
        print(year_hundred)
        age_input = int(input("enter the year in which you would like to know your age :"))
        future_age = age_input - date.today().year + age +1
        print(future_age)

variable = int(input("enter your birth year/age : "))
hundred(variable)
"""
"""
# divide the apple
try:
  apples = int(input("enter the number of apples : "))
  minimum = int(input("enter minimum number of students : "))
  maximum = int(input("enter maximum number of students : "))
except ValueError:
    print("enter integers only")
    exit()

if minimum == maximum:
        if apples % minimum == 0:
            print(f"{minimum} is a divisor of {apples}")
        else:
            print(f"{minimum} is not a divisor of {apples}")
else:
    for i in range(minimum,maximum+1):
        if apples % i == 0:
            print(f"{i} is a divisor of {apples}")
        else:
            print(f"{i} is not a divisor of {apples}")
"""

"""
def method1(list1):
    list2 = list1[:]
    list2.reverse()
    print(list2)


def method2(list1):
    list2=list1[:]
    print(list2[::-1])


def method3(list2):
    list1=list2[:]
    for i in range(len(list1) // 2):
        var1 = list1[i]
        list1[i] = list1[len(list1) - i - 1]
        list1[len(list1) - i - 1] = var1
    print(list1)


lista = eval(input("enter the values : "))
method1(lista)
method2(lista)
method3(lista)
print(lista)
"""
"""
test_cases=int(input("enter number of test cases you want to analyze : "))
for i in range (test_cases):
    str1=input("enter the string : ")
    if str1 == str1[::-1]:
        print("string is already a palindrome")
    else :
        num1=int(str1)
        while True:
            if str(num1) == str(num1)[::-1]:
                print(f"{num1} is next pallindrome")
                break
            else:
                num1+=1
"""
"""
mylist = []
len1 = int(input("enter the number of items you want in list : "))
for i in range(len1):
    item = int(input("enter the list item :"))
    mylist.append(item)

print(f"the list is {mylist}")
for i in range(len1):
    if mylist[i] >= 10:
        num = mylist[i]
        while True:
            if str(mylist[i]) == str(mylist[i])[::-1]:
                break
            else:
                mylist[i] = mylist[i] + 1
print(f"the list is {mylist}")
"""
"""
import random


def structure():
    count = 0
    var = int(input(f"enter your number between {a} and {b}"))
    while var != number:
        if var < number:
            print(f"correct number is greater than {var}")
            count += 1

        elif var > number:
            print(f"correct number is smaller than {var}")
            count += 1
        var = int(input(f"enter your number between {a} and {b}"))


    count += 1
    print(f"correct answer. you guessed in {count} trials . ")
    return count


a = int(input("enter the lower limit : "))
b = int(input("enter the upper limit : "))

number = random.randint(a, b)
print("player 1 turn ")
chances1 = structure()
number = random.randint(a, b)
print("player 2 turn ")
chances2 = structure()

if chances1 == chances2:
    print("both guessed in same number of trials ")
elif chances2 > chances1:
    print(f"player 1 won with {chances1} chances ")
else:
    print(f"player 2 won with {chances2} chances ")
"""

"""
import collections

list1 = ["is is is is is ", "this is good", "python is good", "python is not python", "hello is world",
         "python is worst", "not python",
         "hello world python", "ayush jain", "srishti lalita", "pythonda lepa"]

query = input("enter your query")
list2 = query.split()
dict1 = {}

for j in list1:
    count = 0
    list3 = []
    var1 = j.split()
    for i in list2:
        for z in var1:
            if i == z:
                count += 1
    if count == 0:
        continue;
    else:
        list3.append(j)
        if count in dict1.keys():
            dict1[count].extend(list3)
        else:
            dict1[count] = list3

dict2 = collections.OrderedDict(sorted(dict1.items()))

list4 = []
for i in dict2:
    for j in dict2[i]:
        list4.append(j)

list4.reverse()
for i in range(len(list4)):
    print(f"{i + 1}. {list4[i]}")
"""

"""
def match(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    sentences = ["is is is is is", "this is good", "python is good", "python is not python", "hello is world",
                  "python is worst", "not python", "hello world python", "ayush jain", "srishti lalita", "pythonda lepa"]

    query = input("enter your query : ")
    scores = [match(query, sentence) for sentence in sentences]
    sortedsentscore = [sentscore for sentscore in sorted(zip(scores, sentences), reverse=True)]

    print(f"{len(sortedsentscore)} results found")
    for score, item in sortedsentscore:
        print(f"\"{item} \":with a score of {score}")
"""

"""
import random


def rohan(number):
    list1 = []
    num1 = random.randint(1, 10)
    for i in range(1, 11):
        if i != num1:
            print(f"{number} * {i} = ", number * i)
            list1.append(number * i)
        else:
            value = random.randint(((number * num1) - 4), ((number * num1) + 4))
            print(f"{number} * {i} = ", value)
            list1.append(value)
    return list1


def correct(list1, number):
    for i in range(1, 11):
        if (number * i) != list1[i - 1]:
            print(f"wrong answer by rohan")
            return i - 1
    return None


if __name__ == '__main__':
    num = int(input("enetr your number : "))
    print("rohan program output is :")
    rohan_output = rohan(num)
    print(rohan_output)
    print("my output is :")
    my_output = correct(rohan_output, num)
    if my_output != None:
        print(f"rohan's answer was wrong at position {my_output}")
        print(f"correct answer should be {num * (my_output + 1)}")
    else:
        print("roahns and my output in this case are same ")

"""

"""
import random

friend_first=[]
friend_last=[]
number_of_friends=int(input("enetr number of freinds : "))
for i in range(number_of_friends):
    fname=input("enetr your freind name :")
    name_list=fname.split(" ")
    friend_first.append(name_list[0])
    friend_last.append(name_list[1])
print(friend_first)
print(friend_last)

for i in friend_first:
    lastname=random.choice(friend_last)
    friend_last.remove(lastname)
    print(f"{i} {lastname}")
"""

x = 0
list1 = []
str1="helo ayush oh warum ooy python"
z=len(str1)

while x<z:
    str2=" "
    for i in range (x,len(str1)):
        x+=1
        if str1[i] !='o':
            str2+=str1[i]

        else:
            break
    print(len(str2))
    if len(str1)!=1:
        list1.append(str2)
print(list1)
