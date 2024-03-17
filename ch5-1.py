krozv = {
    "name": "krozv",
    "XP": 1000,
    "team": "A",
}

def create_player(name, xp, team):
    return {
    "name": name,
    "XP": xp,
    "team": team,
    }

def introduce_player(player):
    name = player["name"]
    team = player["team"]
    print(f'Hi, My name is {name} and i play for {team}.')

introduce_player(krozv)