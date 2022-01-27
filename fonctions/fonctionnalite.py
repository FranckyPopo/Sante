import os
import tkinter
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from .data import recording_data, get_data
from fonctions import style_window1, style_window3


folder_current = os.getcwd()
folder_data = os.path.join(folder_current, "data")
    
recovery_appointment = get_data(folder_data, "list_appointment")


def window1():
    
    def afficher():
        last_name = enter_last_name.get()
        firs_name = enter_firsname.get()
        email = enter_email.get()
        telephone_number = enter_telephone_number.get()
        category = list_category.get()
        date_appoitment = str(enter_date.get_date())
        
        label_erreur = tkinter.Label(container_forms, text="Veuillez remplir tous les champs", fg="#4E9F3D", bg="#4E9F3D")
        label_erreur.grid(row=13, column=0, sticky="W")

        if last_name and firs_name and email and telephone_number:
            instance_appoitment = {
                "last_name": last_name,
                "firs_name": firs_name,
                "email": email,
                "telephone_number": telephone_number,
                "category": category,
                "date_appoitment": date_appoitment
            }
            
            recovery_appointment.append(instance_appoitment)
            recording_data(recovery_appointment, folder_current, "data", "list_appointment")
            
            messagebox.showinfo("Rendez-vous pris avec succès", "Rendez-vous pris avec succès")
            
            enter_last_name.delete(0, "end")
            enter_firsname.delete(0, "end")
            enter_telephone_number.delete(0, "end")
            enter_email.delete(0, "end")
            
            label_erreur["fg"] = "#4E9F3D"
        else:
            label_erreur["fg"] = "red"
    
    root = tkinter.Tk()
    root.geometry("720x800")
    root.resizable(width=False, height=False)
    root.title("Prendre rendez-vous")
    root["bg"] = "#4E9F3D"
    
    container_title = tkinter.Frame(root, bg="#4E9F3D")
    
    titre = tkinter.Label(container_title, text="PRENDRE RENDEZ-VOUS", **style_window1.grand_titre).pack(pady=35, fill="x")
    
    container_title.pack()
    
    container_forms = tkinter.Frame(root, bg="#4E9F3D")

    # champ 1
    Label_last_name = tkinter.Label(container_forms, text="Nom: ", **style_window1.color_label).grid(row=0, column=0, **style_window1.margin_label)
    enter_last_name = tkinter.Entry(container_forms)
    enter_last_name.grid(row=2, column=0, **style_window1.style_enter)
    
    # champ 2
    Label_firs_name = tkinter.Label(container_forms, text="Prénom: ", **style_window1.color_label).grid(row=3, column=0, **style_window1.margin_label)
    enter_firsname = tkinter.Entry(container_forms)
    enter_firsname.grid(row=4, column=0, **style_window1.style_enter)
    
    # champ 3
    Label_telephone_number = tkinter.Label(container_forms, text="Télephone: ", **style_window1.color_label).grid(row=5, column=0, **style_window1.margin_label)
    enter_telephone_number = tkinter.Entry(container_forms)
    enter_telephone_number.grid(row=6, column=0, **style_window1.style_enter)
    
    # champ 4
    Label_email = tkinter.Label(container_forms, text="Email: ", **style_window1.color_label).grid(row=7, column=0, **style_window1.margin_label)
    enter_email = tkinter.Entry(container_forms) 
    enter_email.grid(row=8, column=0, **style_window1.style_enter)

    # champ 5
    label_category = tkinter.Label(container_forms, text="Category: ", **style_window1.color_label).grid(row=9, column=0, **style_window1.margin_label)
    choose_category = ["Generaliste", "Dermatologue", "Dentiste"]
    list_category = ttk.Combobox(container_forms, values=choose_category, width=17)
    list_category.current(0)
    list_category.grid(row=10, column=0, **style_window1.style_enter) 
    
    # champs 6
    label_date = tkinter.Label(container_forms, text="Date du rendez-vous: ", **style_window1.color_label).grid(row=11, column=0, **style_window1.margin_label)
    enter_date = DateEntry(container_forms)
    enter_date.grid(row=12, column=0, **style_window1.style_calendar)
    
    # Bouton valider
    bnt_validate = tkinter.Button(container_forms, command=afficher, text="Valider",  **style_window1.bnt_valided).grid(row=14, column=0, sticky="W", pady=20)
    
    container_forms.pack()
    
    root.mainloop()
    
def window3():
    
    
    root = tkinter.Toplevel()
    root.geometry("720x480")
    #root.resizable(width=False, height=False)
    root["bg"] = "#4E9F3D"
    
    frame_title = tkinter.Frame(root)
    
    label_title = tkinter.Label(frame_title, text="OU NOUS RETOUVER", **style_window3.style_title).grid(row=0)
    
    frame_title.pack(pady=25)
    
    frame_infos = tkinter.Frame(root, bg="#4E9F3D")
    
    
    # block 1
    container1 = tkinter.Frame(frame_infos, bg="#4E9F3D")
    
    label1 = tkinter.Label(container1, text="Clinique Popo (Siége)", **style_window3.style_label1)
    label1.grid(row=0, column=0, sticky="WE")
    
    under_label1 = tkinter.Label(container1, text="25 32 00 05 04", **style_window3.style_under_label) 
    under_label1.grid(row=1, column=0, sticky="W")
    
    under_label2 = tkinter.Label(container1, text="Ouvert actuellement", **style_window3.style_under_label) 
    under_label2.grid(row=2, column=0, sticky="W")
    
    container1.grid(row=0, column=0, pady=10)
    
    # block 2
    container2 = tkinter.Frame(frame_infos, bg="#4E9F3D")
    
    label2 = tkinter.Label(container2, text="Clinique Popo - Koumassi", **style_window3.style_label1)
    label2.grid(row=0, column=0, sticky="WE")
    
    under_label_1 = tkinter.Label(container2, text="25 05 04 00 32", **style_window3.style_under_label) 
    under_label_1.grid(row=1, column=0, sticky="W")
    
    under_label2_2 = tkinter.Label(container2, text="Ouvert  24h / 24h", **style_window3.style_under_label) 
    under_label2_2.grid(row=2, column=0, sticky="W")
    
    container2.grid(row=1, column=0, pady=10)
    
    # block 3
    container3 = tkinter.Frame(frame_infos, bg="#4E9F3D")
    
    label3 = tkinter.Label(container3, text="Clinique Popo - Riviera", **style_window3.style_label1)
    label3.grid(row=0, column=0, sticky="WE")
    
    under_label_3_3 = tkinter.Label(container3, text="25 05 04 00 32", **style_window3.style_under_label) 
    under_label_3_3.grid(row=1, column=0, sticky="W")
    
    under_label2_3 = tkinter.Label(container3, text="Ouvert  24h / 24h", **style_window3.style_under_label) 
    under_label2_3.grid(row=2, column=0, sticky="W")
    
    container3.grid(row=2, column=0)
    
    
    frame_infos.pack()
    
    
    root.mainloop()