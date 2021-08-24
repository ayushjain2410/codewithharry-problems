# code with harry probems and solutions



"""
# age predictor -----------------------------------------------------------------------
Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year
of birth and tell the user when they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

Do not use any type of modules like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
Your code should handle all sort of errors like:                       (2 points)
You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible
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
# divide the apple------------------------------------------------------------------------------------------------------
Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples 
is provided to harry by his friends, and he can request for few more or few less apples.
You need to print whether a number is in range mn to mx, is a divisor of “n” or not.

Input:
Take input n, mn, and mx from the user.
Output:
Print whether the numbers between mn and mx are divisor of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx.
Show the result for that number.
Example:
If n is 20 and mn=2 and mx=5
2 is a divisor of20
3 is not a divisor of 20
..
5 is a divisor of 20


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
------------------------------------------------------------------------------------------------------------------------
You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. 
You have to reserve this list of food items containing calories.
You have to use the following three methods to reserve a list:
Inbuild method of python
List name [::-1] slicing trick
Swap the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]
Input:
Take a list as an input from the user
[5, 4, 1]
Output:
[1, 4, 5]
[1, 4, 5]
[1, 4, 5]
All three methods give the same results!

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
----------------------------------------------------------------------------------------------------------------------
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
676, 616, mom, 100001.
You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number.
 Your first input should be the number of test cases and then take all the cases as input from the user.
Input:
3
451
10
2133
Output:
Next palindrome for 451 is 454
Next palindrome for 10 is 11
Next palindrome for 2311 is 2222

You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is greater than 10;
 otherwise, you will print that number.
Input:
[1, 6, 87, 43]
Output:
[1, 6, 88, 44]


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
------------------------------------------------------------------------------------------------------------------------
You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is greater than 10;
 otherwise, you will print that number.
Input:
[1, 6, 87, 43]
Output:
[1, 6, 88, 44]

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
------------------------------------------------------------------------------------------------------------------------
Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b. a and b 
are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number and 
your program must tell whether the number is greater than the actual number or less than the actual number. Log the 
number of trials it took your friend to arrive at the number. You play the same game and then the person with minimum
 number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.
Input:
Enter the value of a
4
Enter the value of b
13
Output:
Player1 :
Please guess the number between 4 and 13
5
Wrong guess a greater number again
8
Wrong guess a smaller number again
6
Correct you took 3 trials to guess the number
Player 2:
Correct you took 7 trials to guess the number
Player 1 wins!

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
-----------------------------------------------------------------------------------------------------------------------
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user.
You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after
converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum 
number of matching words with the query.
Sentences = [“Python is cool”, “python is good”, “python is not python snake”]
Input:
Please input your query string
“Python is”
Output:
3 results found:
python is not python snake
python is good
Python is cool

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
------------------------------------------------------------------------------------------------------------------------
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user.
You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after
converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum 
number of matching words with the query.
Sentences = [“Python is cool”, “python is good”, “python is not python snake”]
Input:
Please input your query string
“Python is”
Output:
3 results found:
python is not python snake
python is good
Python is cool


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
-----------------------------------------------------------------------------------------------------------------------
 Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a given number and put 
 one of the values (randomly generated) as wrong.Rohan Das did this to fool his classmates and make them commit a mistake in a test. 
 You cannot tolerate this!So you decided to use your python skills to counter Rohan’s actions by writing a python program that 
 validates Rohan’s multiplication table.Your function should be able to find out the wrong values in Rohan’s table and expose 
 Rohan Das as a fraud. Note: Rohan’s function returns a list of numbers like this
Rohan Das’s Function Input:
rohanMultiplication(6)
Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]
You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None

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
------------------------------------------------------------------------------------------------------------------------
it's result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names to come up with some funny names.
Your program should take the number of names and the names separated by space as input. Output should be funny names in the same order.
Input:
Enter number of friends:
3
Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora
Output:
Ritesh Das
Shubham Arora
Rohan Agarwal


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

