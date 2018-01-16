class Mine():
    def __init__(self,mine_type,player_owner,player_mines):
        self.mine_type=mine_type
        self.player_owner=player_owner
        self.player_mines=player_mines

    def get_type(self):
        print("this mine is a : " + self.mine_type)

    def change_owner(self):
        print("this mine is now own by : " + self.player_owner)

        for mine in self.player_mines:
            if mine == self.mine_type:
                self.player_mines[mine]+=1
                print("this player now has " + str(self.player_mines[mine]) + " "+ self.mine_type)

print("mine ###################################")
mine_type = "gold_mine"
player_owner="Nick"
player_mines={"gold_mine":0,"wood_mine":5,"ore_mine":3}
first_gold_mine = Mine(mine_type,player_owner,player_mines)
first_gold_mine.get_type()
first_gold_mine.change_owner()

print("mine ###################################")
first_gold_mine = Mine(mine_type,player_owner,player_mines)
first_gold_mine.get_type()
first_gold_mine.change_owner()

print("mine ###################################")
mine_type = "wood_mine"
first_gold_mine = Mine(mine_type,player_owner,player_mines)
first_gold_mine.get_type()
first_gold_mine.change_owner()

print("mine ###################################")
player_owner="Bart"
player_mines={"gold_mine":11,"wood_mine":11,"ore_mine":11}
mine_type = "gold_mine"
first_gold_mine = Mine(mine_type,player_owner,player_mines)
first_gold_mine.get_type()
first_gold_mine.change_owner()
