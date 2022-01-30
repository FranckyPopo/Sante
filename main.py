import os
import tkinter
from fonctions import style_acceuil, fonctionnalite, fonctionnalite_medecin

window = tkinter.Tk()
window.geometry("720x480")
window.resizable(width=False, height=False)
window.title("CLINIQUE POPO")
window["bg"] = "#4E9F3D"
 
frame = tkinter.Frame(window, bg="#4E9F3D")

bnt1 = tkinter.Button(frame, text="Prendre rendez-vous", **style_acceuil.style_bouton_accueil, command=fonctionnalite.user_fonctionnality_1)
bnt1.grid(row=0, column=0, padx=20)

bnt2 = tkinter.Button(frame, text="Carnet de santé", **style_acceuil.style_bouton_accueil, command=fonctionnalite.user_fonctionnality_2)
bnt2.grid(row=0, column=1, padx=20)

frame.pack(expand="yes")

window.mainloop()