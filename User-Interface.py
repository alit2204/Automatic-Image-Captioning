from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import os
import generate
from gtts import gTTS
from playsound import playsound
from tkinter import messagebox

def choose_file():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(("JPG File", ".jpg"), ("PNG file", ".png"), ("All files", "*.")))
    entry1.delete(0, 'end')
    entry1.insert(0,str(filename))
    img = Image.open(filename)
    # resize image to fixed size
    img = img.resize((1000,650))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

root = Tk()
root.title("Image Caption Generator Using Deep Learning")
root.geometry("1980x1080")
root.configure(bg="#F1F1F1")

# Add two images to the left and right
left_image = Image.open("/home/alit2204/Downloads/national-university-logo.png")
left_image = left_image.resize((275, 300))
left_image = ImageTk.PhotoImage(left_image)
left_label = Label(root, image=left_image, bg="#F1F1F1")
left_label.pack(side=LEFT, padx=10, pady=10, anchor=N)

right_image = Image.open("/home/alit2204/Downloads/1709548643490.jpeg")
right_image = right_image.resize((300, 300))
right_image = ImageTk.PhotoImage(right_image)
right_label = Label(root, image=right_image, bg="#F1F1F1")
right_label.pack(side=RIGHT, padx=10, pady=10, anchor=N)

mylabel = Label(root, text=" ", font=("Arial", 30,"bold"), bg="#F1F1F1",wraplength=1000)

def generateCaption(mylabel):
    file_name = entry1.get()
    if not file_name:
        messagebox.showerror("Error", "No file selected")
        return
    try:
        img = Image.open(file_name)
    except:
        messagebox.showerror("Error", "Invalid file selected")
        return
    caption = generate.runModel(file_name)
    mylabel.config(text=caption)

def soundcaption(mylabel):
    file_name = entry1.get()
    if not file_name:
        messagebox.showerror("Error", "No file selected")
        return
    try:
        img = Image.open(file_name)
    except:
        messagebox.showerror("Error", "Invalid file selected")
        return
    caption = generate.runModel(file_name)
    text_to_say = caption
    language = "en"
    gtts_object = gTTS(text=text_to_say, lang=language, slow=False)
    gtts_object.save("./gtts.wav")
    playsound('./gtts.wav')

frm = Frame(root, bg="#F1F1F1", borderwidth=2, relief="solid", highlightbackground="#CCCCCC", highlightthickness=1)
frm.pack(side=BOTTOM, padx=10, pady=10)

lbl = Label(root, bg="#F1F1F1")
lbl.pack()

entry1 = Entry(frm,width =240)

button1 = Button(frm, text="Select Image",command = choose_file, width=25, font=("Open Sans", 14), bg="#008080", fg="#FFFFFF")

button2 = Button(frm, text="Generate Caption", command= lambda : generateCaption(mylabel), width=25, font=("Open Sans", 14), bg="#008080", fg="#FFFFFF")

img = PhotoImage(file="/home/alit2204/Downloads/pngwing.com (2).png")
button3 = Button(frm, image=img, command=lambda: soundcaption(mylabel), width=200, font=("Open Sans", 14), bg="#008080", fg="#FFFFFF")
button3.image = img

entry1.pack(pady=10)
mylabel.pack(pady=10)
button1.pack(pady=10)
button2.pack(padx=10, pady=10)
button3.pack(padx=10, pady=10)

root.mainloop()