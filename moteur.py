#author : Ben Musampa
# i use tkinter and GoogleNews library to built this application
from tkinter import *
from GoogleNews import GoogleNews
import pandas as pd
from tkinter.filedialog import *
from threading import *
from tkinter import messagebox
from tkinter import ttk
#---------------------------------------------------- moteur de recherche -----

def recherche():
    
    actu = GoogleNews(period='1h', lang='fr')
    actu.search(sujet.get())
    resultat = actu.result()
    info = pd.DataFrame.from_dict(resultat)
    info = info.drop(columns = ["img"])
    info.head()

    for i in resultat:
        res.set("Titre : " + i["title"] + "\n \n"+"information : " + i["desc"] + "\n \n" +"Lien : " +i["link"])
        

#---------------------------------------------- programme ----------

cn = Tk()
cn.iconbitmap("favicon.ico")
cn.title("Congonews")
cn.minsize(900,600)
cn.maxsize(1000,800)

res = StringVar()

cnlogo = PhotoImage(file = "logo.png")
cnlogo2 = Label(image = cnlogo)
cnlogo2.place(x=235,y=20)

nom = Label(cn, text="Congonews", fg="black", font=("Montserrat",32))
nom.place(x=375,y=55)

sujet = Entry(cn, width=50, font=("Montserrat",12) ,borderwidth=1)
sujet.place(x=200,y=240)

Entrer_sujet = Label(cn, text="sujet ", font=("Montserrat",11))
Entrer_sujet.place(x=90,y=240)

recherche_button = Button(cn,width=12 ,height=1 , text="recherche", font=("Montserrat",14) ,relief="groove", bg="#3A2E2E", fg="white", borderwidth=1, command=recherche)
recherche_button.place(x=360,y=290)

information = Label(cn, text="", textvariable=res, fg="black", font=("Montserrat",12)).place(x=50,y=340)
cn.mainloop()
