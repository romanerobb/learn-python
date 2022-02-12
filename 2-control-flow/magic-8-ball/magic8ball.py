import random

name = "Romane Robb"
question = "Will I win the lottery?"
answer = ""

random_number = random.randint(1, 21)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Sorry. Nope@"
elif random_number == 11:
  answer = "Something may happen."
elif random_number == 12:
  answer = "This is highly unlikely."
elif random_number == 13:
  answer = "The unlucky number."
elif random_number == 14:
  answer = "You win some. You lose some."
elif random_number == 15:
  answer = "Seyma says yes."
elif random_number == 16:
  answer = "Amelia says no."
elif random_number == 17:
  answer = "Well ofcourse."
elif random_number == 18:
  answer = "According to Monk, the TV show,...sure!"
elif random_number == 19:
  answer = "Keep your day job!"
elif random_number == 20:
  answer = "Winner, winner, vegetarian chicken dinner."
else:
  answer = "Error"

if name == "":
  print("Question: " + question)

if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")

else:
  print(name + " asks: " + question)
print("Magic 8-Ball's answer: "  + answer)
