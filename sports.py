players = [{"name": "Xavier Worthy", "position": "WR", "number": "1", "touchdowns": 3, "yards": 48}, 
           {"name": "Wanya Morris","position": "OT","number": "64", "touchdowns": 0, "yards": 98}, 
           {"name": "Trey Smith","position": "G","number": "65", "touchdowns": 7, "yards": 102}]

positions = []

for i in players:
    positions.append(i["position"])

joinedPos = ", ".join(positions)
print(f"The players positions are: {joinedPos}")

xavier = players[0]
xavier["touchdowns"] = 10

print(f"Xavier scored a total of {xavier["touchdowns"]} touchdowns.")

totalTouchdowns = 0
for i in players:
    totalTouchdowns += i["touchdowns"]

avgTouchdowns = totalTouchdowns / 3
print(f"The average number of touchdowns was: {avgTouchdowns}")

totalYards = 0
for i in players:
    totalYards += i["yards"]

avgYards = totalYards / 3
print(f"The average number of yards gaines was: {avgYards}")

