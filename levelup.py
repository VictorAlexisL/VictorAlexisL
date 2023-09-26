character_list = []

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.level = 0
        self.exp = 0
        self.character_class = character_class
        self.strength = 10
        self.intelligence = 10
        self.dexterity = 10
        character_list.append(self.name)
        return f"Character created: {self.name}"

    def gain_exp(self):
        import random
        self.exp += random.randint(1,100)
        if self.exp >= 100:
            self.level_up()        
        return self.exp
    
    def level_up(self):
        self.level += 1
        if self.character_class == "Warrior":
            import random
            self.strength += random.randint(1,2)
            self.intelligence += random.randint(0,1)
            self.dexterity += random.randint(0,2)
        elif self.character_class == "Wizard":
            import random
            self.strength += random.randint(0,1)
            self.intelligence += random.randint(1,2)
            self.dexterity += random.randint(0,2)
        else:
            import random
            self.strength += random.randint(0,2)
            self.intelligence += random.randint(0,1)
            self.dexterity += random.randint(1,2)
        print(f"Level Up! Current level: {self.level}")
        return self.level
    
    def generate_lvl5_stats(self):
        while self.level < 5:
            Character.get_exp(self)
        print(self.strength)
        print(self.intelligence)
        print(self.dexterity)
        print("Done testing.")
        return True
    
merlin = Character("Merlin", "Wizard")

Character.generate_lvl5_stats(merlin)

print(character_list)
