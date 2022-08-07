# haircut battle
import time
A = input("Player 1 Name: ")
B = input("Player 2 Name: ")
# A = "Player 1"
# B = "Player 2"

plr = [
    {
        "name": A,
        "haircut": 100,
        "turn": False,
    },
    {
        "name": B,
        "haircut": 100,
        "turn": False,
    } 
]

# infinite loop
while True:
    # print(plr)
    # print(plr[0]["name"])
    # print(plr[1]["name"])
    # print(plr[0]["haircut"])
    # print(plr[1]["haircut"])
    # print(plr[0]["turn"])
    # print(plr[1]["turn"])
    # print("\n")
    # print("\n")
    # print("\n")
    # print("\n")
    
    print("\n")
    print("{}'s haircut: {}".format(plr[0]["name"], plr[0]["haircut"]))
    print("{}'s haircut: {}".format(plr[1]["name"], plr[1]["haircut"]))
    print("\n")
    plr[0]["haircut"] = plr[0]["haircut"] - 1
    plr[1]["haircut"] = plr[1]["haircut"] - 1
    if plr[1]["haircut"] <= 0:
        print("Player 1 wins")
        break
    time.sleep(1)
    if plr[0]["haircut"] <= 0:
        print("Player 2 wins")
        break
    time.sleep(1)
    plr[0]["turn"] = True

    time.sleep(1)
    print("""
    Player 1 turn
    - Q = attack player 2
    - E = defend
    - C = nothing
    """)

    spr = input(""+plr[0]["name"]+": ")
    pr = spr.upper()
    if pr == "Q":
        plr[1]["haircut"] -= 5
    elif pr == "E":
        plr[1]["haircut"] += 5
    elif pr == "C":
        plr[1]["haircut"] += 0
    else:
        print("Invalid input")

    print("\n")
    print("{}'s haircut: {}".format(plr[0]["name"], plr[0]["haircut"]))
    print("{}'s haircut: {}".format(plr[1]["name"], plr[1]["haircut"]))
    print("\n")

    if plr[1]["haircut"] <= 0:
        print("Player 1 wins")
        break
    time.sleep(1)
    if plr[1]["haircut"] <= 0:
        print("Player 2 wins")
        break
    time.sleep(1)
    plr[0]["turn"] = False

    plr[1]["turn"] = True
    print("""
    Player 2 turn
    - Q = attack player 1
    - E = defend
    - C = nothing
    """)
    spr2 = input(""+plr[1]["name"]+": ")
    pr2 = spr2.upper()
    if pr2 == "Q":
        plr[0]["haircut"] -= 5
    elif pr2 == "E":
        plr[0]["haircut"] += 5
    elif pr2 == "C":
        plr[0]["haircut"] += 0
    else:
        print("Invalid input")
    plr[1]["turn"] = not plr[1]["turn"]
    time.sleep(1)
