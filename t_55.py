# the class is related to the role of said vehicle, with the T-55 being a MBT (Main Battle Tank)
class T55:

    # the vehicle has several attributes, like its model (ex: a, b, b3), main gun, coax, aa gun and health
    # these specifications are individual of each vehicle
    def __init__(self, model, gun, reload_time, coax, aa_gun, hitpoints):
        self.model = model
        self.gun = gun
        self.reload_time = reload_time
        self.coax = coax
        self.aa_gun = aa_gun
        self.hitpoints = hitpoints

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
    def upgrade(self):
        self.model = "T-55A"
        self.gun = "D-10T2S 100mm rifled gun"
        self.reload_time = 15
        self.coax = "SGMT 7.62mm light machine gun"
        self.aa_gun = "DShK 12.7mm heavy machine gun"
        self.hitpoints = 15000

        print("Your vehicle was retrofited with newly developed parts!")

    def specs(self):
        output = f"""
        Model: {tank.model}
        Gun: {tank.gun}
        Reload time: {tank.reload_time}/s
        Coax: {tank.coax}
        AA Gun: {tank.aa_gun}
        Hitpoints: {tank.hitpoints}
        """

        print(output)


if __name__ == '__main__':

    tank = T55("T-55", "D-10T2S 100mm rifled gun", 15, "SGMT 7.62mm light machine gun", "No AA Gun", 1450)

    tank.specs()