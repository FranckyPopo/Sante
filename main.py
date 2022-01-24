import tkinter
from tkinter import ttk
from fonctions import style_acceuil

window = tkinter.Tk()
window.geometry("720x480")
window.minsize(720, 480)
window.title("CLINIQUE POPO")
window["bg"] = "#4E9F3D"


def window1():
    
    root = tkinter.Tk()
    root.geometry("720x480")
    root.minsize(720, 480)
    root.title("Prendre rendez-vous")
    root["bg"] = "#4E9F3D"
    
    container_title = tkinter.Frame(root, bg="#4E9F3D")
    
    titre = tkinter.Label(container_title, text="PRENDRE RENDEZ-VOUS", **style_acceuil.grand_titre).pack(pady=35)
    
    container_title.pack()
    
    container_forms = tkinter.Frame(root, bg="#4E9F3D")
    
    # champ 1
    last_name = tkinter.StringVar()
    Label_last_name = tkinter.Label(container_forms, text="Nom: ", **style_acceuil.color_label).grid(row=0, column=0, **style_acceuil.margin_label)
    enter_last_name = tkinter.Entry(container_forms, textvariable=last_name).grid(row=0, column=1, **style_acceuil.style_enter)
    
    # champ 2
    firs_name = tkinter.StringVar()
    Label_firs_name = tkinter.Label(container_forms, text="Prénom: ", **style_acceuil.color_label).grid(row=1, column=0, **style_acceuil.margin_label)
    enter_firsname = tkinter.Entry(container_forms, textvariable=firs_name).grid(row=1, column=1, **style_acceuil.style_enter)
    
    # champ 3
    telephone_number = tkinter.IntVar()
    Label_telephone_number = tkinter.Label(container_forms, text="Télephone: ", **style_acceuil.color_label).grid(row=2, column=0, **style_acceuil.margin_label)
    enter_telephone_number = tkinter.Entry(container_forms, textvariable=telephone_number).grid(row=2, column=1, **style_acceuil.style_enter)
    
    # champ 4
    email = tkinter.StringVar()
    Label_email = tkinter.Label(container_forms, text="Email: ", **style_acceuil.color_label).grid(row=3, column=0, **style_acceuil.margin_label)
    enter_email = tkinter.Entry(container_forms, textvariable=email).grid(row=3, column=1, **style_acceuil.style_enter)

    # champ 5
    label_category = tkinter.Label(container_forms, text="Category: ", **style_acceuil.color_label).grid(row=4, column=0, **style_acceuil.margin_label)
    choose_category = ["Généraliste", "Dermatologue", "Dentiste"]
    liste_category = ttk.Combobox(container_forms, values=choose_category, width=17)
    liste_category.current(0)
    liste_category.grid(row=4, column=1, **style_acceuil.style_enter) 
    
    # Bouton valider
    bnt_validate = tkinter.Button(container_forms, text="Valider", command=voir, **style_acceuil.bnt_valided).grid(row=5, column=0, sticky="W")
    container_forms.pack()
    
    root.mainloop()
    
    



frame = tkinter.Frame(window, bg="#4E9F3D")

bnt1 = tkinter.Button(frame, text="Prendre rendez-vous", **style_acceuil.style_bouton_accueil, command=window1).grid(row=0, column=0, padx=20)
bnt2 = tkinter.Button(frame, text="Tarifs", **style_acceuil.style_bouton_accueil).grid(row=0, column=1, padx=20)
bnt3 = tkinter.Button(frame, text="Nous retrouver", **style_acceuil.style_bouton_accueil).grid(row=0, column=2, padx=20)

frame.pack(expand="yes")

window.mainloop()
