print("This tool was made to give a term representation of f, using two known points from the graf of a linear function f.\nEg.: (Px | Py), (Qx | Qy)\n\n")
def calc():
    
    # Input Variables
    Px = float(input("Px: "))
    Py = float(input("Py: "))

    Qx = float(input("Qx: "))
    Qy = float(input("Qy: "))


    check = input(f"\nIf those Variables are right press ENTER, else type 'r' and press ENTER to restart.:\n({Px} | {Py}), ({Qx} | {Qy})\n")
    if check == "r":
        print("\n\n\n\n")
        calc()
    else:
        print("\n\nSolution:\n")

    #Getting k
    k = (((Qy) - (Py)) / ((Qx) - (Px)))

    print(f"k = ({Qy} - {Py}) / ({Qx} - {Px})\nk = {(Qy) - (Py)} / {(Qx) - (Px)}\nk = {k}\n")


    #Getting d
    d = ((Py) - (k) * (Px))

    print(f"{Py} = {k} * {Px} + d\nd = {Py} - {k} * {Px}\nd = {d}\n\n")


    #Final Results
    print(f"f(x) = {k} * x + {d}")


    again = input("\n\n\n\nIf you want to restart press ENTER.\nIf you want to quit type 'e' and press ENTER.\n")
    if not again == "e":
        print("\n\n\n\n")
        calc()
    else:
        exit()
calc()