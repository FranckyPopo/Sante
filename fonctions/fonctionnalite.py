import os
import tkinter
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from .data import recording_data, get_data
from fonctions import style_window1, style_canet


folder_current = os.getcwd()
folder_data = os.path.join(folder_current, "data")
    
recovery_appointment = get_data(folder_data, "list_appointment")

def user_fonctionnality_1():
    
    def appoitment():
        recovery_appointment = get_data(folder_data, "list_appointment")
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
    bnt_validate = tkinter.Button(container_forms, command=appoitment, text="Valider",  **style_window1.bnt_valided).grid(row=14, column=0, sticky="W", pady=20)
    
    container_forms.pack()
    
    root.mainloop()
    
def user_fonctionnality_2():
    recovery_canet = get_data(folder_data, "list_canet")
    
    root = tkinter.Toplevel()
    root.title("Canet de santé")
    root.geometry("720x600")
    root.resizable(width=False, height=False)
    root.title("Prendre rendez-vous")
    root["bg"] = style_window1.bg
    
    title = tkinter.Label(root, text="CANET DE SANTE", **style_window1.grand_titre)
    title.pack(pady=30)
    
    i = 0
    for item in recovery_canet:
        reason = item["reason"]
        last_name_doctor = item["doctor"]
        date_appoitment = item["date_appoitment"]
        
        frame_block = tkinter.Frame(root, bg=style_window1.bg)
        
        label_reason = tkinter.Label(frame_block, text=reason, **style_canet.style_label_reason)
        label_reason.grid(row=0)
        
        label_doctor = tkinter.Label(frame_block, text=last_name_doctor, **style_canet.style_infos)
        label_doctor.grid(row=1)
        
        label_date_appoitment = tkinter.Label(frame_block, text=date_appoitment, **style_canet.style_infos)
        label_date_appoitment.grid(row=2)
        
        frame_block.pack(padx=100)
        i += 1
    
    
    root.mainloop()

