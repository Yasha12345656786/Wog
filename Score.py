def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    file = open('Scores.txt','a')
    file.write(f"{points_of_winning}")
    file.close()
    print("Your Score Was Saved")


