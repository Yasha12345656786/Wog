def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    try:
        file = open('Scores.txt', 'r+')
        data = file.read()
        print(f"Your Score:{data}")
        file = open('Scores.txt', 'a')
        file.write(f"{points_of_winning}")
        file.close()
        print("Your Score Was Saved")
    except FileNotFoundError:
        file1 = open('Scores1.txt', 'a')
        file1.write(f"{points_of_winning}")
        file1.close()
        print("Your Score Was Saved")
