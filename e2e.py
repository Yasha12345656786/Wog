from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.get("http://127.0.0.1:5000")
score = dr.find_element(by="id", value="score")
if score => 1
