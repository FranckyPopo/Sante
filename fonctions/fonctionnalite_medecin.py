import tkinter
from tkinter import ttk
import tkcalendar
from fonctions.fonctionnalite import folder_data
from fonctions.data import get_data, recording_data
from fonctions.style_window1 import grand_titre, bnt_valided
from fonctions.style_fonctionnali_medecin import style_title, style_consultation_display, pady, sticky, style_canet, bg


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
    
def canet():
    root = tkinter.Toplevel()
    root.title("Canet de santé")
    root.resizable(width=False, height=False)
    root.geometry("720x480")
    root["bg"] = "#4E9F3D"
    
    label_title = tkinter.Label(root, text="CANET DE SANTE", **grand_titre)
    label_title.pack(pady=25)
    
    frame_forms = tkinter.Frame(root, bg="#4E9F3D")
    
    # champs 1
    container1 = tkinter.Frame(frame_forms, bg=bg)
    label_doctor = tkinter.Label(container1, text="Medecin en charge de la consultation:", **style_canet)
    label_doctor.grid(row=0, sticky=sticky)
    
    choose_doctor = ["Popo", "Afri", "Kreto",]
    enter_last_name_doctor = ttk.Combobox(container1, values=choose_doctor)
    enter_last_name_doctor.grid(row=2, column=0, sticky=sticky)
    container1.grid(row=0, pady=10, sticky=sticky)
    
    # champ 2
    container2 = tkinter.Frame(frame_forms, bg=bg)
    label_date = tkinter.Label(container2, text="Date:", **style_canet)
    label_date.grid(row=3, column=0, sticky=sticky)
    
    
    enter_last_name_doctor = tkcalendar.DateEntry(container2)
    enter_last_name_doctor.grid(row=4, column=0, sticky=sticky)
    container2.grid(row=1, pady=10, sticky=sticky)
    
    # champs 3
    container3 = tkinter.Frame(frame_forms, bg=bg)
    label_reason = tkinter.Label(container3, text="Motif:", **style_canet)
    label_reason.grid(row=5, column=0, sticky=sticky)
    
    enter_reason = tkinter.Text(container3, width=38, height=5)
    enter_reason.grid(row=6, column=0, sticky=sticky)
    container3.grid(row=2, sticky=sticky)
    
    # Bouton valider
    bnt_validate = tkinter.Button(frame_forms, text="Valider", **bnt_valided)
    bnt_validate.grid(row=3, sticky=sticky, pady=20)

    frame_forms.pack()
    
    root.mainloop()