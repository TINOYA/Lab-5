import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def get_fox_image():
    response = requests.get('https://randomfox.ca/floof/')
    fox_json = response.json()
    image_url = fox_json['image']
    image_response = requests.get(image_url)
    image_data = BytesIO(image_response.content)
    img = Image.open(image_data)
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

root = tk.Tk()
root.title("Генератор картинок")

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Сгенерировать картинку", command=get_fox_image)
button.pack(pady=10)

label = tk.Label(root)
label.pack()

get_fox_image()  

root.mainloop()