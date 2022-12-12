#Pattanapong Chirabandhu 6310742132
from tkinter import *

"""ในส่วนของ UX จะมีการออกแบบให้ใช้งานง่ายเพียงแค่ทำการป้อน input องศา
   ลงไปแล้วกดปุ่มเพื่อแปลงค่า ใช้งานเรียบง่ายไม่ซับซ้อน ตอบโจทย์ผู้ใช้งาน
   ในส่วนของ UI Design ให้ดูสบายตาในเรื่องของการจัดวางองค์ประกอบ การวาง Layout 
   เป็นระเบียบโดยในโปรแกรมนี้จะเน้นการจัดวาง Layout ให้อยู่ตรงกลาง
   ในส่วนของสีก็มีการเลือกใช้สี Bloody Moon Color Palette ให้ความรู้สึกสบายตา
   มีความ Modern น่าใช้งาน """

#tkinter window settings
root = Tk()
root.geometry("1000x680") #window size
root.configure(bg='#233342') #set background color
root.title("Tempereture Converter") # Title of window

# Main label 
title_label = Label(root, text="Temperature Converter", font=("Monaco 30 bold"), bg="#233342", fg="white")
title_label.pack(anchor='n', pady=(60, 0)) # set to middle padding from top 60 units

#this function convert celsius to farenheit 
def convertToFarenheit():
    c = float(celsius_entry.get()) #recieve a float from entry box
    f = (c * 9/5) + 32 #farenheit formula
    farenheit_entry.delete(0,'end') #clear entry box
    farenheit_entry.configure(fg="black") # set entry box text color to black
    farenheit_entry.insert(0, round(f,2)) #insert result to entry box

#this function convert farenheit to celsius 
def convertToCelsius():
    f = float(farenheit_entry.get()) #recieve a float from entry box
    c = (f - 32) * 5/9  #celsius formula
    celsius_entry.delete(0,'end') #clear entry box
    celsius_entry.configure(fg="black") # set entry box text color to black
    celsius_entry.insert(0, round(c,2)) #insert resault to entry box

#this function is activate when user clicked into entry box it will clear current input
def temp_text(e):
   celsius_entry.delete(0,"end")
   celsius_entry.configure(fg="black")
   farenheit_entry.delete(0,"end")
   farenheit_entry.configure(fg="black")
    
#celsius label
cLabel = Label(root, text="Celsius(°C)", font=("Monaco 15 bold"), bg="#233342", fg="white")
cLabel.pack(anchor='n', pady=(30, 0)) # set to middle padding from top 30 units

#frame of entry box for input in °C
frame = Frame(root, bg="#233342")
celsius_entry = Entry(frame, font=("Arial 20 "), width=40, bg="white",justify=CENTER, fg="grey") #Entry box for input in celsius
celsius_entry.insert(0, "°C") # set default text in entry box °C
celsius_entry.bind("<FocusIn>", temp_text) #when click entry box it will activate temp_text function
celsius_entry.pack(anchor='n',pady=(10, 0)) # set to middle padding from top 10 units
frame.pack(pady=(10, 0)) # set to middle padding from top 10 units

#this button is for convert to farenheit
convertToF_button = Button(root, text="Convert to °F", command=convertToFarenheit,bd=0, bg="#B35340", fg="white", height=1, width=15,activebackground="#5072A7",activeforeground="white")
convertToF_button.pack(pady=(40, 0)) # set to middle padding from top 40 units

#farenheit label
fLabel = Label(root, text="Farenheit(°F)", font=("Monaco 15 bold"), bg="#233342", fg="white")
fLabel.pack(anchor='n', pady=(60, 0)) # set to middle padding from top 60 units

#Entry box for input in °F
frame2 = Frame(root, bg="#233342")
farenheit_entry = Entry(frame2, font=("Arial 20 "), width=40, bg="white",justify=CENTER, fg="grey") #Entry box for input in farenheit
farenheit_entry.insert(0, "°F") # set default text in entry box °F
farenheit_entry.bind("<FocusIn>", temp_text) #when click entry box it will activate temp_text function
farenheit_entry.pack(anchor='n',pady=(10, 0)) # set to middle padding from top 10 units
frame2.pack(pady=(10, 0)) # set to middle padding from top 10 units

#this button is for convert to celsius
convertToC_button = Button(root, text="Convert to °C", command=convertToCelsius,bd=0, bg="#B35340", fg="white", height=1, width=15,activebackground="#5072A7",activeforeground="white")
convertToC_button.pack(pady=(40, 0)) # set to middle padding from top 40 units

#this is for running gui
root.mainloop() 