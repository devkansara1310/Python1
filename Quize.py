#Quize 

def check_guess(guess, answer):
  global score
  still_guessing = True
  attempt = 0
  while still_guessing and attempt < 3:
    if guess.lower() == answer.lower():
      print("Correct ans")
      score+=1
      still_guessing=False
    else:
      if attempt < 2:
        guess = input("Sorry Wrong Answer, Try again !")
      attempt+=1  
  if attempt==3:
    print("The Correct answer is :", answer)

score=0
print("Guess the Animal")
guess1=input("Q.1 Which bear live at the north pole?")
check_guess(guess1,"Polar Bear")
guess2=input("Q.2 Fastest Animal on planet")
check_guess(guess2,"Cheetah")
guess3=input("Q.3 Largest Animal")
check_guess(guess3,"Elephant")
