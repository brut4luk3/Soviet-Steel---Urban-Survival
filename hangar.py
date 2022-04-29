import t_55
import t_62

if __name__ == '__main__':

    t55 = t_55.T55("T-55", "D-10T 100mm rifled gun", 15, "SGMT 7.62mm light machine gun", "No AA Gun", 1450)
    t62 = t_62.T62("T-62", "U-5TS 115mm smoothbore gun", 10, "PKT 7.62mm light machine gun", "No AA Gun", 1650)

    print("Choose a map to fight!\n")
    maps = f"""
    <-1-> Kabul: Operation Storm 333 (Available vehicles: {t55.model}, {t62.model})
    <-2-> Grozny: First Chechen War (Available vehicles: {t55.model}, {t62.model})
    <-3-> Tskhinvali: Georgian War (Available vehicles: {t55.model}, {t62.model})
    """
    print(maps)

    choose_map = int(input("Type the number of the map: "))

    if choose_map == 1:
        print("We're off to Kabul then!")

    elif choose_map == 2:
        print("We're going to Grozny!")

    elif choose_map == 3:
        print("Hold tight, we're going to Tskhinvali!")

    else:
        while 1 or 2 or 3 not in choose_map:
            print("Wrong choice! Choose the number of the map!\n")
            choose_map_again = int(input("Choose: "))

            if choose_map_again == 1:
                print("We're off to Kabul then!")
                break

            elif choose_map_again == 2:
                print("We're going to Grozny!")
                break

            elif choose_map_again == 3:
                print("Hold tight, we're going to Tskhinvali!")
                break

            else:
                continue



