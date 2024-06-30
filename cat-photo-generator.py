import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def fetch_cat_photo():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data[0]['url']
        display_cat_photo(image_url)
    else:
        print("Failed to fetch cat photo")

def display_cat_photo(url):
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((400, 400), Image.LANCZOS)  
    img_tk = ImageTk.PhotoImage(img)

    label.config(image=img_tk)
    label.image = img_tk

root = tk.Tk()
root.title("Random Cat Photo Generator")
root.geometry("500x500")

label = tk.Label(root)
label.pack(pady=20)

button = tk.Button(root, text="Get Random Cat Photo", command=fetch_cat_photo)
button.pack(pady=20)

root.mainloop()
