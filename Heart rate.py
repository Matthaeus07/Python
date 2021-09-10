# Put heart rate here:
heart_rate = int(input("PLease enter your heart rate. \n"))



high_heart_rate = 100
extremely_high_heart_rate = 140
low_heart_rate = 60
extremely_low_heart_rate = 40


hhr_var = heart_rate >= high_heart_rate
ehhr_var = heart_rate >= extremely_high_heart_rate
lhr_var = heart_rate <= low_heart_rate
elhr_var = heart_rate <= extremely_low_heart_rate

import random
import time

print("Measuring heart rate:")
for num_1 in range(random.randint(1, 4)):
  time.sleep(1)
  print("...")
time.sleep(1)
print(f"Measuring complete. - (Took {num_1 + 1} sec)")
print("Calculating results:")
for num_2 in range(random.randint(1, 3)):
  time.sleep(1)
  print("...")
time.sleep(1)

if heart_rate <= 0:
  print("ERROR")
  print("Couldn't calculate results!")
  print("(Heart rate invalid.)")

else:
  print(f"Done! - (Took {num_2 + 1} sec)")
  print("")
  print("Results:")
    
  if ehhr_var:
    print(f"Heart rate far too high! ({heart_rate}BPM)")
  elif hhr_var:
    print(f"Heart rate higher than normal! ({heart_rate}BPM)")
  elif elhr_var:
    print(f"Heart rate far too low! ({heart_rate}BPM)")
  elif lhr_var:
    print(f"Heart rate lower than normal! ({heart_rate}BPM)")
  else:
    print (f"Heart rate ok! ({heart_rate}BPM)")

  if ehhr_var or elhr_var:
    print("Go to a doctor!")
  
time.sleep(15)
print("\n \n \nProgram will close in 30 seconds")
time.sleep(29)
print("Program will close now.")
time.sleep(1)