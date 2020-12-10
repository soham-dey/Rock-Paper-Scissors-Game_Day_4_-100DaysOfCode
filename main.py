import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves= [rock, paper, scissors]

comp_move_index= random.randint(0, len(moves)-1)
comp_move= moves[comp_move_index]


user_move= int(input("Enter 0 for rock, 1 for paper, 2 for scissor"))

if (user_move==0 and comp_move==rock) or (user_move==1 and comp_move==paper) or (user_move==2 and comp_move==scissors):
  print("The result is draw.\n" + "Computer's Move: " + comp_move +"\n" + "Your Move: " + moves[user_move])
elif (user_move==0 and comp_move==scissors) or (user_move==1 and comp_move==rock) or (user_move==2 and comp_move==paper):
  print("You won!\n" + "Computer's Move: " + comp_move +"\n" + "Your Move: " + moves[user_move])
else:
  print("Eh! You lost!\n" + "Computer's Move: " + comp_move +"\n" + "Your Move: " + moves[user_move])
