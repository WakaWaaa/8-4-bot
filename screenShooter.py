import discord
import pyautogui
import PIL
import tkinter as tk

root = tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

scrheight = root.winfo_screenheight()
scrwidth = root.winfo_screenwidth()

path = "D:\very cool programing projects\Discord\8-4 bot\screenshots\screenshot.png"

def screenShot():
    myScrnSht = pyautogui.screenshot(region = (0,0,scrwidth, scrheight/10))
    myScrnSht.save(r'D:\very cool programing projects\Discord\8-4 bot\screenshots\screenshot.png')
    root.destroy()

b = tk.Button(text = "Screenshot", command = screenShot)
b.pack()
root.mainloop()