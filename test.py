import os
from appium import webdriver
import time

web_contexts=[]

desired_caps={}

desired_caps['platformName']='Android'

#this is the android version you want to target- this should match the android version in the device
desired_caps['platformVersion']='6.0.1'

desired_caps['deviceName']='samsung'

desired_caps['app']=os.path.join('path/of/your/apk')

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#now locate the elements using chrome inspect 

#switches context to webview since Appium cannot work with webview

print(driver.current_context)

web_contexts = driver.contexts

# it would print NATIVE_APP, WEBVIEW_com.app.destimoney

webview = web_contexts[1]

driver.switch_to.context('WEBVIEW_com.app.destimoney')

print(driver.current_context)

#just a test to see an element is displayed
print(driver.find_element_by_css_selector('.title').is_displayed())

#clicks on skip button on splash screen once
driver.find_element_by_xpath('//span[contains(text(),"Skip")]').click()
#clicks on Next button on splash screen once
# driver.find_element_by_xpath('//span[contains(text(),"Next")]').click()
#
# time.sleep(5)
#
# driver.find_element_by_xpath('//span[contains(text(),"Next")]').click()
#
# time.sleep(1)
#
# driver.find_element_by_xpath('//span[contains(text(),"Next")]').click()

# time.sleep(1)

driver.find_element_by_id("login_btn").click()

# signup

# driver.find_element_by_xpath('//*[@class="text-input text-input-md"]').send_keys("akanksha")
#
# time.sleep(1)
#
# driver.find_element_by_xpath('(//*[@class="text-input text-input-md"])[2]').send_keys("ak")
# time.sleep(1)
#
# driver.find_element_by_xpath('(//*[@class="text-input text-input-md"])[3]').send_keys("verma")
# time.sleep(1)
#
# driver.find_element_by_xpath('(//*[@class="text-input text-input-md"])[4]').send_keys("id")
# time.sleep(1)
#
# driver.find_element_by_xpath('(//*[@class="text-input text-input-md"])[5]').send_keys("123455677")
# time.sleep(1)
#
# driver.find_element_by_xpath('(//*[@class="text-input text-input-md"])[6]').send_keys("111111")
# time.sleep(1)

# driver.find_element_by_class_name("item-cover disable-hover item-cover-md item-cover-default item-cover-default-mdcheckbox-icon").click()
# time.sleep(3)
# driver.find_element_by_id("undefined").click()
#
# driver.find_element_by_xpath('//span[contains(text(),"Sign Up")]').click()
#
# time.sleep(10)
# for otp
# driver.find_element_by_class_name("pinbox input input-md ng-pristine ng-valid ng-touched").send_keys("4")
# # driver.find_element_by_xpath('(//*[@class="item item-block item-md item-input item-input-disabled ng-untouched ng-pristine ng-valid"])[1]').send_keys("111111")

# driver.find_element_by_id("login_btn").click()
time.sleep(5)

# google sign in
driver.find_element_by_xpath('//span[contains(text(),"Google")]').click()
time.sleep(10)
# driver.find_elements_by_css_selector('[ng-reflect-name="menu"]').click()
driver.find_elements_by_css_selector("ion-icon.icon.icon-md.ion-md-menu").click()
time.sleep(10)
# driver.find_elements_by_css_selector('div[class="button-effect"]').click()
# driver.quit()
