from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert '홈 화면' in browser.title

browser.quit()
