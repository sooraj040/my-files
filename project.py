players = []
choice = ""

while choice != "4":
    print("\nFootball Team Manager")
    print("1. Add player")
    print("2. View players")
    print("3. Top scorer")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        position = input("Position: ")
        club = input("Club: ")
        goals = int(input("Goals scored: "))
        players.append([name, position, club, goals])
        print("Player added.")
    elif choice == "2":
        if len(players) == 0:
            print("No players found.")
        else:
            for i in range(len(players)):
                print(i + 1, ".", players[i][0], "|", players[i][1], "|", players[i][2], "|", players[i][3], "goals")
    elif choice == "3":
        if len(players) == 0:
            print("No players found.")
        else:
            top_scorer = players[0]
            for player in players:
                if player[3] > top_scorer[3]:
                    top_scorer = player
            print("Top scorer:", top_scorer[0], "with", top_scorer[3], "goals")
    elif choice == "4":
        print("Thank you!")
    else:
        print("Invalid choice.")
