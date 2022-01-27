import tkinter
from fonctions.fonctionnalite import folder_data
from fonctions.data import get_data, recording_data
from fonctions.style_window1 import grand_titre
from fonctions.style_fonctionnali_medecin import style_title, style_consultation_display, pady, sticky


def consultation():
    recovery_appointment = get_data(folder_data, "list_appointment")
    
    root = tkinter.Toplevel()
    root.geometry("720x480")
    root.resizable(width=False, height=False)
    root.title("Consultation du jour")
    root["bg"] = "#4E9F3D"

    frame_title = tkinter.Frame(root)
    label_title = tkinter.Label(frame_title, text="LISTE DES CONSULTATION DU JOUR", **grand_titre)
    label_title.grid(row=0, column=0)
    frame_title.grid(row=0, column=0, pady=20, padx=60)
    
    frame_reservation = tkinter.Frame(root, bg="#4E9F3D")
       
    number_label = tkinter.Label(frame_reservation, text="N°", **style_title)
    number_label.grid(row=0, column=0, sticky=sticky)
    
    name_label = tkinter.Label(frame_reservation, text="Nom", **style_title)
    name_label.grid(row=0, column=1, padx=100, sticky=sticky)
    
    category_label = tkinter.Label(frame_reservation, text="Categorie", **style_title)
    category_label.grid(row=0, column=2, sticky=sticky)
    
    i = 0
    for item in recovery_appointment:
        i += 1
        name = item["last_name"] + " " + item["firs_name"]
        category = item["category"]
        
        tkinter.Label(frame_reservation, text=i, **style_consultation_display).grid(row=i, column=0, pady=pady, sticky=sticky)
        tkinter.Label(frame_reservation, text=name, **style_consultation_display).grid(row=i, padx=100, column=1, pady=pady, sticky=sticky)
        tkinter.Label(frame_reservation, text=category, **style_consultation_display).grid(row=i, column=2, pady=pady, sticky=sticky)
        
    frame_reservation.grid(row=1, column=0)

    root.mainloop()