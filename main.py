from tkinter import *
from tkinter import messagebox
import requests


# ---------------------Button function---------------------------------------#

def message_display():
    response = requests.get(url="https://zenquotes.io/api/random")
    response.raise_for_status()
    data = response.json()
    my_quote = data[0]['q']
    messagebox.showinfo(title="Here it is", message=my_quote)


# ---------------------------UI -SETUP -------------------------------------- #
window = Tk()
window.title("Motivate Me")
canvas = Canvas(width=300, height=300)
canvas_images = PhotoImage(file="nu.png")
canvas.create_image(150, 150, image=canvas_images)
canvas.pack()
# button-motivate
motivate_button = Button(text="Motivate me pls", command=message_display)
motivate_button.pack()

window.mainloop()
