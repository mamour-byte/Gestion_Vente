from db import verifier_utilisateur
from accueil import afficher_accueil
from customtkinter import *
from tkinter import messagebox

# Configuration principale
set_appearance_mode("light")  # "dark" ou "light"
set_default_color_theme("green")

# Fonction d'authentification
def verifier_authentification():
    email = email_entry.get()
    mot_de_passe = mdp_entry.get()

    utilisateur = verifier_utilisateur(email, mot_de_passe)
    
    if utilisateur:
        messagebox.showinfo("Succès", "Connexion réussie !")
        app.destroy()
        afficher_accueil(utilisateur[1], utilisateur[0])   
    else:
        messagebox.showerror("Erreur", "Email ou mot de passe incorrect.")

# Création de la fenêtre principale
app = CTk()
app.geometry("500x400")
app.title("Authentification")

# Cadre principal
frame = CTkFrame(master=app)
frame.pack(expand=True, padx=20, pady=20, fill="both")

# Titre
title_label = CTkLabel(master=frame, text="Connexion", font=("Arial Bold", 22))
title_label.pack(pady=(10, 20))

# Cadre pour les champs de saisie
input_frame = CTkFrame(master=frame)
input_frame.pack(pady=20, padx=20, fill="both")

# Champ Email
CTkLabel(master=input_frame, text="Email :", anchor="w").grid(row=0, column=0, sticky="w", pady=5)
email_entry = CTkEntry(master=input_frame, placeholder_text="Entrez votre email", width=250)
email_entry.grid(row=1, column=0, pady=5)

# Champ Mot de passe
CTkLabel(master=input_frame, text="Mot de passe :", anchor="w").grid(row=2, column=0, sticky="w", pady=5)
mdp_entry = CTkEntry(master=input_frame, placeholder_text="Entrez votre mot de passe", show="*", width=250)
mdp_entry.grid(row=3, column=0, pady=5)

# Bouton Connexion
login_button = CTkButton(master=frame, text="Se connecter", command=verifier_authentification, width=250)
login_button.pack(pady=20)

# Lancer l'application
app.mainloop()
