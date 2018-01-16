import random
import math



class Creature():

    def __init__(self, damage_creature_attack,damage_creature_defend,health_per_creature_attack,health_per_creature_defend,
    health_of_last_creature_attack,health_of_last_creature_defend,
    number_of_creatures_attack,number_of_creatures_defend,
    name_of_creature_attack,name_of_creature_defend,creature_counterattack):
        self.damage_creature_attack = damage_creature_attack
        self.damage_creature_defend = damage_creature_defend

        self.number_of_creatures_attack = number_of_creatures_attack
        self.number_of_creatures_defend = number_of_creatures_defend

        self.health_per_creature_attack = health_per_creature_attack
        self.health_per_creature_defend = health_per_creature_defend
        self.health_of_last_creature_attack = health_of_last_creature_attack
        self.health_of_last_creature_defend = health_of_last_creature_defend
        self.name_of_creature_attack = name_of_creature_attack
        self.name_of_creature_defend = name_of_creature_defend

        self.creature_counterattack = creature_counterattack


    def creature_attack_normal(self):
        total_damage_creature_attack = self.damage_creature_attack * self.number_of_creatures_attack
        total_health_creature_defend = self.number_of_creatures_defend * self.health_per_creature_defend

        if (total_damage_creature_attack > total_health_creature_defend) or (total_damage_creature_attack == total_health_creature_defend):
            Creature.creature_death(self.name_of_creature_defend)
        else:
            total_health_creature_defend = total_health_creature_defend - total_damage_creature_attack
            self.health_of_last_creature_defend = total_health_creature_defend % self.health_per_creature_defend
            self.number_of_creatures_defend = math.ceil(total_health_creature_defend / self.health_per_creature_defend)
            if self.health_of_last_creature_defend == 0 and self.number_of_creatures_defend > 0:
                self.health_of_last_creature_defend = self.health_per_creature_defend
            print("After "+self.name_of_creature_attack+" attacked there are " + self.name_of_creature_defend + " alive: "+  str(self.number_of_creatures_defend) + " and last creature has health: " + str(self.health_of_last_creature_defend))



            def creature_attack_counterattack(total_damage_creature_attack,total_health_creature_defend):
                print(self.name_of_creature_defend+" has counter attacked !")
                total_damage_creature_defend = self.number_of_creatures_defend * self.damage_creature_defend
                total_health_creature_attack = self.number_of_creatures_attack * self.health_per_creature_attack

                if (total_damage_creature_defend > total_health_creature_attack) or (total_damage_creature_defend == total_health_creature_attack):
                    Creature.creature_death(self.name_of_creature_attack)
                else:
                    total_health_creature_attack = total_health_creature_attack - total_damage_creature_defend
                    self.health_of_last_creature_attack = total_health_creature_attack % self.health_per_creature_attack
                    self.number_of_creatures_attack = math.ceil(total_health_creature_attack / self.health_per_creature_attack)
                    print(str(self.number_of_creatures_attack))
                    if (self.health_of_last_creature_attack == 0 and self.number_of_creatures_attack > 0):
                        self.health_of_last_creature_attack = self.health_per_creature_attack
                    print("After "+self.name_of_creature_defend+" has initiated an counter attack, there are " + self.name_of_creature_attack + " alive: "+  str(self.number_of_creatures_attack) + " and last creature has health: "+str(self.health_per_creature_attack))

            if self.creature_counterattack == True and self.number_of_creatures_defend > 0:
                if random.randint(1,100) >15:
                        creature_attack_counterattack(total_damage_creature_attack, total_health_creature_defend)


    def creature_defend():
        creature_health=+1
        Creature.creature_end_turn()

    def creature_death(creature_name):
        print(creature_name+" has died !!")

    def creature_end_turn():
        pass

    def creature_walk():
        pass


#fields:
#def __init__(self, damage_creature_attack,damage_creature_defend,
#health_per_creature_attack,health_per_creature_defend,
#health_of_last_creature_attack,health_of_last_creature_defend,
#number_of_creatures_attack,number_of_creatures_defend,
#name_of_creature_attack,name_of_creature_defend,creature_counterattack):
fight1 = Creature(10,10,10,10,10,10,10,20,"Demon","Pikeman",True)
fight1.creature_attack_normal()

print("###################################")
