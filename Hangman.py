import random
import urllib.request
from time import sleep
from getch import pause_exit
from PyDictionary import PyDictionary

tries = 6

def game():
  try:
    word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
  except:
    print("An exception occurred!\nPython cannot connect to the internet.\nProgram will close in 5 seconds.")
    sleep(5)
    exit
    
  random_word = random.choice(words)
  blanks = '_' * len(random_word)
  
  hangman_symbol = make_hangman_symbol(tries, space)
  hangman_symbol = f" +---+\n{space}     |\n{space}     |\n{space}     |\n{space}    ==="
  for i in range(len(blanks)):
    first_space_list.pop()
    first_space = "".join(first_space_list)
  print(f"Word = {blanks}{first_space}{hangman_symbol}")
  random_word_unedited = random_word
  
  used_letters = []

  def guess_the_word(random_word, blanks, tries):
    while tries > 0:
      guess_right = False
      define = False
      hack_true = False
      guess = input("\nMake a guess! (Enter a single letter)\n").lower().strip()

      if guess == "hack=true":
        hack_true = True
        print(f"\nSecret word = {random_word_unedited}")
        guess_the_word(random_word, blanks, tries)

      if guess == "define":
        define = True
        dictionary=PyDictionary()
        print()
        print(dictionary.meaning(random_word_unedited))
        guess_the_word(random_word, blanks, tries)

      if len(guess) != 1 and not hack_true and not define:
        print("\nJust input a single letter!")
        guess_the_word(random_word, blanks, tries)

      for i in random_word:
        if i in guess:
          r_word_index = random_word.index(guess)

          blanks_list = list(blanks)
          blanks_list[r_word_index] = guess
          blanks = "".join(blanks_list)

          r_word_list = list(random_word)
          r_word_list[r_word_index] = "_"
          random_word = "".join(r_word_list)
          
          hangman_symbol = make_hangman_symbol(tries, space)
          print(f"\nYou are right! The letter {guess} is in the secret word.")
          print(f"Word = {blanks}{first_space}{hangman_symbol}")

          if "_" in blanks:
            guess_right = True
          else:
            print("Congratulations you won!")
            pause_exit(0, "Press any key to exit...\n")
          
          guess_the_word(random_word, blanks, tries)
          return random_word

      if guess_right == False:
        

        if guess in used_letters:
          print(f"\nSorry you have already tried the letter '{guess}'!\nPlease try again!")
          hangman_symbol = make_hangman_symbol(tries, space)
          print(f"Word = {blanks}{first_space}{hangman_symbol}")
          guess_the_word(random_word, blanks, tries)

        else:
          tries = tries - 1
          if tries == 0:
            pause_exit(0, f"\nGame Over!\nThe secret word was {random_word_unedited}\nPress any button to exit...\n")
          
          print("\nSorry your guess was wrong!")
          print(f"You have {tries} tries left.")
          hangman_symbol = make_hangman_symbol(tries, space)
          print(f"Word = {blanks}{first_space}{hangman_symbol}")

          used_letters.append(guess)

          guess_the_word(random_word, blanks, tries)
          return tries
        

  guess_the_word(random_word, blanks, tries)


first_space = "                      "
space = first_space + "       "
first_space_list = list(first_space)

def make_hangman_symbol(tries, space):
  if tries == 6:
    hangman_symbol = f" +---+\n{space}     |\n{space}     |\n{space}     |\n{space}    ==="
  if tries == 5:
    hangman_symbol = f" +---+\n{space} O   |\n{space}     |\n{space}     |\n{space}    ==="
  if tries == 4:
    hangman_symbol = f" +---+\n{space} O   |\n{space} |   |\n{space}     |\n{space}    ==="
  if tries == 3:
    hangman_symbol = f" +---+\n{space} O   |\n{space}/|   |\n{space}     |\n{space}    ==="
  if tries == 2:
    hangman_symbol = f" +---+\n{space} O   |\n{space}/|\  |\n{space}     |\n{space}    ==="
  if tries == 1:
    hangman_symbol = f" +---+\n{space} O   |\n{space}/|\  |\n{space}/    |\n{space}    ==="
  if tries == 0:
    hangman_symbol = f" +---+\n{space} O   |\n{space}/|\  |\n{space}/ \  |\n{space}    ==="
  return hangman_symbol

game()