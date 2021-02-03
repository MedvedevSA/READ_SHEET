import gspread
import os
import subprocess
from tkinter import *  
from tkinter.ttk import Combobox
import pandas as pd

def df_filter(df, key, value):
    return df[df[key] == value]

def btn1_clicked():  
    upd_combo()
    combo.current(1)  # установите вариант по умолчанию  

def btn2_clicked():  
    open_pj_path(txt.get())    

def upd_dict_n_cnc (list_2d):
    new_dict = {"1":[],
                "2":[],
                "3":[]}

    for index in range(0,len(list_2d[1])):
        status_number = [ list_2d[0][index], list_2d[2][index]]

        if list_2d[1][index] == "1":
            new_dict["1"].append(status_number)
        elif list_2d[1][index] == "2":
            new_dict["2"].append(status_number)
        elif list_2d[1][index] == "3":
            new_dict["3"].append(status_number)
    return new_dict

def upd_combo ():
    
    gc = gspread.service_account(filename=".\\key.json")
    sheet_url = "https://docs.google.com/spreadsheets/d/1WY0pdiHgJ39govH042CNgQD_vKKYyTsTslZMYsEw1Og/edit#gid=942461385"

    sht = gc.open_by_url(sheet_url)
    worksheet = sht.sheet1
    dataframe = pd.DataFrame(worksheet.get_all_records())
    dataframe = dataframe
    request = txt.get()
    df_f = df_filter(dataframe,"Номер станка",1)
    df_f = df_f
    #combo['values'] = tuple(dict_status_number[txt.get()][1])  
    
def open_pj_path (batch_n):

    path_col = 14
    
    gc = gspread.service_account(filename=".\\key.json")
    sheet_url = "https://docs.google.com/spreadsheets/d/1WY0pdiHgJ39govH042CNgQD_vKKYyTsTslZMYsEw1Og/edit#gid=942461385"

    sht = gc.open_by_url(sheet_url)
    worksheet = sht.sheet1
    values_list = worksheet.col_values(3)

    pj_path = worksheet.cell(values_list.index(batch_n)+1,path_col).value

    cmd = f"explorer {pj_path}"
    subprocess.Popen(cmd)


window = Tk()  
window.title("Навигатор")  
window.geometry('400x250')  

lbl = Label(window, text="Номер станка")  
lbl.grid(column=0, row=0)  

txt = Entry(window,width=10)  
txt.grid(column=1, row=0)  

btn1 = Button(window, text="Обновить список", command=btn1_clicked)  
btn1.grid(column=2, row=0) 


combo = Combobox(window)  
combo.grid(column=0, row=1) 

btn2 = Button(window, text="Открыть", command=btn2_clicked)  
btn2.grid(column=1, row=1) 

window.mainloop()

