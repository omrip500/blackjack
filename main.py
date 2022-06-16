import random
import art
import methods

want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

while want_to_play == 'y':
    print(art.logo)
    my_pack = methods.new_pack()
    computer_pack = methods.new_pack()
    print(f"Your cards: {my_pack}, current score: {sum(my_pack)}")
    print(f"computer's first card: {computer_pack[0]}")
    keep_playing = input("Type 'y' to get another card, type 'n' to pass: ")
    while keep_playing == 'y':
        computer_pack = methods.computer_choice(computer_pack)
        random_number = random.randint(2, 11)
        my_pack.append(random_number)
        if sum(my_pack) > 21:
            keep_playing = 'n'
        else:
            print(f"Your cards: {my_pack}, cuurent score {sum(my_pack)} \n computer's first card:{computer_pack[0]}")
            keep_playing = input("Type 'y' to get another card, type 'n' to pass: ")

    print(f"Your final hand: {my_pack}, final score: {sum(my_pack)} \n Computer's final hand: {computer_pack}, final score: {sum(computer_pack)}")

    my_diffrernce_from_21 = abs(21 - sum(my_pack))
    computer_diffrernce_from_21 = abs(21 - sum(computer_pack))

    if sum(my_pack) > 21:
        if sum(computer_pack) > 21:
            if my_diffrernce_from_21 < computer_diffrernce_from_21:
                print("You win")
            elif my_diffrernce_from_21 > computer_diffrernce_from_21:
                print("You went over. You lose")
        else:
            print("You went over, you lose")

    elif my_diffrernce_from_21 < computer_diffrernce_from_21:
        print("You win")

    elif my_diffrernce_from_21 > computer_diffrernce_from_21:
        print("You lose")

    elif my_diffrernce_from_21 == computer_diffrernce_from_21:
        print("Teko")

    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")