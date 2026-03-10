import random
import time

plays = ('Rock', 'Paper', 'Scissors')
pc = random.choice(plays)
text1 = "Can you be me in Rock paper scissors"
text2 = "SHHoot!!!"
print( text1.center(20, "-") )
user = input("Enter your choice(rock, paper, scissors): ")
for i in range(3):
    time.sleep(1)
    print(f"{plays[i]:-^30}")
time.sleep(1)
print(f"{text2:-^30}")
time.sleep(1)
if user.lower() == pc.lower():
    print("It's a draw")
elif user.lower() == 'paper' and pc == plays[0]:
    print("You win")
elif user.lower() == 'scissors' and pc == plays[1]:
    print("You win")
elif user.lower() == 'rock' and pc == plays[2]:
    print("You win")
elif user.lower() == 'scissors' :
