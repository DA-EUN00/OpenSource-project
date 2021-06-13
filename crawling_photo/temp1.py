from selenium import webdriver
from bs4 import BeautifulSoup as soups

def search_selenium(search_name, search_path, search_limit) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    
    browser = webdriver.Chrome('C:/Users/충북대학교/Downloads/chromedriver_win32/chromedriver.exe') #webdriver 위치
    browser.get(search_url)
    
    image_count = len(browser.find_elements_by_tag_name("img"))
    print("로드된 이미지 개수 : ", image_count)

    browser.implicitly_wait(2)

    for i in range( search_limit ) :
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot("C:/crawling_photo/일몰/일몰7" + str(i) + ".jpg") #사진 저장 위치

    browser.close()

if __name__ == "__main__" :

    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    search_path = "Your Path"
    # search_maybe(search_name, search_limit, search_path)
    search_selenium(search_name, search_path, search_limit)