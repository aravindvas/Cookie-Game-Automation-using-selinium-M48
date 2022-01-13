from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

urLL = "http://orteil.dashnet.org/experiments/cookie/"

chr_drvr = "D:\Softwares\chromedriver_win32\chromedriver.exe"
drvr = webdriver.Chrome(executable_path=chr_drvr)

drvr.get(url=urLL)

cok = drvr.find_element_by_id("cookie")

itm = drvr.find_elements_by_css_selector("#store div")
itm_id = [i.get_attribute("id") for i in itm]

tmout = time.time() + 10
fv_min = time.time() + 60*5

while True:
    cok.click()
    if time.time() > tmout :
        allp = drvr.find_elements_by_css_selector("#store b")
        itm_pr = []

        for j in allp:
            txt = j.text
            if txt != "":
                cost = int(txt.split("-")[1].strip().replace(",",""))
                itm_pr.append(cost)
        upgd = {}
        for n in range(len(itm_pr)):
            upgd[itm_pr[n]] = itm_id[n]
        money = drvr.find_element_by_id("money").text
        if ","  in money:
            money = money.replace(",","")
        cook_cnt = int(money)

        afford_upgd = {}
        for cst,idd in upgd.items():
            if cook_cnt > cst:
                afford_upgd[cst] = idd

        hst_pr = max(afford_upgd)
        print(hst_pr)
        to_purch = afford_upgd[hst_pr]

        drvr.find_element_by_id(to_purch).click()

        tmout = time.time() + 10

    if time.time() > fv_min:
        ckpersec = drvr.find_element_by_id("cps").text
        print(f"cookie / sec :{ckpersec}")
        break


# drvr.close()
# drvr.quit()