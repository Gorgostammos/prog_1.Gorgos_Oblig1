while True:

    print("   mini-kalkulator  ")
    print()

    tall1 = int(input("legg et numer her: "))
    print()

    operatorene = input("velg operator: ")
    if operatorene == "+":
        print()
    elif operatorene == "-":
        print()
    elif operatorene == "*":
        print()
    elif operatorene == "%":
        print()
    elif operatorene == "**":
        print()
    elif operatorene == "//":
        print()
    elif operatorene == "/":
        print()
    else:
        print("Du må velge en operator  ")
        print()
        operator = ["*", "+", "-", "/", "//", "**", "%"]
        print(operator)

        operatorene = input("velg operator: ")
        if operatorene == "+":
            print()
        elif operatorene == "-":
            print()
        elif operatorene == "*":
            print()
        elif operatorene == "%":
            print()
        elif operatorene == "**":
            print()
        elif operatorene == "//":
            print()
        elif operatorene == "/":
            print()
        else:
            break
        print()

    tall2 = int(input("legg et numer her: "))
    print()

    if operatorene == "+":
        print(f"svare: {tall1 + tall2}")
        print()

    elif operatorene == "-":
        print(f"svare: {tall1 - tall2}")
        print()

    elif operatorene == "*":
        print(f"svare: {tall1 + tall2}")
        print()

    elif operatorene == "%":
        print(f"svare: {tall1 % tall2}")
        print()

    elif operatorene == "**":
        print(f"svare: {tall1 ** tall2}")
        print()

    elif operatorene == "//":
        print(f"svare: {tall1 // tall2}")
        print()

    elif operatorene == "/":
        print(f"svare: {tall1 / tall2}")
        print()


    slut = input("Vil du Forsatte?  ")
    if slut == "ja":
        continue
    elif slut == "nei":
        print("hadet bra!!")
        break
    else:
        print("Du må velge ja eller nei")
        slut = input("Vil du Forsatte?  ")
        if slut == "ja":
            continue
        elif slut == "nei":
            print("hadet bra!!")
            break
        print()
