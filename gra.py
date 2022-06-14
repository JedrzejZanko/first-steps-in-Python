import string

preparation = ["Ready", "Steady", "And", "GOOOO!"]
for cuntdown in preparation:
    print(cuntdown)

from gra_odpowiedzi import odpowiedzi

odpowiedzi1 = odpowiedzi("Banfi", "Anka", "Aleksander", "kupa", "Paweł", "Borys")


Cheer1 = "Don't give up!"
Cheer2 = "Try one more time :)"
score = 0
secret_word = (odpowiedzi1.odp1)
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Pyt 1. Czarny świrus to: ")
        guess_count += 1
    if guess_count == 1 and (guess != secret_word):
        space = Cheer1.rjust(len(Cheer1)+7)
        print(space)
    elif guess_count == 2 and (guess != secret_word):
        space = Cheer2.rjust(len(Cheer2)+7)
        print(space)

    else:
        out_of_guesses = True
if guess == secret_word:
        print("wygranko w zgadywanko")
        score += 1
        print("Awesome! Your score is: ", (score))
else:
    print("Przegranko!")
    print("Your score is: ", (score))

print()
score1 = 0
secret_word1 = (odpowiedzi1.odp2)
guess1 = ""
guess_count1 = 0
guess_limit1 = 3
out_of_guesses1 = False
while guess1 != secret_word1 and not(out_of_guesses1):
    if guess_count1 < guess_limit1:
        guess1 = input("Pyt 2. Ma szmergla na punkcie kwiatów: ")
        guess_count1 += 1
    if guess_count1 == 1 and (guess1 != secret_word1):
        space = Cheer1.rjust(len(Cheer1)+7)
        print(space)
    elif guess_count1 == 2 and (guess1 != secret_word1):
        space = Cheer2.rjust(len(Cheer2)+7)
        print(space)
    else:
        out_of_guesses1 = True
if guess1 == secret_word1:
    print("wygranko w zgadywanko")
    score1 += 1
    print("Awesome! Your score is: ", (score1 + (score)))
else:
    print("Przegranko!")
    print("Your score is: ", (score1 + (score)))

print()
score2 = 0
secret_word2 = (odpowiedzi1.odp3)
guess2 = ""
guess_count2 = 0
guess_limit2 = 3
out_of_guesses2 = False
while guess2 != secret_word2 and not(out_of_guesses2):
    if guess_count2 < guess_limit2:
        guess2 = input("Pyt 3. Potezny alkoholik: ")
        guess_count2 += 1
    if guess_count2 == 1 and (guess2 != secret_word2):
        space = Cheer1.rjust(len(Cheer1) + 7)
        print(space)
    elif guess_count2 == 2 and (guess2 != secret_word2):
        space = Cheer2.rjust(len(Cheer2) + 7)
        print(space)
    else:
        out_of_guesses2 = True
if guess2 == secret_word2:
    print("wygranko w zgadywanko")
    score2 += 1
    print("Awesome! Your score is: ", (score2 + (score1) +(score)))
else:
    print("Przegranko!")
    print("Your score is: ", (score2 + (score1) + (score)))

print()
score3 = 0
secret_word3 = (odpowiedzi1.odp4)
guess3 = ""
guess_count3 = 0
guess_limit3 = 3
out_of_guesses3 = False
while guess3 != secret_word3 and not(out_of_guesses3):
    if guess_count3 < guess_limit3:
        guess3 = input("Pyt 4. Banfi robi 5 dziennie: ")
        guess_count3 += 1
    if guess_count3 == 1 and (guess3 != secret_word3):
        space = Cheer1.rjust(len(Cheer1) + 7)
        print(space)
    elif guess_count3 == 2 and (guess3 != secret_word3):
        space = Cheer2.rjust(len(Cheer2) + 7)
        print(space)
    else:
        out_of_guesses3 = True
if guess3 == secret_word3:
    print("wygranko w zgadywanko")
    score3 += 1
    print("Awesome! Your score is: ", (score3 + (score2) + (score1) + (score)))
else:
    print("Przegranko!")
    print("Your score is: ", (score3 + (score2) + (score1) + (score)))

print()
score4 = 0
secret_word4 = (odpowiedzi1.odp5)
guess4 = ""
guess_count4 = 0
guess_limit4 = 3
out_of_guesses4 = False
while guess4 != secret_word4 and not(out_of_guesses4):
    if guess_count4 < guess_limit4:
        guess4 = input("Pyt 5. Lubi cośtam z czymśtam: ")
        guess_count4 += 1
    if guess_count4 == 1 and (guess4 != secret_word4):
        space = Cheer1.rjust(len(Cheer1) + 7)
        print(space)
    elif guess_count4 == 2 and (guess4 != secret_word4):
        space = Cheer2.rjust(len(Cheer2) + 7)
        print(space)
    else:
        out_of_guesses4 = True

if guess4 == secret_word4:
    print("wygranko w zgadywanko")
    score4 += 1
    print("Awesome! Your score is: ", (score4 + (score3) + (score2) + (score1) + (score)))
else:
    print("Przegranko!")
    print("Your score is: ", (score4 + (score3) + (score2) + (score1) + (score)))

print()
score5 = 0
secret_word5 = (odpowiedzi1.odp6)
guess5 = ""
guess_count5 = 0
guess_limit5 = 3
out_of_guesses5 = False
while guess5 != secret_word5 and not(out_of_guesses5):
    if guess_count5 < guess_limit5:
        guess5 = input("Pyt 6. Najmłodszy w rodzinie fan Pana Kleksa to: ")
        guess_count5 += 1
    if guess_count5 == 1 and (guess5 != secret_word5):
        space = Cheer1.rjust(len(Cheer1) + 7)
        print(space)
    elif guess_count5 == 2 and (guess5 != secret_word5):
        space = Cheer2.rjust(len(Cheer2) + 7)
        print(space)
    else:
        out_of_guesses5 = True

if guess5 == secret_word5:
    print("wygranko w zgadywanko")
    score5 += 1
    print("Awesome! Your score is: ", (score5 + (score4) + (score3) + (score2) + (score1) + (score)))
else:
    print("Przegranko!")
    print("Your score is: ", (score5 + (score4) + (score3) + (score2) + (score1) + (score)))
print()

import random
zgoda = "tak"
niezgoda = "nie"
if (score5 + (score4) + (score3) + (score2) + (score1) + (score)) >= 5:
    odpowiedz = input("Czy chcesz spróbować wylosować bonusowy mnoznik od x0 do x5: ")
    if odpowiedz == zgoda:
        print("Twój wynik po wylosowaniu mnożnika to: ")
        def roll_dice(num):
            return random.randint(0, num)
        print(roll_dice(5) * (score5 + (score4) + (score3) + (score2) + (score1) + (score)))
    elif odpowiedz == niezgoda:
        print("Wiec kończysz grę z wynikiem: ", (score5 + (score4) + (score3) + (score2) + (score1) + (score)))


    # dokończyć napisać równanie mnożnik razy wynik i zeby to sie wyswietlało


