import telebot, selenium, time, simplejson
from selenium import webdriver

bot = telebot.TeleBot('Telegram Bot Token')
cookies = simplejson.load(open('cookies.json', 'rb'))

antiduplicate = []

driver = webdriver.Edge('msedgedriver.exe')
print('Loading lolz.guru')

driver.get('https://lolz.guru/chatbox')

start_time = time.time() 
for cookie in cookies:
    driver.add_cookie(cookie)

if time.time() - start_time >= 1:
    driver.close()
    input('Failed to import cookies. Took a long time: %s seconds' % (time.time() - start_time))
    quit()
else:
    print("Cookies successfully imported in %s seconds" % (time.time() - start_time))

print('Parsing new messages from chat lolz.guru')

time.sleep(1)

for first_run in driver.find_elements_by_xpath("//*[starts-with(@id, 'chatboxMessage_')]/span[2]/div"):
    antiduplicate.append(first_run)
for first_run in driver.find_elements_by_xpath("//*[starts-with(@id, 'chatboxMessage_')]/span[2]/a"):
    antiduplicate.append(first_run)
 
while True:
    for message in driver.find_elements_by_xpath("//*[starts-with(@id, 'chatboxMessage_')]/span[2]/div"):
        for username in driver.find_elements_by_xpath("//*[starts-with(@id, 'chatboxMessage_')]/span[2]/a"):

            if not message in antiduplicate:             
                 if not username in antiduplicate:

                    print(str(username.text)+':', str(message.text))
                    bot.send_message(chat_id=сhat_id, text=f"{str(username.text)}" + ': ' + str(message.text))
        
                    antiduplicate.append(message)
                    antiduplicate.append(username) 

                    print('Size: ', len(antiduplicate), 'Element ID: ', message.id)
   
driver.close()
