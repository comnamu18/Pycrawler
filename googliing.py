#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import excelPy
import crawling

driver = webdriver.Chrome(executable_path="C:\\Users\comna\algoGit\Pycrawler\requirements\chromedriver.exe")
driver.get("http://google.com")
nameList = excelPy.getname_from_excels('KBO_타자.xlsx', 0)
for i in nameList:
    keyword = str(i) + "site : ""http://www.kbreport.com/"""
    elem = driver.find_element_by_id('lst-ib')
    elem.send_keys(keyword)
    elem.submit()
    ##### 구글 검색 결과 페이지 #####
    try:
        box = driver.find_element_by_xpath("//div[@id='rso']/div[2]/div")
        list = box.find_elements_by_tag_name('h3')
        for item in list :
            print(item.text)
            if( 'kbreport' in item.text ):
                p = item.find_element_by_tag_name('a')
                p.click()
                break
    except NoSuchElementException:
        box = driver.find_element_by_xpath("//div[@id='rso']/div/div")
        list = box.find_elements_by_tag_name('h3')
        for item in list:
            print(item.text)
            if ('kbreport' in item.text):
                p = item.find_element_by_tag_name('a')
                p.click()
                break