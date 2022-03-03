import matplotlib.pyplot as plt
def calc():

# Choose the operation
    choose = input("""If you want a term representation of f as an output using two known points from the graf of a linear function f
  Eg.: (Px | Py), (Qx | Qy)
press ENTER.

If you want to calculate the zero point using the term of f
type 'z' and press ENTER.
""")

# Visual demonstration of the graf
    def visual_graf():
        #calculating y
        y1 = k * 1 + d
        y2 = k * 5 + d

        #setting properties of grid
        plt.xlim(-5, 10)
        plt.ylim(-5, 10)
        plt.grid(True)

        #plotting the grid
        plt.axline((0, 0), (1, 0), color = "black")
        plt.axline((0, 0), (0, 1), color = "black")

        #plotting points of f
        plt.axline((1, y1), (5, y2))

        #naming x/y axis
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')

        #title
        plt.title(f"f(x) = {k} * x + {d}")

        # function to show the plot
        plt.show()

        # again
        again = input(
            "\n\n\n\n- If you want to restart press ENTER.\n- If you want to quit type 'e' and press ENTER.\n")
        if again == "e":
            exit()
        else:
            print("\n\n\n\n")
            calc()

# Getting the zero point
    def get_zero():
        print(f"f(x) = {k} * x + {d} = 0\n\n0 = {k} * x + {d}   | -{d}\n{0 - d} = {k} * x   | :{k}\n{0 - d} / {k} = {(0 - d) / k} = x\n\nN ({(0 - d) / k} | 0)")
        
        #again
        again = input(
            "\n\n\n\n- If you want to restart press ENTER.\n- If you want to see the graf visually type 'v' and press ENTER\n- If you want to quit type 'e' and press ENTER.\n")
        if again == "v":
            visual_graf()
        if again == "e":
            exit()
        else:
            print("\n\n\n\n")
            calc()

# Input Variables for zero point
    if choose == "z":
        k = float(input("\nk: "))
        d = float(input("d: "))

        #Check if input is right
        check = input(
            f"\nIf those Variables are right press ENTER, else type 'r' and press ENTER to restart.:\nf(x) = {k} * x + {d}\n")
        if check == "r":
            print("\n\n\n\n")
            calc()
        else:
            print("\n\nSolution:\n")
            get_zero()


# Input Variables
    Px = float(input("\nPx: "))
    Py = float(input("Py: "))

    Qx = float(input("Qx: "))
    Qy = float(input("Qy: "))

    #Check if input is right
    check = input(
        f"\nIf those Variables are right press ENTER, else type 'r' and press ENTER to restart.:\n({Px} | {Py}), ({Qx} | {Qy})\n")
    if check == "r":
        print("\n\n\n\n")
        calc()
    else:
        print("\n\nSolution:\n")

# Getting k
    k = (((Qy) - (Py)) / ((Qx) - (Px)))

    print(f"k = ({Qy} - {Py}) / ({Qx} - {Px})\nk = {(Qy) - (Py)} / {(Qx) - (Px)}\nk = {k}\n")

# Getting d
    d = ((Py) - (k) * (Px))

    print(f"{Py} = {k} * {Px} + d\nd = {Py} - {k} * {Px}\nd = {d}\n\n")


# Term representation
    print(f"f(x) = {k} * x + {d}")

    #again
    again = input(
        "\n\n\n\n- If you want to restart press ENTER.\n- If you want to get the zero point type 'z' and press ENTER\nIf you want to see the graf visually type 'v' and press ENTER\n- If you want to quit type 'e' and press ENTER.\n")
    if again == "z":
        print("\n\n\nZero Point:\n")
        get_zero()
    if again == "v":
        visual_graf()
    if again == "e":
        exit()
    else:
        print("\n\n\n\n")
        calc()


    


calc()