n = 10
m = n + 1
for i in range(n//2-1):
  for j in range(m):
    if i == n//2-2 and (j == 0 or j == m-1):
      print("*", end=" ")
    elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
                            or (j-i == m//2-n//2+3 and j > m//4)):
            print("*", end=" ")
    elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
                           or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
            print("*", end=" ")
    else:
            print(" ", end=" ")
  print()
for i in range(n//2-1, n):
  for j in range(m):
    if (i-j == n//2-1) or (i+j == n-1+m//2):
            print('*', end=" ")
    elif i == n//2-1:
              
      if j == m//2-1:
        print('  ', end="")
      elif j == m//2:
        print('  ', end="")
      else:
        print(' ', end=" ")
    else:
      print(' ', end=" ")
  print()

print("\n")



from time import sleep
name = "*insert name*"

import webbrowser
webbrowser.open('https://www.youtube.com/watch?v=hW8c1y2xsa0&t=4s', new=1)

sleep(1.5)

def display_words(words):
  for char in words:
    sleep(0.1)
    print(char, end="", flush=True)
  print(" ", end="")

def display_words2(words):
  for char in words:
    sleep(0.2)
    print(char, end="", flush=True)
  print()

def display_words3(words):
  for char in words:
    sleep(0.25)
    print(char, end="", flush=True)
  print("\n")

words = "Happy Birthday"
words2 = "to you!"
words3 = name
words4 = "*instert sentence*"
words5 = "*instert sentence*"
words6 = "it's true!"

display_words(words)
display_words2(words2)
sleep(1)
display_words(words)
display_words2(words2)
sleep(1)
print()

display_words(words)
display_words3(words3)
sleep(0.5)

display_words(words)
display_words2(words2)
sleep(1)
print()

display_words(words4)
display_words2(words6)
sleep(0.5)
display_words(words5)
display_words2(words6)
print()

display_words(words)
display_words3(words3)

display_words(words)
display_words2(words2)


input()