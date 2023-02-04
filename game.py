import random

def choise_options():
   options = ('Piedra', 'Papel', 'Tijera')
   user_option = input("Piedra, Papel o Tijera => ")
   user_option = user_option.capitalize()
   if not user_option in options:
       print('la opcion no es valida')
       # continue
       return None, None
   computer_option = random.choice(options)

   print('user option =>', user_option)
   print('computer option', computer_option)
   return user_option, computer_option

def check_rules(user_option,computer_option,user_wins,computer_wins):
   if user_option == computer_option:
       print('Empate')
   elif user_option == 'Piedra':
       if computer_option == 'Tijera':
           print('piedra gana a tijera')
           print('user ganó')
           user_wins +=1
       else:
           print('papel gana a piedra')
           print('computer ganó')
           computer_wins +=1
   elif user_option =='Papel':
       if computer_option == 'Piedra':
           print('papel gana a piedra')
           print('user ganó')
           user_wins += 1
       else:
           print('tijera gana a papel')
           print('computer ganó')
           computer_wins += 1
   elif user_option =='Tijera':
       if computer_option =='Papel':
           print('tijera gana a papel')
           print('user ganó')
           user_wins += 1
       else:
           print('piedra gana a tijera')
           print('computer ganó')
           computer_wins += 1
   return user_wins, computer_wins

def check_winner(user_wins,computer_wins):
   if computer_wins == 2:
       print('El ganador es la computadora')
       exit()
   if user_wins == 2:
       print('El ganador es el Usuario')
       exit()


def run_game():
   computer_wins = 0
   user_wins = 0
   rounds = 1
   while True:
       print('*'*10)
       print('ROUND', rounds)
       print('*' * 10)

       print('computer_wins', computer_wins)
       print('user_wins', user_wins)
       rounds += 1
       user_option, computer_option = choise_options()
       user_wins, computer_wins = check_rules(user_option,computer_option,user_wins,computer_wins)
       check_winner(user_wins,computer_wins)

run_game()
