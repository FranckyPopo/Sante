import tkinter
from tkinter import ttk
import tkcalendar
from fonctions.fonctionnalite import folder_data, folder_current
from fonctions.data import get_data, recording_data
from fonctions.style_window1 import grand_titre, bnt_valided
from fonctions.style_fonctionnali_medecin import style_title, style_consultation_display, pady, sticky, style_canet, bg

from pprint import pprint

def consultation():
    recovery_appointment = get_data(folder_data, "list_appointment")
    
    root = tkinter.Toplevel()
    root.geometry("720x480")
    #root.resizable(width=False, height=False)
    root.title("Consultation du jour")
    root["bg"] = "#4E9F3D"

    frame_title = tkinter.Frame(root)
    label_title = tkinter.Label(frame_title, text="LISTE DES CONSULTATIONS DU JOUR", **grand_titre)
    label_title.grid(row=0, column=0)
    frame_title.pack(pady=20, padx=60)
    
    frame_reservation = tkinter.Frame(root, bg="#4E9F3D")
    frame_reservation.pack()
    
    number_label = tkinter.Label(frame_reservation, text="N°", **style_title)
    number_label.grid(row=0, column=0, sticky=sticky)

    name_label = tkinter.Label(frame_reservation, text="Nom", **style_title)
    name_label.grid(row=0, column=1, padx=80, sticky=sticky)
    
    category_label = tkinter.Label(frame_reservation, text="Categorie", **style_title)
    category_label.grid(row=0, column=2, sticky=sticky)
    
    main_frame = tkinter.Frame(root)
    main_frame.pack(fill="both", expand=1, padx=140)
    
    my_canvas = tkinter.Canvas(main_frame, bg="#4E9F3D")
    my_canvas.pack(side="left", fill="both", expand=1)

    my_croolbar = ttk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
    my_croolbar.pack(side="right", fill="y")
    
    my_canvas.config(yscrollcommand=my_croolbar.set)
    my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = tkinter.Frame(my_canvas, bg="#4E9F3D")
    second_frame.pack()

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i = 0
    for item in recovery_appointment:
        i += 1
        name = item["last_name"] + " " + item["firs_name"]
        category = item["category"]
        
        tkinter.Label(second_frame, text=i, **style_consultation_display).grid(row=i, column=0, pady=pady, padx=45, sticky=sticky)
        tkinter.Label(second_frame, text=name, **style_consultation_display).grid(row=i, column=1, pady=pady, padx=30, sticky=sticky)
        tkinter.Label(second_frame, text=category, **style_consultation_display).grid(row=i, column=2, pady=pady, sticky=sticky)
        
    

    root.mainloop()
    
def canet():

    def verification():
        choose_doctor = enter_last_name_doctor.get()
        date_appoitment = enter_date_appoitment.get()
        reason = enter_reason.get("1.0", "end")
        
        if choose_doctor and date_appoitment and reason != "\n":
            recovery_canet = get_data(folder_data, "list_canet")
            instance_canet = {
                "doctor": choose_doctor,
                "date_appoitment": date_appoitment,
                "reason": str(reason)
            }
            recovery_canet.append(instance_canet)
            recording_data(recovery_canet, folder_current, "data", "list_canet")
            
            if label_error["fg"] == "red": label_error["fg"] = bg
        else:
            label_error["fg"] = "red"
        
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
    
    list_doctor = ["Popo", "Afri", "Kreto",]
    enter_last_name_doctor = ttk.Combobox(container1, values=list_doctor)
    enter_last_name_doctor.current(1)
    enter_last_name_doctor.grid(row=2, column=0, sticky=sticky)
    container1.grid(row=0, pady=10, sticky=sticky)
    
    # champ 2
    container2 = tkinter.Frame(frame_forms, bg=bg)
    label_date = tkinter.Label(container2, text="Date:", **style_canet)
    label_date.grid(row=3, column=0, sticky=sticky)
    
    enter_date_appoitment = tkcalendar.DateEntry(container2)
    enter_date_appoitment.grid(row=4, column=0, sticky=sticky)
    container2.grid(row=1, pady=10, sticky=sticky)
    
    # champs 3
    container3 = tkinter.Frame(frame_forms, bg=bg)
    label_reason = tkinter.Label(container3, text="Motif:", **style_canet)
    label_reason.grid(row=0, column=0, sticky=sticky)
    
    enter_reason = tkinter.Text(container3, width=38, height=5)
    enter_reason.grid(row=1, column=0, sticky=sticky)
    
    # Erreur
    label_error = tkinter.Label(container3, text="Veuillez remplir tout les champs", bg=bg, fg=bg, font=("Arial", 10, "bold"))
    label_error.grid(row=2, sticky=sticky, pady=5)
    container3.grid(row=2, sticky=sticky)
    
    # Bouton valider
    bnt_validate = tkinter.Button(frame_forms, command=verification, text="Valider", **bnt_valided)
    bnt_validate.grid(row=3, sticky=sticky, pady=5)

    frame_forms.pack()
    
    root.mainloop()