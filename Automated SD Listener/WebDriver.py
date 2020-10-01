######################################################
#                                                    #
#             Automated SD Restore Editor            #
#                                                    #
######################################################

import DataGrab, time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument('--allow-running-insecure-content')

driver = webdriver.Chrome('chromedriver.exe', options=options)

def frame_switch(frame_name):
    driver.switch_to.frame(driver.find_element_by_name(frame_name))

def LoginToServiceDesk(username, password, first_time = False):
    driver.get('http://sd.appriss.com/CAisd/pdmweb.exe')
    usernameTextBox = driver.find_element_by_id('USERNAME')
    usernameTextBox.send_keys(username)
    passwordTextBox = driver.find_element_by_id('PIN')
    passwordTextBox.send_keys(password)
    loginButton = driver.find_element_by_id('imgBtn0').click()
    if first_time:
        time.sleep(3)
        frame_switch('product')
        frame_switch('tab_2001')
        frame_switch('role_main')
        frame_switch('scoreboard')
        queues = driver.find_element_by_name('nodeImg27').click()
        time.sleep(3)
        driver.switch_to.default_content()
        frame_switch('product')
        frame_switch('tab_2001')
        frame_switch('role_main')
        frame_switch('cai_main')
        export_incidents_button = driver.find_element_by_id('imgBtn4').click()

def OpenIncident(incident):
    global original_window, incident_window
    
    frame_switch('gobtn')
    selection_box = Select(driver.find_element_by_id('ticket_type'))
    selection_box.select_by_value('go_in')
    incident_searchbox = driver.find_element_by_name('searchKey')
    incident_searchbox.send_keys(incident)
    search_button = driver.find_element_by_id('imgBtn0')
    original_window = driver.window_handles[0]
    search_button.click()
    incident_window = driver.window_handles[1]
    driver.switch_to.window(incident_window)

def GrabIncidentInformation(username, password):
    frame_switch('cai_main')
    try:
        vine3 = driver.find_element_by_id('df_7_2').text
        CI = driver.find_element_by_xpath('//*[@id="df_2_2"]/span').text
    except NoSuchElementException:
        time.sleep(3)
        vine3 = driver.find_element_by_id('df_7_2').text
        CI = driver.find_element_by_xpath('//*[@id="df_2_2"]/span').text
    if vine3 == "Yes":
        driver.close()
        driver.switch_to.window(original_window)
    else:
        if CI[-4:].lower() == 'data':
            Organization = driver.find_element_by_xpath('//*[@id="df_2_1"]/span').text
            if Organization[-3:].lower() == "vpo":
                DataGrab.grab_vpo(Organization, CI)
            else:
                DataGrab.grab_ae(username, password)
                DataGrab.grab_dfr(username, password)
        elif CI[-3:].lower() == 'rms':
            print("Only VPOs are implemented\n")
        else:
            print("Not a ticket for data, and only VPOs are implemented\n")
        driver.close()
        driver.switch_to.window(original_window)
    return vine3

def Finish():
    driver.close()
