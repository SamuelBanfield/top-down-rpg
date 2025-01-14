from . import entity as ent
from . import attack as at
from .stats.make_dataframes import weapon_types


class Item(ent.Entity):

    def __init__(self, itemName):
        super().__init__(itemName)
        self.is_carried = True
        self.type = ''

    # Checks if the item is a weapon
    def is_Weapon(self):
        if self.type in weapon_types:
            return True
        else:
            return False

    # Checks if the item is armour
    def is_Armour(self):
        if self.type in ['Under', 'Over']:
            return True
        else:
            return False


class Weapon(Item):
    def __init__(self, weaponName):
        super().__init__(weaponName)
        self.impact = 0
        self.sharpness = 0

        self.velocity = 0
        self.energy = 0

        self.is_melee = True

        self.getStats()

    # Collects entity base stats
    def getStats(self):
        ent.Entity.entityStats.getWeaponStats(self)
        pass

    # Updates the velocity of the weapon
    def updateVelocity(self, velocity: float):
        self.velocity = velocity

    # Calculates and updates the energy of the weapon
    def updateEnergy(self):
        self.energy = self.velocity * self.impact


class Armour(Item):
    def __init__(self, armourName):
        super().__init__(armourName)
        self.type = ''
        self.value = 0
        self.flex: float = 0
        self.weight = 0
        self.coverage = 0

        self.getStats()

    # Collects entity base stats
    def getStats(self):
        ent.Entity.entityStats.getArmourStats(self)
