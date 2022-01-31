import os
import tkinter
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from .data import recording_data, get_data
from fonctions import style_window1, style_canet


folder_current = os.getcwd()
folder_data = os.path.join(folder_current, "data")
    

def user_fonctionnality_1():
    
    def appoitment():
        recovery_appointment = get_data(folder_data, "list_appointment")
        last_name = enter_last_name.get()
        firs_name = enter_firsname.get()
        email = enter_email.get()
        telephone_number = enter_telephone_number.get()
        category = list_category.get()
        date_appoitment = str(enter_date.get_date())
        
        label_erreur = tkinter.Label(container_forms, text="Veuillez remplir tous les champs", fg=style_window1.bg, bg=style_window1.bg)
        label_erreur.grid(row=13, column=0, sticky="W")

        if last_name and firs_name and email and telephone_number and category:
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
            
            label_erreur["fg"] = style_window1.bg
        else:
            label_erreur["fg"] = "red"
    
    root = tkinter.Tk()
    root.geometry("720x600")
    root.resizable(width=False, height=False)
    root.title("Prendre rendez-vous")
    root["bg"] = style_window1.bg
    
    container_title = tkinter.Frame(root, bg=style_window1.bg)
    
    label_title = tkinter.Label(container_title, text="PRENDRE RENDEZ-VOUS", **style_window1.grand_titre)
    label_title.pack(pady=25)
    
    container_title.pack()
    
    container_forms = tkinter.Frame(root, bg=style_window1.bg)

    # champ 1
    container1 = tkinter.Frame(container_forms, bg=style_window1.bg)
    Label_last_name = tkinter.Label(container1, text="Nom: ", **style_window1.color_label)
    Label_last_name.grid(row=0, column=0, sticky=style_window1.sticky, pady=style_window1.pady)
    
    enter_last_name = tkinter.Entry(container1)
    enter_last_name.grid(row=1, column=0, **style_window1.style_enter)
    container1.grid(row=0, sticky=style_window1.sticky, pady=style_window1.pady)
    
    # champ 2
    container2 = tkinter.Frame(container_forms, bg=style_window1.bg)
    Label_firs_name = tkinter.Label(container2, text="Prénom: ", **style_window1.color_label)
    Label_firs_name.grid(row=0, column=0, sticky=style_window1.sticky, pady=style_window1.pady)
    
    enter_firsname = tkinter.Entry(container2)
    enter_firsname.grid(row=1, column=0, **style_window1.style_enter)
    container2.grid(row=1, sticky=style_window1.sticky, pady=style_window1.pady)
    
    # champ 3
    container3 = tkinter.Frame(container_forms, bg=style_window1.bg)
    Label_telephone_number = tkinter.Label(container3, text="Télephone: ", **style_window1.color_label)
    Label_telephone_number.grid(row=0, column=0, sticky=style_window1.sticky, pady=style_window1.pady)
    
    enter_telephone_number = tkinter.Entry(container3)
    enter_telephone_number.grid(row=1, column=0, **style_window1.style_enter)
    container3.grid(row=2, sticky=style_window1.sticky, pady=style_window1.pady)
    
    # champ 4
    container4 = tkinter.Frame(container_forms, bg=style_window1.bg)
    Label_email = tkinter.Label(container4, text="Email: ", **style_window1.color_label)
    Label_email.grid(row=0, column=0, sticky=style_window1.sticky, pady=style_window1.pady)
    
    enter_email = tkinter.Entry(container4) 
    enter_email.grid(row=2, column=0, **style_window1.style_enter)
    container4.grid(row=3, sticky=style_window1.sticky, pady=style_window1.pady)
    
    # champ 5
    container5 = tkinter.Frame(container_forms, bg=style_window1.bg)
    label_category = tkinter.Label(container5, text="Category: ", **style_window1.color_label)
    label_category.grid(row=0, column=0, sticky=style_window1.sticky, pady=style_window1.pady)
     
    choose_category = ["Generaliste", "Dermatologue", "Dentiste"]
    list_category = ttk.Combobox(container5, values=choose_category, width=17)
    list_category.current(0)
    list_category.grid(row=1, column=0, **style_window1.style_enter) 
    container5.grid(row=4, sticky=style_window1.sticky, pady=style_window1.pady)
    
    # champs 6
    container6 = tkinter.Frame(container_forms, bg=style_window1.bg)
    label_date = tkinter.Label(container6, text="Date du rendez-vous: ", **style_window1.color_label)
    label_date.grid(row=0, column=0, sticky=style_window1.sticky, pady=style_window1.pady)
    
    enter_date = DateEntry(container6)
    enter_date.grid(row=1, column=0, **style_window1.style_calendar)
    container6.grid(row=5, sticky=style_window1.sticky, pady=style_window1.pady)
    
    # Bouton valider
    bnt_validate = tkinter.Button(container_forms, command=appoitment, text="Valider",  **style_window1.bnt_valided).grid(row=14, column=0, sticky="W", pady=20)
    
    container_forms.pack()
    
    root.mainloop()
    
def user_fonctionnality_2():
    recovery_canet = get_data(folder_data, "list_canet")
    
    root = tkinter.Toplevel()
    root.title("Canet de santé")
    root.geometry("720x600")
    #root.resizable(width=False, height=False)
    root.title("Prendre rendez-vous")
    root["bg"] = style_window1.bg
    
    title = tkinter.Label(root, text="CANET DE SANTE", **style_window1.grand_titre)
    title.pack(pady=30)
    
    frame_main = tkinter.Frame(root, bg="#4E9F3D", relief="flat")
    frame_main.pack()
    
    my_canvas = tkinter.Canvas(frame_main, height=450, width=400, bg="#4E9F3D")
    my_canvas.pack(side="left", fill="both", expand=1)
    
    my_croolbar = ttk.Scrollbar(frame_main, orient="vertical", command=my_canvas.yview)
    my_croolbar.pack(side="right", fill="y")

    my_canvas.config(yscrollcommand=my_croolbar.set)
    my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    
    second_frame = tkinter.Frame(my_canvas, bg="#4E9F3D")
    
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    for item in recovery_canet:
        reason = item["reason"]
        date = item["date_appoitment"]
        doctor = item["doctor"]       
        
        text_reason = tkinter.Text(second_frame, bg="#4E9F3D", height=5, relief="flat", font=("Arial", 12))
        text_reason.insert(1.0, reason)
        text_reason.configure(state='disabled')
        text_reason.pack()
        
        frame_block = tkinter.Frame(second_frame, bg="#4E9F3D")
        frame_block.pack(fill="x")
        
        label_date = tkinter.Label(frame_block, text=date, fg="#D8E9A8", bg="#4E9F3D")
        label_date.grid(row=1, column=0, pady=5)
        
        label_doctor = tkinter.Label(frame_block, text=doctor, fg="#D8E9A8", bg="#4E9F3D")
        label_doctor.grid(row=1, column=1, padx=300, pady=5)
        
    
    
    root.mainloop()