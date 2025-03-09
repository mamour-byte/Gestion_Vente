from db import verifier_utilisateur
from accueil import afficher_accueil
import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox

# Configuration principale
set_appearance_mode("light")  
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
        
        
app = ctk.CTk()

# Définir la taille de la fenêtre
window_width = 400  # Agrandir la fenêtre
window_height = 500
app.geometry(f"{window_width}x{window_height}")

# Obtenir la taille de l'écran
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Calculer la position pour centrer la fenêtre
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)

# Appliquer la position
app.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

# Créer le cadre
frame = ctk.CTkFrame(master=app)
frame.pack(pady=30, padx=80, fill="both", expand=True)

# Agrandir la police du label
label = ctk.CTkLabel(master=frame, text="Se connecter", font=("Arial", 24))  # Police plus grande
label.pack(pady=20, padx=10)

# Agrandir les champs de texte
email_entry = ctk.CTkEntry(master=frame, placeholder_text="Identifiant", font=("Arial", 18), width=350, height=40)  # Police plus grande
email_entry.pack(pady=20)

mdp_entry = ctk.CTkEntry(master=frame, placeholder_text="Mot de passe", show="*", font=("Arial", 18) , width=350, height=40)  # Police plus grande
mdp_entry.pack(pady=20)

# Agrandir le bouton
button = ctk.CTkButton(master=frame, text="Connexion", command=verifier_authentification, font=("Arial", 18), width=250, height=50)  # Plus grand bouton
button.pack(pady=20, padx=10)

# Afficher l'application
app.mainloop()
