global file


def add_score(difficulty):
    global file
    points_of_winning = (difficulty * 3) + 5
    try:
        file = open('Scores.txt', 'r+')
    except FileNotFoundError:
        file = open('Scores.txt', 'a')
    finally:
        data = file.read()
        print(f"Your Score:{data}")
        file = open('Scores.txt', 'a')
        file.write(f"{points_of_winning}\n")
        file.close()
        print("Your Score Was Saved")


add_score(3)
