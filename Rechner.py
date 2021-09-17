import math
def calculator():
  item = input("Please input the item you want to calculate. (sphere/ cylinder/ cone)\n").strip().lower().replace(" ", "")

  if item == "sphere":
    class Sphere:
      def __init__(self, rd, item, number):
        self.rd = rd
        self.item = item
        self.number = number
        Sphere.change_rd(self)
        Sphere.calculate(self)
        Sphere.print(self)

      def change_rd(self):
        if self.rd == "radius":
          self.number = self.number
        elif self.rd == "diameter":
          self.number = self.number / 2
        else:
          print(f"{self.rd.capitalize()} is not a valid input. - Please try again.\n\n")
          calculator()

      def calculate(self):
        if self.item == "surface":
          self.calc_item = 4 * self.number**2 * math.pi
        elif self.item == "volume":
          self.calc_item = 4 * self.number**3 * math.pi / 3
        elif self.item == "circumfence":
          self.calc_item = 2 * self.number * math.pi
        else:
          print(f"{self.item.capitalize()} is not a valid input. - Please try again.\n\n")
          calculator()

      def print(self):
        print(f"The {self.item} of the sphere is {self.calc_item}")
          
        
    ask_rd = input("Do you want to use the radius or diameter as an input? (radius/ diameter)\n").strip().lower().replace(" ", "")
    ask_item = input("Please input the item you want to calculate. (surface/ volume/ circumfence)\n").strip().lower().replace(" ", "")
    ask_number = int(input (f"Please input {ask_rd}. \n"))
    Sphere(ask_rd, ask_item, ask_number)
  

  
  elif item == "cylinder":
    class Cylinder:
      def __init__(self, rd, item, number, height):
        self.rd = rd
        self.item = item
        self.number = number
        self.height = height
        Cylinder.change_rd(self)
        Cylinder.calculate(self)
        Cylinder.print(self)

      def change_rd(self):
        if self.rd == "radius":
          self.number = self.number
        elif self.rd == "diameter":
          self.number = self.number / 2
        else:
          print(f"{self.rd.capitalize()} is not a valid input. - Please try again.\n\n")
          calculator()

      def calculate(self):
        if self.item == "circumfence":
          self.calc_item = 2 * math.pi * self.number
        elif self.item == "ground":
          self.calc_item = math.pi * self.number**2
        elif self.item == "shell":
          self.calc_item = 2 * math.pi * self.number * self.height
        elif self.item == "surface":
          self.calc_item = 2 * math.pi * self.number * (self.number + self.height)
        elif self.item == "volume":
          self.calc_item = math.pi * self.number**2 * self.height
        else:
          print(f"{self.item.capitalize()} is not a valid input. - Please try again.\n\n")
          calculator()
        
      def print(self):
        print(f"The {self.item} of the cylinder is {self.calc_item}")


    ask_rd = input("Do you want to use the radius or diameter as an input? (radius/ diameter)\n").strip().lower().replace(" ", "")
    ask_item = input("Please input the item you want to calculate. (circumfence/ ground/ shell/ surface/ volume)\n").strip().lower().replace(" ", "")
    ask_height = int()
    if (ask_item == "shell") or (ask_item == "volume"):
      ask_height = int(input("Please input the height of the cylinder.\n"))
    ask_number = int(input (f"Please input {ask_rd}. \n"))
    Cylinder(ask_rd, ask_item, ask_number, ask_height)

    

  elif item == "cone":
    class Cone:
      def __init__(self, rd, item, number, height):
        self.rd = rd
        self.item = item
        self.number = number
        self.height = height
        Cone.change_rd(self)
        Cone.calculate(self)
        Cone.print(self)

      def change_rd(self):
        if self.rd == "radius":
          self.number = self.number
        elif self.rd == "diameter":
          self.number = self.number / 2
        else:
          print(f"{self.rd.capitalize()} is not a valid input. - Please try again.\n\n")
          calculator()

      def calculate(self):
        if self.item == "slantheight":
          self.calc_item = math.sqrt(self.height**2 + self.number**2)
        elif self.item == "ground":
          self.calc_item = math.pi * self.number**2
        elif self.item == "shell":
          self.calc_item = math.pi * self.number * (math.sqrt(self.height**2 + self.number**2))
        elif self.item == "surface":
          self.calc_item = (math.pi * self.number**2) + (math.pi * self.number * (math.sqrt(self.height**2 + self.number**2)))
        elif self.item == "volume":
          self.calc_item = 1 / 3 * (math.pi * self.number**2) * self.height
        else:
          print(f"{self.item.capitalize()} is not a valid input. - Please try again.\n\n")
          calculator()
        
      def print(self):
        if self.item == "slantheight":
          print(f"The slant height of the cylinder is {self.calc_item}")
        else:
          print(f"The {self.item} of the cylinder is {self.calc_item}")


    ask_rd = input("Do you want to use the radius or diameter as an input? (radius/ diameter)\n").strip().lower().replace(" ", "")
    ask_item = input("Please input the item you want to calculate. (slant height/ ground/ shell/ surface/ volume)\n").strip().lower().replace(" ", "")
    ask_height = int()
    if (ask_item == "slantheight") or (ask_item == "shell") or (ask_item == "surface") or (ask_item == "volume"):
      ask_height = int(input("Please input the height of the cone.\n"))
    ask_number = int(input (f"Please input {ask_rd}. \n"))
    Cone(ask_rd, ask_item, ask_number, ask_height)


  else:
    print(f"{item.capitalize()} is not a valid input. - Please try again.\n\n")
    calculator()

  input()
calculator()