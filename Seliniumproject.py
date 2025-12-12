import time
import selenium.webdriver as webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getbtn(Xpt):
    btn = wait.until(EC.visibility_of_element_located((By.XPATH,Xpt)))
    return btn
def gettext(Xpt):
    txt = wait.until(EC.visibility_of_element_located((By.XPATH,Xpt))).text
    return txt
buttonXpathsDB = { "englishBtnXpath" : "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]",
                   "cookitbtnXpath":"/html/body/div[2]/div[2]/div[15]/div[8]/button",
                   "currentCookieScore":"/html/body/div[2]/div[2]/div[15]/div[4]",
                   "cursorPrice":"/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[2]/div[3]/span[2]",
                   "cursorBtn":"/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[2]"}


browser = uc.Chrome()
wait  = WebDriverWait(browser,50)
browser.get("https://orteil.dashnet.org/cookieclicker/")
englishbtn = getbtn(buttonXpathsDB["englishBtnXpath"]).click()
time.sleep(5)
cookitbtn = getbtn(buttonXpathsDB["cookitbtnXpath"])
while True:
    cookitbtn.click()
    cookitbtn.click()
    cookitbtn.click()
    cookitbtn.click()
    cookitbtn.click()
    cookitbtn.click()

    currentCooki = gettext(buttonXpathsDB["currentCookieScore"]).split(" ")[0]
    cursorPrice = gettext(buttonXpathsDB["cursorPrice"]).split(" ")[0]
    try:
        currentCooki  = currentCooki.replace(",","")
        cursorPrice = cursorPrice.replace(",","")
    except:
        pass
    currentCooki = int(currentCooki)
    cursorPrice = int(cursorPrice)
    if currentCooki>=cursorPrice:
        getbtn(buttonXpathsDB["cursorBtn"]).click()

time.sleep(500)
browser.quit()
