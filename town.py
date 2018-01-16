class Town():

    def __init__(self, has_buildings,player_gold,hero_in_town,hero_has_spellbook,hero_name):
        self.has_buildings=has_buildings
        self.player_gold = player_gold
        self.hero_in_town = hero_in_town
        self.hero_has_spellbook = hero_has_spellbook
        self.hero_name = hero_name


    def enter_town(self):
        for building in self.has_buildings:
            Town.display_building(building)

        if self.hero_in_town == True and self.hero_has_spellbook == True:
            Town.hero_get_spells(self)

    def display_building(building):
        print("# Town has: "+building)


    def hero_get_spells(self):
        has_building_lvl = str(0) #had to add because when town does not have mage guild
        max_lvl_player_has_buidling = 0
        for building in has_buildings:
            if building[:len(building)-1] == "mage_guild_lvl_":
                has_building_lvl = building[len(building)- 1:len(building)]
                if int(has_building_lvl) > max_lvl_player_has_buidling:
                    max_lvl_player_has_buidling = int(has_building_lvl)

        for spell in all_spells:
            if spell not in has_spells:
                if (spell[len(spell)-1 : len(spell)] == has_building_lvl) or (spell[len(spell)-1 : len(spell)] < has_building_lvl):
                     has_spells.append(spell)
        Town.list_hero_spells(self)


    def list_hero_spells(self):
        print(self.hero_name + "has spells: ")
        for spell in has_spells:
            print(spell)


    def build_building(self, new_building):
        #checking for money and construction
        def check_building_requirements(self,new_building):
            #checking what building type building is and calling a fucntion with that building type
            building_type = new_building[:len( new_building ) - 1]
            if building_type == "barracks_type_":
                Town.check_required_lvl(self,new_building,building_type)
            elif building_type == "mage_guild_lvl_":
                Town.check_required_lvl(self,new_building,building_type)
            elif building_type == "hall_":
                Town.check_required_lvl(self,new_building,building_type)
            elif building_type == "fort_":
                Town.check_required_lvl(self,new_building,building_type)
            elif building_type == "market_":
                Town.check_required_lvl(self,new_building,building_type)
            elif building_type == "tavern_":
                Town.check_required_lvl(self,new_building,building_type)
            else:
                print("You have typed a building that does not exist in this game, please try again.")


        if new_building in self.has_buildings:
             print("Sorry, you cant build it beacause you already have " + new_building)
        #checking if barracks are build in order ex: you cant build lvl 3 if you dont have lvl 1 and 2
        else:
            check_building_requirements(self,new_building)

    def check_required_lvl(self,new_building,building_type):  #look what level of building is the max level player has
        constructing_building_lvl = new_building[len(new_building)-1:len(new_building)]
        print("Construction asked for a " + building_type + " with level: " + constructing_building_lvl)
        max_lvl_player_has_buidling = 0
        for building in has_buildings:
            if building[:len(building)-1] == building_type:
                has_building_lvl = building[len(building)- 1:len(building)]
                if int(has_building_lvl) > max_lvl_player_has_buidling:
                    max_lvl_player_has_buidling = int(has_building_lvl)
        print("Town has " + building_type + " of maximum level: " + str(max_lvl_player_has_buidling))

        if str(constructing_building_lvl) == str((max_lvl_player_has_buidling + 1)):
            print("Building " + building_type + "has been approved because town already has level " + str(max_lvl_player_has_buidling) +
            " and player has asked for level " + str(constructing_building_lvl))
            Town.construction_of_building(self,new_building)
        else:
            print ("You can't build " + new_building + " because you dont have required buildings")


    def construction_of_building(self,new_building):
        if (self.player_gold == all_buildings[new_building]) or (self.player_gold > all_buildings[new_building]) :
            self.has_buildings.append(new_building)
            self.player_gold -= all_buildings[new_building]
            print("Building has been built and now you have: ")
            self.enter_town()
        else:
            print("You dont have enough money to purchase " + building_name)


    def buy_spellbook(self):
        for building in has_buildings:
            if building[:len(building)-1] == "mage_guild_lvl_":
                if self.hero_in_town and self.hero_has_spellbook == False and ((self.player_gold == 500) or (self.player_gold > 500)):
                    buy_spellbook = input ("Do you want to buy a spellbook? y/n ")
                    if buy_spellbook == "y":
                        self.hero_has_spellbook = True
                        self.player_gold -= 500
                        Town.hero_get_spells(self)
                    elif buy_spellbook == "n":
                        print("If you don't buy it now I'll keep bothering you every time i see you in this city...")

                    else:
                        Town.buy_spellbook(self)
    def buy_creatures(self, buying_from_barracks, buying_number_of_creatures):
        for creature in all_barracks_creature_price:
            if buying_from_barracks == creature:
                        self.player_gold = self.player_gold - ( buying_number_of_creatures * all_barracks_creature_price[creature])
        for creature in all_barracks_creature_num:
            if buying_from_barracks == creature:
                all_barracks_creature_num[creature] = all_barracks_creature_num[creature] - buying_number_of_creatures
                for_message = all_barracks_creature_num[creature]
                town_defending_creatures.update({buying_from_barracks:buying_number_of_creatures})
                print("You have bought "+str(buying_number_of_creatures)+ " and now you have " + str(self.player_gold) + " gold left.")
                print("In barracks " + buying_from_barracks + " there are " + str(for_message) + " creatures. ")


    def list_creatures_in_barracks(self):
        for creatures in all_barracks_creature_num:
            print("In there are " + all_barracks_creature_num(creatures)+ " left.")

    def list_town_creatures(self):
        for creature in town_creatures:
            print("Town are defending " +  town_creatures(creature) + " from creature")

    def put_creatures_on_new_week(self):
        for creature in all_barracks_creature_get:
            if creature in all_barracks_creature_num:
                all_barracks_creature_num[creature] = all_barracks_creature_num[creature] + all_barracks_creature_get[creature]
                print("Creature "+ creature + " has gain "+str(all_barracks_creature_get[creature]) + " and now there are availible " +str(all_barracks_creature_num[creature]) )


