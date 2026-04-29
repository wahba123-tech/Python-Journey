secret_word=("wahba")
display_word=['_', '_', 'h ','_','_' ]
print("Secret Word: _ _ h _ _")
guess_count=0
choice=input("do you want to play a game(y/n):").lower()
while choice=='y':
 guess=input("Guess a letter:")
 if guess in secret_word:
    print(guess)
    print("correct answer!")
    if guess=='a':
      display_word[1]='a' 
      display_word[4]='a'
      print(display_word)
    elif guess=='b':
      display_word[3] ='b' 
      print(display_word)
    elif guess=='w':
      display_word[0]='w' 
      print(display_word)
 else:
    print("wrong guess do it again!")   

 choice=input("do you want to play again(y/n):")  .lower() 
 if choice=='n' :
   break


secret_word = "wahba"
display_word = ["_" for _ in secret_word]  # Initialize display_word with underscores
print("Secret Word:", " ".join(display_word))

guess_count = 0
choice = input("Do you want to play a game? (y/n): ").lower()

while choice == 'y':
    guess = input("Guess a letter: ").lower()

    if guess in secret_word:
        print(f"✅ Correct! The letter '{guess}' is in the word.")

        # Update display_word at all matching positions
        for index, letter in enumerate(secret_word):
            if letter == guess:
                display_word[index] = guess  # Replace "_" with guessed letter

        print("Secret Word:", " ".join(display_word))
    else:
        print("❌ Wrong guess! Try again.")

    # Check if the player has guessed all the letters
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly!")
        break

    choice = input("Do you want to continue playing? (y/n): ").lower()
    if choice == 'n':
        break
