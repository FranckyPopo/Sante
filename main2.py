import tkinter
from fonctions import style_acceuil, fonctionnalite_medecin

window = tkinter.Tk()
window.title("Interface medecin")
window.geometry("720x480")
window.resizable(width=False, height=False)
window["bg"] = "#4E9F3D"

frame = tkinter.Frame(window, bg="#4E9F3D")

bnt1 = tkinter.Button(frame, text="Consultation du jour", command=fonctionnalite_medecin.consultation , **style_acceuil.style_bouton_accueil)
bnt1.grid(row=0, column=0, padx=20)

bnt2 = tkinter.Button(frame, text="Remplir un canet", **style_acceuil.style_bouton_accueil)
bnt2.grid(row=0, column=1)

frame.pack(expand="yes")


window.mainloop()