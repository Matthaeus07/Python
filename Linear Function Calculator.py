print("This tool was made to give a term representation of f, using two known points from the graf of a linear function f. Eg.: (Px | Py), (Qx | Qy)\n\n")


def calc():

    # Input Variables
    Px = float(input("Px: "))
    Py = float(input("Py: "))

    Qx = float(input("Qx: "))
    Qy = float(input("Qy: "))

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

    # Getting the zero point
    def get_zero():
        print(f"f(x) = {k} * x + {d} = 0\n\n0 = {k} * x + {d}   | -{d}\n{0 - d} = {k} * x   | :{k}\n{0 - d} / {k} = {(0 - d) / k} = x\n\nN ({(0 - d) / k} | 0)")
        again = input(
            "\n\n\n\n- If you want to restart press ENTER.\n- If you want to quit type 'e' and press ENTER.\n")
        if again == "e":
            exit()
        else:
            print("\n\n\n\n")
            calc()


    # Term representation
    print(f"f(x) = {k} * x + {d}")

    again = input(
        "\n\n\n\n- If you want to restart press ENTER.\n- If you want to get the zero point type 'z' and press ENTER\n- If you want to quit type 'e' and press ENTER.\n")
    if again == "z":
        print("\n\n\nZero Point:\n")
        get_zero()
    elif again == "e":
        exit()
    else:
        print("\n\n\n\n")
        calc()



calc()
