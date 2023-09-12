while True:

    print()
    print("  mini-kalkulator  ")
    print()

    numer1 = int(input("legg et numer her: "))

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

    numer2 = int(input("legg et numer her: "))
    print()

    if operatorene == "+":
        print(f"{numer1} {operatorene} {numer2} = {numer1 + numer2}")
        print()

    elif operatorene == "-":
        print(f"{numer1} {operatorene} {numer2} = {numer1 - numer2}")
        print()

    elif operatorene == "*":
        print(f"{numer1} {operatorene} {numer2} = {numer1 * numer2}")
        print()

    elif operatorene == "%":
        print(f"{numer1} {operatorene} {numer2} = {numer1 % numer2}")
        print()

    elif operatorene == "**":
        print(f"{numer1} {operatorene} {numer2} = {numer1 ** numer2}")
        print()

    elif operatorene == "//":
        print(f"{numer1} {operatorene} {numer2} = {numer1 // numer2}")
        print()

    elif operatorene == "/":
        print(f"{numer1} {operatorene} {numer2} = {numer1 / numer2}")
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
