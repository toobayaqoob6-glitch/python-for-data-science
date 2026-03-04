secret=8
guess=0

while guess != secret:
   guess=int(input("enter your number:"))
   if guess > secret:
       print("TOO HIGH")
   elif guess <secret:
       print ("TOO LOW")  
   else:
       print("You won the game!")
    