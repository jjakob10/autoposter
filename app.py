from instabot import Bot
import os
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])
bot = Bot()

bot.login(username="test.page.robson", password="Robson")

image = "img/1.jpg"

bot.upload_photo(image, caption="Test 1111111 Hello people")
