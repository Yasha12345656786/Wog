from selenium import webdriver
from time import sleep

try:
    dr = webdriver.Chrome()
    dr.get("http://127.0.0.1:5000")
    score = dr.find_element(by="id", value="score")
    if int(score) >= 1 or int(score) <= 1000:
        print("true")
except Exception as error:
    print("some error", error)