all_barracks_creature_price = {'barracks_creature_10':100,'barracks_creature_20':300,'barracks_creature_30':500,'barracks_creture_40':700}
all_barracks_creature_num = {'barracks_creature_10':10,'barracks_creature_20':8,'barracks_creature_30':5,'barracks_creture_40':2}
all_barracks_creature_get = {'barracks_creature_10':20,'barracks_creature_20':10,'barracks_creature_30':4,'barracks_creture_40':3}

all_buildings={'hall_1':0,'hall_2':2500,'hall_3':5000,'hall_4':10000,'barracks_type_1':1500,
                'barracks_type_2':2500,'barracks_type_3':3500,'barracks_type_4':4500,'mage_guild_lvl_1':2000,
                'mage_guild_lvl_2':4000,'mage_guild_lvl_3':6000,'mage_guild_lvl_4':8000,'market_1':1000,
                "tavern_1":1000,'fort_1':2000,'fort_2':3000,'fort_3':5000}
all_spells = ["poke_1","wind_arrow_1","fire_arrow_2","ice_arrow_2","earth_arrow_2","lava_hit_3"]

town_defending_creatures = {}


print("TOWER ###################################")
#test for building in order and out of order of same building

has_spells=[]
has_buildings=["village_hall","barracks_type_1","hall_1"]
tower = Town(has_buildings, 22000, True, False, "Solmyr")
tower.enter_town()
#tower.build_building("barracks_type_2")
#tower.buy_creatures("barracks_creature_10",5)
#tower.buy_creatures("barracks_creature_10",2)
#tower.buy_creatures("barracks_creature_10",5)
tower.put_creatures_on_new_week()
#tower.build_building("barracks_type_4")
#tower.build_building("barracks_type_3")
#tower.build_building("barracks_type_4")
#tower.build_building("mage_guild_lvl_1")
#tower.build_building("mage_guild_lvl_2")
#tower.build_building("mage_guild_lvl_4")
#tower.build_building("mage_guild_lvl_3")
#tower.build_building("mage_guild_lvl_4")
#tower.build_building("fort_1")
#tower.build_building("fort_3")
#tower.build_building("fort_2")
#tower.build_building("fort_3")
#tower.build_building("market_1")
#tower.build_building("tavern_1")
tower.buy_spellbook()


print("RAMPART ###################################")
#necro_buildings=["barracks1", "skeleton_transformer",]
#necro = Town(necro_buildings,350,True,False)
#necro.enter_town()
#necro.new_building("barracks2")


print("CASTLE ###################################")
#castle_buildings=["barracks1","barracks2"]
#castle = Town(castle_buildings,3000,True,False)
#castle.enter_town()
#castle.new_building("barracks2")
#castle.new_building("barracks3")
#castle.buy_spellbook()
