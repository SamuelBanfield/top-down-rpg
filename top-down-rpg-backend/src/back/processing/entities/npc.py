from . import entity as ent
from . import character as ch


# A non-playable character
class NPC(ch.Character):
    def __init__(self, npcName: str):
        self.target = None
        self.behaviour_type = 2
        self.team = 1
        self.hitProf = 0
        self.max_bulk = 20

        self.starting_items = []

        super().__init__(npcName)

        self.getStats()

        self.resetStats()
        self.resetHealth()

        self.refreshStatAfterEquipment()

        self.calcInitiative()

    # Collects entity base stats
    def getStats(self):
        ent.Entity.entityStats.getCharacterStats(self)
        self.getEquipment()
        self.convAttacks()

    # Checks if the character is proficient with the weapon
    def is_Proficient(self, weapon):
        return weapon.name in self.starting_items

    # Sees if the npc max bulk has been exceeded
    def is_exceededBulk(self):
        return self.bulk > self.max_bulk


# A hostile character
class Monster(NPC):
    def __init__(self, monsterName: str):
        super().__init__(monsterName)
        self.team = 2

    # Checks if entity is still alive
    def checkAlive(self):
        if self.health < 0:
            self.is_alive = False
            self.health = 0
