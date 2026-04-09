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

def view_leaderboard(ids, names, scores, rounds, cuts):
    print("\n# Player                Par Round Status")

    for i in range(len(ids)):
        if scores[i] > 0:
            par = "+" + str(scores[i])
        else:
            par = str(scores[i])

        if cuts[i] == 1:
            status = "\U0001F601"
        else:
            status = "\U00002369\U0000FE0F"

        print(ids[i], names[i], par, rounds[i], status)

def delete_player(ids, names, scores, rounds, cuts):
    delete_id = int(input("ENter Golfer ID: "))

    if delete_id in ids:
        index = ids.index(delete_id)

        ids.pop(index)
        names.pop(index)
        scores.pop(index)
        rounds.pop(index)
        cuts.pop(index)

        print("Player Deleted!")
    else:
        print("ID not found!")#

def add_player(ids, names, scores, rounds, cuts):
    new_id = int(input("Enter new Golfer ID: "))
    if new_id in ids:
        print("ID already exists!")
    else:
        name = input("Enter new name: ")
        score = int(input("Enter score: "))

        ids.append(new_id)
        names.append(name)
        scores.append(score)
        rounds.append(2)
        cuts.append(1)

        print("Player Added.")

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
