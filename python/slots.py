import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']


def play():
  ans = input("Play? (y/n): ")

  
  while ans != 'n':
  

    result = random.choices(symbols, k=3)
    
    formatted_result = ' | '.join(result)


    print(formatted_result)


    if formatted_result == "7️⃣ | 7️⃣ | 7️⃣":
        print("Jackpot! 💰")

    ans = input("Again? (y/n): ")

  print("Try again later!")


play()
