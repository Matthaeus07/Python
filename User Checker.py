import time
def program():

  available_users = [("Paul", 22), ("Max", 32), ("Tom", 19), ("John", 55)]
  

  username = input("Please enter username.\n").strip().capitalize()
  print("")
  

  def input_all():
    print(f"All users ({len(available_users)}):")
    for all_users in available_users:
      print(all_users[0])
    print("\n")
    program()

  p_ = "-----------------------------------"

  def age_fun(name, index):
    age = available_users[index][1]
    print("Checking user age.")
    print(f"User {name} has the age {age}.")
    print(p_)
  
  def mail_fun(name, index):
    year_born = 2021 - available_users[index][1]
    print("Checking user mail.")
    print(f"User {name} has the E-Mail {name}.{year_born}@outlook.at")
    print(p_)


  if username.lower() == "all":
    input_all()

  if username != "all":
    for i in range(0, len(available_users)):
      if username in available_users[i]:
        print(f"Found user {username} in database.\n")
        found_user = True

        check_age = input("Do you want to check age? (True/False)\n").strip().lower()
        check_mail = input("Do you want to check mail? (True/False)\n").strip().lower()

        if check_age == "true" or "t" or check_mail == "true" or "t":
          print(p_)

        if (check_age == "true") or (check_age == "t"):
          age_fun(username, i)
        elif (check_age == "false") or (check_age == "f"):
          check_age = False
        else:
          print(f"Input ({check_age}) is not a boolean.")
          program()
      
        if (check_mail == "true") or (check_mail == "t"):
            mail_fun(username, i)
        elif (check_mail == "false") or (check_mail == "f"):
          check_mail = False
        else:
          print(f"Input ({check_mail}) is not a Boolean")
          program()
    if found_user == False:
      print("ERROR")
      print("Failed to find user in database. - Try again.\n\n")
      program()

  time.sleep(15)
  print("\n \n \nProgram will close in 30 seconds")
  time.sleep(29)
  print("Program will close now.")
  time.sleep(1)
program()