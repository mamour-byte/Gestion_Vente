import sqlite3
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

# Configuration de CustomTkinter
ctk.set_appearance_mode("light")  # Modes : "light", "dark", "system"
ctk.set_default_color_theme("green")  # Thème vert

# Connexion à la base de données
def get_produits():
    conn = sqlite3.connect("database/gestion_vente.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, prix, stock FROM produits")
    produits = cursor.fetchall()
    conn.close()
    return produits

def enregistrer_vente(produit_id, quantite, utilisateur_id, root):
    conn = sqlite3.connect("database/gestion_vente.db")
    cursor = conn.cursor()

    # Récupérer le produit
    cursor.execute("SELECT prix, stock FROM produits WHERE id=?", (produit_id,))
    produit = cursor.fetchone()
    
    if not produit:
        messagebox.showerror("Erreur", "Produit introuvable")
        return
    
    prix_unitaire, stock_disponible = produit

    if quantite > stock_disponible:
        messagebox.showerror("Erreur", "Stock insuffisant")
        return

    sous_total = prix_unitaire * quantite
    date_vente = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insérer la vente
    cursor.execute("INSERT INTO ventes (utilisateur_id, date_vente, total) VALUES (?, ?, ?)", 
                   (utilisateur_id, date_vente, sous_total))
    vente_id = cursor.lastrowid

    # Insérer le détail de la vente
    cursor.execute("INSERT INTO detail_ventes (vente_id, produit_id, quantite, prix_unitaire, sous_total) VALUES (?, ?, ?, ?, ?)",
                   (vente_id, produit_id, quantite, prix_unitaire, sous_total))

    # Mettre à jour le stock
    cursor.execute("UPDATE produits SET stock = stock - ? WHERE id=?", (quantite, produit_id))

    # Générer une facture
    cursor.execute("INSERT INTO factures (vente_id, date_facture, montant_total) VALUES (?, ?, ?)", 
                   (vente_id, date_vente, sous_total))

    conn.commit()
    conn.close()
    messagebox.showinfo("Succès", "Vente enregistrée avec succès!")
    root.destroy()

# Interface de vente
def afficher_interface_vente(utilisateur_id):
    vente_fenetre = ctk.CTk()
    vente_fenetre.title("Gestion des Ventes")
    vente_fenetre.geometry("400x250")

    produits = get_produits()

    ctk.CTkLabel(vente_fenetre, text="Sélectionnez un produit :", font=("Arial", 14)).pack(pady=5)

    produit_var = ctk.StringVar()
    produit_menu = ctk.CTkOptionMenu(vente_fenetre, variable=produit_var, 
                                     values=[f"{p[1]} - {p[2]}€ (Stock: {p[3]})" for p in produits])
    produit_menu.pack(pady=5)

    ctk.CTkLabel(vente_fenetre, text="Quantité :", font=("Arial", 14)).pack(pady=5)
    quantite_entry = ctk.CTkEntry(vente_fenetre, width=200)
    quantite_entry.pack(pady=5)

    def ajouter_vente():
        if not produit_var.get():
            messagebox.showerror("Erreur", "Veuillez sélectionner un produit")
            return
        
        quantite = quantite_entry.get()
        if not quantite.isdigit():
            messagebox.showerror("Erreur", "Veuillez entrer une quantité valide")
            return

        quantite = int(quantite)
        produit_id = [p[0] for p in produits if f"{p[1]} - {p[2]}€ (Stock: {p[3]})" == produit_var.get()][0]

        enregistrer_vente(produit_id, quantite, utilisateur_id, vente_fenetre)     

    bouton_valider = ctk.CTkButton(vente_fenetre, text="Enregistrer la vente", command=ajouter_vente, fg_color="#008000")
    bouton_valider.pack(pady=10)

    vente_fenetre.mainloop()

