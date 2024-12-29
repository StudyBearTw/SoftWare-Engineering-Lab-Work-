class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_player_info(self, number):
        for player in self.players:
            if player.number == number:
                return f"{player.name} ({player.position}) - {player.number}"
            return "Player not found"
        
# 測試程式碼
player1 = Player("Chen Jie-Xian", "Outfielders", 24)
player2 = Player("Lin Yu-Min", "Pitchers", 45)
player3 = Player("Lin Chia-Cheng", "Catchers", 27)

team1 = Team("Team Taiwan")
team1.add_player(player1)
team1.add_player(player2)

print(team1.get_player_info(24))  # 應輸出 "Chen Jie-Xian (Outfielders) - 24"
print(team1.get_player_info(45))  # 應輸出 "Lin Yu-Min (Pitchers) - 45"
print(team1.get_player_info(27))  # 應輸出 "Player not found."