import random

options = ("piedra" , "papel" , "tijera")

computer_wins = 0
user_wins = 0

rounds = 1

while True:

  print("*" * 10)
  print("ROUND ", rounds)
  print("*" * 10)

  print(("Computer wins" , computer_wins))
  print(("User wins" , user_wins))

  user = input("Elige entre, piedra, papel o tijera: ")
  user = user.lower()

  rounds += 1

  if not user in options:
    print("TIENES 3 OPCIONES Y ELIGES UNA QUE NO ES, ERES NORMAL?")
    continue #para que  no ejecute el codigo hacia abajo y cree nuevo
   # exit() #para terminarlo si no elige opcion correcta


  computer = random.choice(options)
  print(f"usuario eligió {user} y la computadora eligió {computer}")

  if user == computer:
    print("EMPATE !!") 
  elif user == "piedra":
    if computer == "tijera":
      print("GANASTE !")
      user_wins += 1
    else:
      print("PERDISTE !!")
      computer_wins += 1
  elif user == "papel":
    if computer == "piedra":
      print("GANASTE !!")
      user_wins += 1
    else:
      print("PERDISTE !!")
      computer_wins += 1
  elif user == "tijera":
    if computer == "papel":
      print("GANASTE !!")
      user_wins += 1
    else:
      print("PERDISTE !!")
      computer_wins += 1
  else:
    print("Definitivamente quieres llevar la contraria?")

  if computer_wins == 3:
    print("Perdiste con la computadora :(")
    break

  if user_wins == 3:
    print("GANASTE !! :)")
    break