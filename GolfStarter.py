def read_file(filename):
    golfer_ids = []
    player_names = []
    par_score = []
    rounds = []
    cut_status = []

    file = open(filename, 'r')

    for line in file:
        line = line.strip()
        parts = line.split(',')

        golfer_ids.append(int(parts[0]))
        player_names.append(parts[1])
        par_score.append(int(parts[2]))
        rounds.append(int(parts[3]))
        cut_status.append(int(parts[4]))

    file.close()

    return golfer_ids, player_names, par_score, rounds, cut_status



def main():
    filename = "golf_masters.txt"
    golfer_ids, player_names, par_score, cut_status = read_file(filename)
    choice = ""
    while choice != "8":
        print("\nMenu")
        print("1. View Leaderboard")
        print("2. Delete a player")
        print("3. Add a new player")
        print("4. Update cut status")
        print("5. Placeholder for Exam")
        print("6. Placeholder for Exam")
        print("7. Placeholder for Exam")
        print("8. Quit and save")
        choice = input("Enter choice: ")
        if choice == "1":# display leader board

        elif choice == "2":# delete a player

        elif choice == "3":# add a new player

        elif choice == "4":# update cut status

        elif choice == "5":# TODO in exam

        elif choice == "6":# TODO in exam

        elif choice == '7':# TODO in exam

        elif choice == "8":# save data and quit
            print("Data saved. Goodbye.")
        else:
            print("Invalid choice.")


if __name__ == '__main__':
main()
