class Turn():

    def __init__(self,number_of_players,player_name,resources,mines):
        self.number_of_players = number_of_players
        self.player_name = player_name
        self.resources = resources
        self.mines = mines


    def new_player_turn(self):
        print(self.player_name + " turn!")
        turn_counter+=1


    def end_player_turn(self):
         new_day()

    def new_day(self):
        turn_counter = 0
        gain_resources()

    def gain_resources(self):
        for mine in self.mines:
            if mine == "gold_mine":
                resource_income = self.mines[mine] * 1000 #hardcode 1000 gold per day
                self.resources["gold"]+= resource_income
                print(self.player_name + " player has "+str(self.resources["gold"]) + " gold.")
            if mine == "wood_mine":
                resource_income = self.mines[mine] * 2 #hardcode 2 wooda
                self.resources["wood"]+= resource_income
                print(self.player_name + " player has "+str(self.resources["wood"]) + " wood.")
            if mine == "ore_mine":
                resource_income = self.mines[mine] * 2 #hardcode 2 ore
                self.resources["ore"]+= resource_income
                print(self.player_name + " player has "+str(self.resources["ore"]) + " ore.")



print("Player1 ###################################")
number_of_players = 4



player_name="Nick"
resources={"gold":1000, "wood":10,"ore":5}
mines={"gold_mine":1,"wood_mine":1,"ore_mine":1}
player1 = Turn(number_of_players,player_name,resources,mines)
player1.gain_resources()



print("Player2 ###################################")
player_name="Jack"
resources={"gold":3000, "wood":4,"ore":3}
mines={"gold_mine":0,"wood_mine":2,"ore_mine":3}
player2 = Turn(number_of_players,player_name,resources,mines)
player2.gain_resources()
player2.gain_resources()
player2.gain_resources()
