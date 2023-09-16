soccer = """





                           ,;;;:.
                          ;;''''`:
                          ;(  O O|              ,;;,
                           |   _\|              \  |
                            \__-/              ,' /
                            |   |             /  /
                      _,--''`---'''-------.,-'  /
                    ,'  /          `.     |  _,'
                  ,'    |====== WM =|     |-'
                 \      ,======|  |=|''---'
                / `.  ,' \      \/ /
              ,'. ,'`'   | --._    |
            ,'  ,'       |         |
        __,' _,'         \    -._  |
       `- ,-'            |---------)
      ';;'               ;:::::::::|
                        ;:::::::::::\
                       /::::::;:::::|
                      /_:::::/\:::::_\
                      / `-:_/  \,-' |
                     /    /     \   |
                     |   |      | _,)
                     \_,-\      |   |
                      \   |     |   |
                       |__|      \,-|
                       /##|      |  |
                      \##/       |  |
                     ,-'''-.     |,-|
                    // \_/ \\    `.##\
                    |\_/ \_/|      `--`
           jrei     \/ \_/ \/
                     `-...-'
"""
import random
print(soccer)
print("Welcome to Stryktipset - Can you get all 13?\n")
game_on = True
while game_on:
    enter_stryktipsrad = input("Enter your Stryktipsrad. \n")

    score = 0
    alternative = ["1", "x", "2"]
    facit = []
    my_stryktipsrad = enter_stryktipsrad.split(", ")

    match_1 = []
    match_2 = []
    match_3 = []
    match_4 = []
    match_5 = []
    match_6 = []
    match_7 = []
    match_8 = []
    match_9 = []
    match_10 = []
    match_11 = []
    match_12 = []
    match_13 = []

    for _ in range(13):
        one_match = random.choice(alternative)
        facit.append(one_match)

    match_1.append(my_stryktipsrad[0])
    match_1.append(facit[0])
    match_2.append(my_stryktipsrad[1])
    match_2.append(facit[1])
    match_3.append(my_stryktipsrad[2])
    match_3.append(facit[2])
    match_4.append(my_stryktipsrad[3])
    match_4.append(facit[3])
    match_5.append(my_stryktipsrad[4])
    match_5.append(facit[4])
    match_6.append(my_stryktipsrad[5])
    match_6.append(facit[5])
    match_7.append(my_stryktipsrad[6])
    match_7.append(facit[6])
    match_8.append(my_stryktipsrad[7])
    match_8.append(facit[7])
    match_9.append(my_stryktipsrad[8])
    match_9.append(facit[8])
    match_10.append(my_stryktipsrad[9])
    match_10.append(facit[9])
    match_11.append(my_stryktipsrad[10])
    match_11.append(facit[10])
    match_12.append(my_stryktipsrad[11])
    match_12.append(facit[11])
    match_13.append(my_stryktipsrad[12])
    match_13.append(facit[12])

    print(my_stryktipsrad)
    print("---------------")
    print(facit)
    print(match_1)
    print(match_2)
    print(match_3)
    print(match_4)
    print(match_5)
    print(match_6)
    print(match_7)
    print(match_8)
    print(match_9)
    print(match_10)
    print(match_11)
    print(match_12)
    print(match_13)

    if match_1[0] == match_1[1]:
        score += 1
    if match_2[0] == match_2[1]:
        score += 1
    if match_3[0] == match_3[1]:
        score += 1
    if match_4[0] == match_4[1]:
        score += 1
    if match_5[0] == match_5[1]:
        score += 1
    if match_6[0] == match_6[1]:
        score += 1
    if match_7[0] == match_7[1]:
        score += 1
    if match_8[0] == match_8[1]:
        score += 1
    if match_9[0] == match_9[1]:
        score += 1
    if match_10[0] == match_10[1]:
        score += 1
    if match_11[0] == match_11[1]:
        score += 1
    if match_12[0] == match_12[1]:
        score += 1
    if match_13[0] == match_13[1]:
        score += 1

    if score == 13:
        print(f"Wow, Unbelievable You got {score} out of 13 at Stryktipset, this week.")
    elif score == 12 or score == 11:
        print(f"Really really good You got {score} out of 13 at Stryktipset, this week.")
    elif score == 10:
        print(f"Not bad at all You got {score} out of 13 at Stryktipset, this week.")
    elif score == 2:
        print(f"Embarrassing You got {score} out of 13 at Stryktipset, this week.")
    elif score == 1:
        print(f"Maybe you should try something else? You got {score} out of 13 at Stryktipset, this week.")
    elif score == 0:
        print(f"I don't even know what to say to you, You got {score} out of 13 at Stryktipset, this week.")
    else:
        print(f"You got {score} out of 13 at Stryktipset this week.")
    play_again = input('\nDo you want to go for a new Stryktipsrad? "YES" or "NO"\n').lower()
    if play_again == "yes":
        print("Good Luck!")
    else:
        print("\nBye for now!")
        game_on = False


