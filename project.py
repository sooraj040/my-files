# Football Team Management System (Python)
players = []

# Add Player
def add_player():
    name = input("Enter Player Name: ")
    position = input("Enter Position: ")
    club = input("Enter club name: ")
    goals = int(input("Enter Goals Scored: "))

    player = {
        "name": name,
        "position": position,
        "goals": goals,
        "club": club
    } 
    players.append(player)
    print("\nPlayer Added Successfully!\n")

# View Players
def view_players():
    if len(players) == 0:
        print("\nNo Players Found!\n")
        return

    print("\n----- PLAYER LIST -----")
    for i, player in enumerate(players, start=1):
        print(f"{i}. name: {player['name']} | position: {player['position']} | club: {player['club']} | Goals: {player['goals']}")
    print()

# Search Player
def search_player():
    search_name = input("Enter Player Name to Search: ")
    found = False
    for player in players:
        if player["name"].lower() == search_name.lower():
            print("\nPlayer Found!")
            print("Name:", player["name"])
            print("Position:", player["position"])
            print("Club:", player["club"])
            print("Goals:", player["goals"])
            found = True
            break
    if not found:
        print("\nPlayer Not Found!\n")

# Search Club
def search_club():
    search_club = input("Enter club name to search: ")
    matching_players = [p for p in players if p["club"].lower() == search_club.lower()]
    if matching_players:
        print("Club:", matching_players[0]["club"])     
        print("Players in this club:")      
        for i, player in enumerate(matching_players, start=1):
            print(f"{i}. {player['name']}")
    else:
        print("\nClub not found")


# Update Goals
def update_goals():
    name = input("Enter Player Name: ")
    for player in players:
        if player["name"].lower() == name.lower():
            new_goals = int(input("Enter New Goal Count: "))
            player["goals"] = new_goals
            print("\nGoals Updated Successfully!\n")
            return
    print("\nPlayer Not Found!\n")

# Top Scorer
def top_scorer():
    if len(players) == 0:
        print("\nNo Players Available!\n")
        return
    top = max(players, key=lambda x: x["goals"])
    print("\n----- TOP SCORER -----")
    print("Name:", top["name"])
    print("Position:", top["position"])
    print("Club:", top["club"])
    print("Goals:", top["goals"])
    print()

# Delete Player
def delete_player():
    name = input("Enter Player Name to Delete: ")
    for player in players:
        if player["name"].lower() == name.lower():
            players.remove(player)
            print("\nPlayer Removed Successfully!\n")
            return
    print("\nPlayer Not Found!\n")

# Total Players
def total_players():
    print("Total players:", len(players))

# Main Menu
while True:
    print("FOOTBALL TEAM MANAGEMENT SYSTEM")
    print("1. Add Player")
    print("2. View Players")
    print("3. Search Player")
    print("4. Update Goals")
    print("5. Show Top Scorer")
    print("6. Delete Player")
    print("7. Total players")
    print("8. Search club")
    print("9. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        while True:
            add_player()
            more = input(
                "\nDo you want to add more?\n"
                "if yes then type YES\n"
                "if no then type NO\n"
                "type: "
            )
            if more.lower() not in ["yes", "y"]:
                break

    elif choice == "2":
        view_players()

    elif choice == "3":
        search_player()

    elif choice == "4":
        update_goals()

    elif choice == "5":
        top_scorer()

    elif choice == "6":
        delete_player()

    elif choice == "7":
        total_players()
    
    elif choice == "8":
        search_club()

    elif choice == "9":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
     