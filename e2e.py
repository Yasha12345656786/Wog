from selenium import webdriver
from time import sleep


def test_score_service():
    dr = webdriver.Chrome()
    current_score=0
    try:
        dr.get("http://127.0.0.1:5000")
        score_obj = dr.find_element(by="id", value="score")
        txt = score_obj.text
        scores_string_arr = txt.split("\n")
        for item in scores_string_arr:
            score = int(item.split(": ")[-1])
            current_score = score
            if current_score < 1 or current_score > 1000:
                assert False
    except AssertionError as score:
        print(f"The Score {current_score} Is Invalid")
    finally:
        dr.close()


test_score_service()
