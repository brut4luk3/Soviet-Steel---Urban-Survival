# the class is named after the base model of the vehicle, with the T-62 being a MBT (Main Battle Tank)
class T62:

    # the vehicle has several attributes, like its model (ex: a, b, b3), main gun, coax, aa gun and health
    # these specifications are individual of each vehicle
    def __init__(self, model, gun, reload_time, coax, aa_gun, hitpoints):
        self.model = model
        self.gun = gun
        self.reload_time = reload_time
        self.coax = coax
        self.aa_gun = aa_gun
        self.hitpoints = hitpoints

    # this is a little function created to increment the specs menu. It's separated from the specs method to allow it's repositioning
    def tank_history (self):
        print("Being first introduced in 1961, the T-62 is a further development of the T-55 series. With low profile, thick turret armor and a smoothbore gun with quicker reload, the T-62 is a good street brawler.")

    # these functions are the main commands of which the player will make use throughout the gameplay

    def fire_main_gun(self):
        print("On the way! (the gunner fires the main gun)")

    def reloading(self):
        print("(reloading...")

    def fire_coax(self):
        print("TAKATAKATAKATAKATAKATAKATAKATAKATAKA... (the gunner fires the coax)")

    def fire_aa_gun(self):
        print("BUMBUMBUMBUMBUM... (the commander fires the AA gun)")

    def move_forward(self):
        print("Driver, crank it! (the vehicle steers forward)")

    def move_backward(self):
        print("Driver, fall back! (the vehicle steers backward)")

    # this function will be called whenever the player achieves the research progress
    def upgrade_1(self):
        self.model = "T-62. Obj. 1972"
        self.gun = "U-5TS 115mm smoothbore gun"
        self.reload_time = 8
        self.coax = "PKT 7.62mm light machine gun"
        self.aa_gun = "DShK 12.7mm heavy machine gun"
        self.hitpoints = 17500

        print("Your vehicle was retrofited with newly developed parts!")

    def upgrade_2(self):
        self.model = "T-62M"
        self.gun = "U-5TS 115mm smoothbore gun"
        self.reload_time = 6
        self.coax = "PKT 7.62mm light machine gun"
        self.aa_gun = "DShK 12.7mm heavy machine gun"
        self.hitpoints = 19700

        print("Your vehicle was retrofited with newly developed parts!")


    def specs(self):
        output = f"""
        Model: {t62.model}
        Gun: {t62.gun}
        Reload time: {t62.reload_time}/s
        Coax: {t62.coax}
        AA Gun: {t62.aa_gun}
        Hitpoints: {t62.hitpoints}
        """

        print(output)

if __name__ == '__main__':

    t62 = T62("T-62", "U-5TS 115mm smoothbore gun", 10, "PKT 7.62mm light machine gun", "No AA Gun", 1650)

    t62.tank_history()
    t62.specs()

    print("Press '1' to Upgrade or '2' to exit. \n")
    choice = int(input("Choose: "))

    if choice == 1:
        t62.upgrade_1()
        t62.specs()

    elif choice == 2:
        print("Returning to the menu...")

    else:
        while 1 or 2 not in choice:
            print("Wrong choice! Press '1' to Upgrade or '2' to exit!\n")
            choice2 = int(input("Choose: "))

            if choice2 == 1:
                t62.upgrade_1()
                t62.specs()
                break

            elif choice2 == 2:
                print("Returning to the menu...")

            else:
                continue

    retrofit_again = f"There's another retrofited version of your {t62.model} available! Would you like to upgrade?\n"
    print(retrofit_again)
    choice3 = int(input("Choose: "))

    if choice3 == 1:
        t62.upgrade_2()
        t62.specs()

    elif choice3 == 2:
        print("Returning to the menu...")

    else:
        while 1 or 2 not in choice3:
            print("Wrong choice! Press '1' to Upgrade or '2' to exit!\n")
            choice4 = int(input("Choose: "))

            if choice4 == 1:
                t62.upgrade_2()
                t62.specs()
                break

            elif choice4 == 2:
                print("Returning to the menu...")

            else:
                continue