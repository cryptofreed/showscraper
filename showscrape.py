from selenium import webdriver
import pandas as pd

url = 'https://thewhittierbar.com'

driver = webdriver.Chrome()
driver.get(url)
shows = driver.find_elements_by_class_name('jsx-3895292772 eaec-grid-item-component')

show_list = []

for show in shows:
    title = show.find_element_by_xpath('//*[@id="eapps-events-calendar-1afa4088-3079-4322-8965-4b21c0b46d85"]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[1]').text
    show_item = {
        'title': title
    }
    show_list.append(show_item)

df = pd.DataFrame(show_list)
print(df)



# class="eaec-grid-item"
# title //*[@id="eapps-events-calendar-1afa4088-3079-4322-8965-4b21c0b46d85"]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[1]
# time //*[@id="eapps-events-calendar-1afa4088-3079-4322-8965-4b21c0b46d85"]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/div/div
# month //*[@id="eapps-events-calendar-1afa4088-3079-4322-8965-4b21c0b46d85"]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[1]
# day //*[@id="eapps-events-calendar-1afa4088-3079-4322-8965-4b21c0b46d85"]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[2]
# note: program that sorts info from .ics/google cal files rather than scraping website
