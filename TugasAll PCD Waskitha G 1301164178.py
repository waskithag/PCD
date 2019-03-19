#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:05:52 2019

@author: waskithag
"""

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


class Root(Tk):
    
    def __init__(self):
        super(Root, self).__init__()
        self.title("PCD Waskitha Ghaziadiyata/1301164178")
        self.minsize(640,400)
        self.labelframe = ttk.LabelFrame(self, text = "Process List")
        self.labelframe.grid(column = 0, row = 1, padx = 20, pady = 20)
        self.buttons("Open", self.fileDialog, 1)
        self.buttons("Grayscale", self.greyscale, 2)
        self.buttons("Brightness Up (X)", self.brightnessUpMult, 3)
        self.buttons("Brightness Up (+)", self.brightnessUpIncr, 4)
        self.buttons("Brightness Down (X)", self.brightnessDownMult, 5)
        self.buttons("Brightness Down (+)", self.brightnessDownIncr, 6)
        self.buttons("Crop", self.crop, 7)
        self.buttons("Zoom In", self.zoomin, 8)
        self.buttons("Print Histogram", self.histogram, 9)
        self.buttons("Histeq", self.histeq, 10)
        self.buttons("Print Shape", self.shape, 11)
        self.gambar = None
        self.img = Image
        self.countred = np.zeros(256, dtype = int) #inisiasi penampung nilai untuk menampilkan histogram
        self.countblue = np.zeros(256, dtype = int) #inisiasi penampung nilai untuk menampilkan histogram
        self.countgreen = np.zeros(256, dtype = int) #inisiasi penampung nilai untuk menampilkan histogram
        
    def buttons(self, a, b, c):
        self.button = ttk.Button(self.labelframe, text = a, command = b)   
        self.button.grid(column = 1, row = c)
                      
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("jpg","*.jpg"),("jpeg","*.jpeg"),("All Files", "*.*")))
        path = self.filename
        gam = Image.open(path)
        self.img = gam
        self.cetak(gam, 0, 0)
        #untuk mendapatkan file path dari gambar yang akan dibuka
        
    def cetak(self, img, val, vali):
        gambar2 = ImageTk.PhotoImage(img)
        gambar3 = ttk.Label(self, image = gambar2)
        gambar3.image = gambar2
        self.gambar = gambar3
        self.gambar.grid_forget
        self.gambar.grid(column = 3 + vali, row = 1 + val)
        #untuk mencetak gambar kedalam grid

    def greyscale(self):
        newimg = self.img.convert("RGBA")
        imgarr = np.asarray(newimg)
        red = imgarr[:, :, 1]
        green = imgarr[:, :, 2]
        blue = imgarr[:, :, 3]
        sumr = np.sum(red) # mendapatkan nilai total dari array merah
        sumg = np.sum(green) # mendapatkan nilai total dari array hijau
        sumb = np.sum(blue) #mendapatkan nilai total dari array biru
        sumall = sumr + sumg + sumb
        arrgray = (sumr / sumall * red) + (sumg / sumall * green) + (sumb / sumall * blue) # membuat array image baru dengan nilai dari semua array lain yang telah dirata" kan
        imgnew = Image.fromarray(arrgray.astype('uint8'))
        self.img = imgnew
        self.cetak(imgnew, 0, 0)
        #untuk merubah gambar menjadi greyscale
        
    def brightnessUpMult(self):
        newimg = self.img.convert("RGBA")
        imgarr = np.asarray(newimg)
        val = 1.1
        imgarr = imgarr * val
        imgarr = np.clip(imgarr, 0, 255)
        imgnew = Image.fromarray(imgarr.astype('uint8'))
        self.img = imgnew
        self.cetak(imgnew, 0, 0)
        #untuk menaikkan brightness dengan mengalikan array dengan nilai 1.1
        
    def brightnessUpIncr(self):
        newimg = self.img.convert("RGBA")
        imgarr = np.asarray(newimg)
        val = 20
        imgarr = imgarr + val
        imgarr = np.clip(imgarr, 0, 255)
        imgnew = Image.fromarray(imgarr.astype('uint8'))
        self.img = imgnew
        self.cetak(imgnew, 0, 0)
        #untuk menaikkan brightness dengan menambahkan array dengan nilai 20
        
    def brightnessDownMult(self):
        newimg = self.img.convert("RGBA")
        imgarr = np.asarray(newimg)
        val = 1.1
        imgarr = imgarr // val
        imgarr = np.clip(imgarr, 0, 255)
        imgnew = Image.fromarray(imgarr.astype('uint8'))
        self.img = imgnew
        self.cetak(imgnew, 0, 0)
        #untuk menurunkan brightness dengan membagi array dengan nilai 1.1
        
    def brightnessDownIncr(self):
        newimg = self.img.convert("RGBA")
        imgarr = np.asarray(newimg)
        val = 20
        imgarr = imgarr - val
        imgarr = np.clip(imgarr, 0, 255)
        imgnew = Image.fromarray(imgarr.astype('uint8'))
        self.img = imgnew
        self.cetak(imgnew, 0, 0)
        #untuk menurunkan brightness dengan mengurangi array dengan nilai 20
        
    def crop(self):
        newimg = self.img.convert("RGBA")
        imgarr = np.asarray(newimg)
        imgarr.setflags(write=1)
        
        xval = imgarr.shape[0]
        yval = imgarr.shape[1]
        
        tengahx = xval // 2
        tengahy = yval // 2
        
        kiri = imgarr[0:tengahx, 0:tengahy, :]
        imgkiri = Image.fromarray(kiri)
        imgkiri = imgkiri.convert("RGB")
        self.cetak(imgkiri, 0, 1)
        
        kanan = imgarr[tengahx:xval, 0:tengahy, :]
        imgkanan = Image.fromarray(kanan)
        imgkanan = imgkanan.convert("RGB")
        self.cetak(imgkanan, 1, 1)
        
        kirib = imgarr[0:tengahx, tengahy:yval, :]
        imgkirib = Image.fromarray(kirib)
        imgkirib = imgkirib.convert("RGB")
        self.cetak(imgkirib, 0, 2)
        
        kananb = imgarr[tengahx:xval, tengahy:yval, :]
        imgkananb = Image.fromarray(kananb)
        imgkananb = imgkananb.convert("RGB")
        self.cetak(imgkananb, 1, 2)
        #untuk melakukan crop pada gambar menjadi 4 bagian 
        
    def zoomin(self):
        newimg = self.img.convert("RGBA")
        imgarr = np.asarray(newimg)   
        imgnew = np.repeat(np.repeat(imgarr, 2, axis=0), 2, axis=1)
        imgnew = Image.fromarray(imgnew.astype('uint8'))
        self.cetak(imgnew, 0, 1)
        #untuk memperbesar gambar dengan merubah satu index menjadi 4 index dan memperbesar size array
        
    def histogram(self):
        newimg = self.img.convert("RGBA")
        imgarr = np.asarray(newimg)
        red = imgarr[:, :, 1]
        green = imgarr[:, :, 2]
        blue = imgarr[:, :, 3]
        histred = np.ravel(red) # membuat array satu dimensi sehingga perhitungan menjadi lebih mudah dan kompleksitas alogitma lebih simple
        histblue = np.ravel(blue)
        histgreen = np.ravel(green)
        for i in range(len(histred)):
            self.countred[histred[i]] += 1
            self.countblue[histblue[i]] += 1
            self.countgreen[histgreen[i]] += 1
        plt.subplot(311) # membuah sebuah pengaturan subplot dengan pengaturan 3 rows dan 1 column dan meletakkan pada grid 1
        plt.plot(self.countred)
        plt.title("Histogram Red")# memberi judul pada grafik yang akan ditampilkan
        plt.subplot(312)# membuah sebuah pengaturan subplot dengan pengaturan 3 rows dan 1 column dan meletakkan pada grid 2
        plt.plot(self.countblue)
        plt.title("Histogram Blue")# memberi judul pada grafik yang akan ditampilkan
        plt.subplot(313) # membuah sebuah pengaturan subplot dengan pengaturan 3 rows dan 1 column dan meletakkan pada grid 3
        plt.plot(self.countgreen) 
        plt.title("Histogram Green")# memberi judul pada grafik yang akan ditampilkan
        plt.show()
        
    def histeq(self):
        newimg = self.img.convert("RGBA")
        imgarr = np.asarray(newimg)
        red = imgarr[:, :, 1]
        green = imgarr[:, :, 2]
        blue = imgarr[:, :, 3]
        batasAtasL = 220 #inisiasi batas atas untuk perhitungan
        batasBawahL = 20 #inisiasi batas bawah untuk perhitungan
        tempRed, tempBlue, tempGreen = [], [], []
        for i in range(len(self.countred)): # membuat array baru yang di dalamnya hanya terdapat nilai index yang minimal memiliki jumlah sebanyak 1% dari total bit
            if (self.countred[i] > 0.01 * np.sum(self.countred)):
                tempRed.append(i)
            if (self.countblue[i] > 0.01 * np.sum(self.countblue)):
                tempBlue.append(i)
            if (self.countgreen[i] > 0.01 * np.sum(self.countgreen)):
                tempGreen.append(i)
        batasBawahRed = np.min(tempRed)
        batasAtasRed = np.max(tempRed)
        batasBawahBlue = np.min(tempBlue)
        batasAtasBlue = np.max(tempBlue)
        batasBawahGreen = np.min(tempGreen)
        batasAtasGreen = np.max(tempGreen)
        imgarr.setflags(write = 1) # membuat agar array bisa ditulis
        def rumus(bbb, bba, bab, baa, x): #inisiasi rumus perhitungan untuk histeq
            return bbb + ((x - bba) * (bab - bbb) / (baa - bba))
        newred = np.zeros(red.shape) # menginisiasi tempat penampung nilai baru dengan bentuk yang sama dengan array lama
        newblue = np.zeros(blue.shape)
        newgreen = np.zeros(green.shape)
        for i in range(red.shape[0]):
            for j in range(red.shape[1]):
                newred[i][j] = rumus(batasBawahRed, batasBawahL, batasAtasRed, batasAtasL, red[i][j])
                newblue[i][j] = rumus(batasBawahBlue, batasBawahL, batasAtasBlue, batasAtasL, blue[i][j])
                newgreen[i][j] = rumus(batasBawahGreen, batasBawahL, batasAtasGreen, batasAtasL, green[i][j])
        imgarr[:, :, 1] = newred
        imgarr[:, :, 2] = newgreen
        imgarr[:, :, 3] = newblue
        imgnew = Image.fromarray(imgarr.astype('uint8'))
        self.img = imgnew
        self.cetak(imgnew, 0, 0)
                
    def shape(self):
        newimg = self.img.convert("RGBA")
        imgarr = np.asarray(newimg)   
        red = imgarr[:, :, 1]
        print("dimensi array image", imgarr.shape)
        print("dimensi array warna", red.shape)
    

if __name__ == '__main__':
    root = Root()
    root.mainloop()
    






        