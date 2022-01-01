import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from PIL import Image
import pandas as pd

from ekstraksi_fitur import ekstrak
from knn import predict_knn


class Utama():
    def __init__(self):

        self.win = tk.Tk()
        # self.win.geometry('1280x720')
        self.win.title('KNN')
        self.win.resizable(False, False)
        self.win.configure(bg='#DFD3C3')

        self.tit = tk.Label(text="Klasifikasi Penyakit Jagung melalui Citra Daun Menggunakan Algoritma KNN🌽",
                            padx=25, pady=6, font=("", 12), bg='#DFD3C3').pack()

        self.canvas = tk.Canvas(height=720, width=1280, bg='#F0ECE3')
        self.canvas.pack()

        self.frame1 = tk.Frame(self.canvas, bg='#F0ECE3')
        self.frame1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        self.img = tk.Canvas(self.frame1, height=512, width=512,)
        # self.img.create_rectangle(100, 100, 400, 400)
        self.img.pack(side=tk.LEFT)
        self.img.bind("<Double-Button-1>", self.load_img)

        self.img.create_text(256, 256, text='Image')

        self.text = tk.Text(self.frame1, width=40, height=30)
        self.text.pack(side=tk.RIGHT)

        self.chose_image = tk.Button(text='Choose Image',
                                     padx=35, pady=10,
                                     fg="white", bg="#A68DAD", command=self.load_img)
        self.chose_image.pack(side=tk.LEFT)

        self.neighbors_label = tk.Label(
            text="k_neighbor : ", padx=10, font=("", 12), bg='#DFD3C3')
        self.neighbors_label.pack(side=tk.LEFT)

        self.k = tk.IntVar(value=5)
        self.name_entry = tk.Entry(textvariable=self.k,
                                   font=('calibre', 10, 'normal'))
        self.name_entry.pack(side=tk.LEFT)

        self.class_image = tk.Button(text='Classify Image',
                                     padx=35, pady=10,
                                     fg="white", bg="#A68DAD", command=self.classify)
        self.class_image.pack(side=tk.RIGHT)

        self.win.mainloop()

    def load_img(self):
        if os.path.isfile('trash/file.png'):
            os.remove('trash/file.png')
        self.tempFile = filedialog.askopenfilename(
            initialdir="/", title="Select File", filetypes=(("all files", "*.*"), ("png files", "*.png")))
        print(self.tempFile)
        im = Image.open(self.tempFile)
        im = im.resize((512, 512), Image.ANTIALIAS)
        im.save(f'trash/file.png')
        self.myPic = tk.PhotoImage(file='trash/file.png')
        self.img.delete("all")
        self.img.create_image(260, 260, image=self.myPic)

    def classify(self):
        train = pd.read_csv("train.csv")
        test = ekstrak([self.tempFile])

        preds, y_test, X_test = predict_knn(train, test, self.k.get())

        self.text.delete('1.0', tk.END)

        file_name = self.tempFile.split('/')
        self.text.tag_configure('medium', font=(
            'Verdana', 16, 'bold'))
        self.text.insert(tk.END, '\n \n File : \n' + '   ' + str(
            file_name[len(file_name)-1]).upper() + '\n \n')

        self.text.insert(tk.END, ' Feature : \n')
        for label in X_test.columns:
            self.text.insert(
                tk.END, ('   ' + str(label) + ' : ' + str(X_test[label][0]) + '\n'))
        self.text.insert(tk.END, '\n \n \n \n')
        self.text.tag_configure('big', font=(
            'Verdana', 20, 'bold'), justify='center')
        self.text.insert(tk.END, preds[0], 'big')


if __name__ == "__main__":
    Utama()
    sys.exit()
