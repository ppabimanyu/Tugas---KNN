
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import pandas as pd
from ekstraksi_fitur import ekstrak
from knn import predict_knn


def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                            filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 150
    img = Image.open(image_data)
    print(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    file_name = image_data.split('/')
    panel = tk.Label(frame, text=str(
        file_name[len(file_name)-1]).upper()).pack()
    panel_image = tk.Label(frame, image=img).pack()


def classify():
    train = pd.read_csv("train.csv")
    test = ekstrak([image_data])

    preds, y_test, X_test = predict_knn(train, test, k.get())

    for label in X_test.columns:
        result = tk.Label(frame, text=str(label) + ' : ' +
                          str(X_test[label][0])).pack()

    table = tk.Label(
        frame, text=preds[0]).pack()


root = tk.Tk()
root.title('KNN')
# root.iconbitmap('class.ico')
root.resizable(False, False)

tit = tk.Label(root, text="Klasifikasi Penyakit Jagung melalui Citra Daun Menggunakan Algoritma KNN🌽",
               padx=25, pady=6, font=("", 12)).pack()

canvas = tk.Canvas(root, height=720, width=1280, bg='grey')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

chose_image = tk.Button(root, text='Choose Image',
                        padx=35, pady=10,
                        fg="white", bg="grey", command=load_img)
chose_image.pack(side=tk.LEFT)

neighbors_label = tk.Label(root, text="n_neighbor : ", padx=10, font=("", 12))
neighbors_label.pack(side=tk.LEFT)

k = tk.IntVar(value=5)
name_entry = tk.Entry(root, textvariable=k,
                      font=('calibre', 10, 'normal'))
name_entry.pack(side=tk.LEFT)

class_image = tk.Button(root, text='Classify Image',
                        padx=35, pady=10,
                        fg="white", bg="grey", command=classify)
class_image.pack(side=tk.RIGHT)

root.mainloop()
