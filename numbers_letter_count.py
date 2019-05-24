'''
Number letter count: If the numbers 1 to 5 are written in words: one, two, three, four, five
then, there are 3+3+5+4+4 = 19 letters used in total.

If all the numbers from 1 to 1000 were written in words, how many letters would be used?

For example, 342 (three hundred and forty-two) contains 23 letters, 115 (one hundred and fifteen)
contains 20 letters.

NOTE: Do not count spaces or hyphens

The only input to the function is n, a +ve integer smaller than 1000.

The use of 'and when writing out numbers is in compliance with British usage.

Author: Himangshu Pal
Date: 05/20/2019
'''

def numb_to_word(n):

    one_to_nine = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5:"five", 6: "six", 7: "seven", 8:"eight", 9:"nine"}
    eleven_to_nineteen = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'forteen', 15:"fifteen", 16: "sixteen", 17: "seventeen", 18:"eighteen", 19:"nineteen"}
    tens = {10: "ten", 20: "twinty", 30: "thirty", 40: "forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
    hundred = 'hundred'

    list1 = []
    word = ''
    count = 0
    x = n // 100
    y = n % 100
    list1.append(x)
    x = y // 10
    y = y % 10
    list1.append(x)
    list1.append(y)
    #print(list1)

    if list1[0] > 0:
        word += (one_to_nine[list1[0]]) + ' ' + hundred
     #   print(word)
        if list1[1] == 0 and list1[2] > 0:
            word += ' and ' + (one_to_nine[list1[2]])

    if list1[1] > 0:
        if list1[0] > 0:
            word += ' and '
        if list1[2] == 0:
            z = list1[1] * 10
      #      print(tens[z])
            word += tens[z]

        elif list1[1] == 1 and list1[2] > 0:
            z = list1[1] * 10 + list1[2]
       #     print(eleven_to_nineteen[z])
            word += eleven_to_nineteen[z]
        else:
            # print("here")
            z = list1[1] * 10
        #    print(tens[z])
            word += tens[z]
            z = list1[2]
         #   print(one_to_nine[z])
            word += " " + one_to_nine[z]

    if list1[0] == 0 and list1[1] == 0 and list1[2] > 0:
        z = list1[2]
        word += one_to_nine[z]

    for char in word:
        if char == " ":
            continue
        else:
            count += 1

    print(f"{word} : {count}")
    return count



def main():
    total = 0
    while True:
        user_input = input("Please enter an integer(not more than 999): ")
        try:
            user_input = int(user_input)
            if user_input >= 1000:
                print(f"You entered {user_input}, please re-enter within limit.")

            if user_input < 1000 and user_input > 0:

                for i in (range(1, user_input + 1)):
                    total += numb_to_word(i)
                print("The total is: ", total)
                break
        except:
            print("Error! Only integer is acceptable. ")


main()