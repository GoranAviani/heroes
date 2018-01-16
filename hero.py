class Hero():

    def __init__(self,hero_name,spellbook_spells,hero_current_mana,hero_max_mana,hero_creature_list,hero_skill_list):
        self.spellbook_spells=spellbook_spells
        self.hero_current_mana = hero_current_mana
        self.hero_max_mana = hero_max_mana
        self.hero_creature_list = hero_creature_list
        self.hero_skill_list=hero_skill_list
        self.hero_name=hero_name

    def hero_show_spells(self):
        for spell in self.spellbook_spells:
            print(self.hero_name + " has : "+spell)

    def hero_show_skills(self):
        for skill in self.hero_skill_list:
            print(self.hero_name + " has a skill : " + skill)

    def hero_walk(self):
        pass


    def gain_mana(self): #called on each day
        def calculate_max_mana(self):
            for skill in self.hero_skill_list:
                print("test "+skill)
                if skill == "wisdom2":
                    self.hero_max_mana=60
                else:
                    self.hero_max_mana=20
        calculate_max_mana(self)
        if self.hero_current_mana < self.hero_max_mana:
            self.hero_current_mana+=1
            print(self.hero_name + " has : " +str(self.hero_current_mana )+ " mana.")
            print(self.hero_name + "has maximum mana of : "+ str(self.hero_max_mana))

    def list_hero_creatures(self):
        for creature in self.hero_creature_list:
            print(creature + " display numbers: " + str(hero_creature_list[creature]))


print("HERO solmyr ###################################")
hero_spells = ["magic arrow", "lightning bolt","lightning bolt2"]
hero_current_mana=5
hero_max_mana=50
hero_creature_list={"goblins":30,"hogoblins":20,"golems":15}
hero_skill_list=["wisdom1","wisdom2","blabla"]
hero_name = "Solmyr"
solmyr = Hero(hero_name,hero_spells,hero_current_mana,hero_max_mana,hero_creature_list,hero_skill_list)
solmyr.hero_show_spells()
solmyr.list_hero_creatures()

print("HERO NEELA ###################################")
hero_spells = ["magic arrow", "lightning bolt","lightning bolt2"]
hero_current_mana=10
hero_max_mana=50
hero_creature_list={"goblins":430,"hogoblins":120,"golems":115}
hero_skill_list=["wisdom2","blabla"]
hero_name="Neela"
neela = Hero(hero_name,hero_spells,hero_current_mana,hero_max_mana,hero_creature_list,hero_skill_list)
neela.hero_show_skills()
neela.gain_mana()
