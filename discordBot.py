import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Screenshot import Screenshot_Clipping

# Load bot token key
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

description = ''' Bot to take full page screenshots '''
bot = commands.Bot(command_prefix="!", description=description)


def get_full_screenshot(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("window-size=1920,1080")

    browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    browser.get(url)

    screen = Screenshot_Clipping.Screenshot()
    screen.full_Screenshot(browser, save_path=r'.', image_name='screenshot.png')

    browser.quit()


@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print("has connected to Discord")


@bot.command()
async def fss(ctx, url):
    await ctx.send("You got it")
    get_full_screenshot(url)
    await ctx.send(file=discord.File("screenshot.png"))


@fss.error
async def fss_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("I need an url")


bot.run(TOKEN)