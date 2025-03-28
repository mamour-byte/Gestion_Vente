from customtkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def afficher_interface_produits():
    # Configuration principale
    produits = CTk()
    produits.title("Gestion des Produits")
    
    # Définir la taille de la fenêtre
    window_width = 800
    window_height = 500
    produits.geometry(f"{window_width}x{window_height}")

    # Obtenir la taille de l'écran
    screen_width = produits.winfo_screenwidth()
    screen_height = produits.winfo_screenheight()

    # Calculer la position pour centrer la fenêtre
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)

    # Appliquer la position
    produits.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    # Cadre principal
    main_frame = CTkFrame(master=produits)
    main_frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Section gauche : Menu vertical
    left_frame = CTkFrame(master=main_frame, width=150)
    left_frame.pack(side="left", fill="y", padx=10, pady=10)

    CTkLabel(master=left_frame, text="Produits", font=("Arial Bold", 14)).pack(pady=20)

    btn_ajouter = CTkButton(master=left_frame, text="Ajouter", command=lambda: ajouter_produit(), width=120, height=40)
    btn_ajouter.pack(pady=10)

    btn_modifier = CTkButton(master=left_frame, text="Modifier", command=lambda: modifier_produit(), width=120, height=40)
    btn_modifier.pack(pady=10)

    btn_supprimer = CTkButton(master=left_frame, text="Supprimer", command=lambda: supprimer_produit(), width=120, height=40)
    btn_supprimer.pack(pady=10)

    btn_quitter = CTkButton(master=left_frame, text="Quitter", command=produits.destroy, fg_color="red", hover_color="darkred", width=120, height=40)
    btn_quitter.pack(pady=10)

    # Section droite : Liste des produits
    right_frame = CTkFrame(master=main_frame)
    right_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    CTkLabel(master=right_frame, text="Liste des Produits", font=("Arial Bold", 16)).pack(pady=10)

    # Tableau des produits (Treeview)
    columns = ("ID", "Nom", "Prix", "Quantité")
    tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=10)

    # Configuration des colonnes
    for col in columns:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, width=150, anchor="center")

    # Ajouter les bordures et styles
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"), padding=5, borderwidth=2, relief="solid")
    style.configure("Treeview", font=("Arial", 10), rowheight=25, borderwidth=2, relief="solid")

    tree.pack(pady=5, padx=5, fill="both", expand=True)

    # Fonction pour charger les produits
    def charger_produits():
        """Récupère et affiche la liste des produits"""
        # Supprimer les anciennes entrées
        for row in tree.get_children():
            tree.delete(row)

        # Exemple de données (à remplacer par une récupération depuis une base de données)
        produits_table = [
            (1, "Produit A", 1000, 50),
            (2, "Produit B", 2000, 30),
            (3, "Produit C", 1500, 20),
        ]

        for produit in produits_table:
            tree.insert("", "end", values=produit)

    # Charger les produits une première fois
    charger_produits()

    # Fonction pour ajouter un produit
    def ajouter_produit():
        def confirmer_ajout():
            nom = entry_nom.get()
            prix = entry_prix.get()
            quantite = entry_quantite.get()

            if nom and prix.isdigit() and quantite.isdigit():
                # Ajouter le produit (à remplacer par une insertion dans une base de données)
                print(f"Produit ajouté : {nom}, {prix} F cfa, {quantite} unités")
                charger_produits()
                popup.destroy()
            else:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs correctement.")

        popup = CTkToplevel(produits)
        popup.title("Ajouter un Produit")
        popup.geometry("300x200")

        CTkLabel(master=popup, text="Nom :").pack(pady=5)
        entry_nom = CTkEntry(master=popup)
        entry_nom.pack(pady=5)

        CTkLabel(master=popup, text="Prix :").pack(pady=5)
        entry_prix = CTkEntry(master=popup)
        entry_prix.pack(pady=5)

        CTkLabel(master=popup, text="Quantité :").pack(pady=5)
        entry_quantite = CTkEntry(master=popup)
        entry_quantite.pack(pady=5)

        CTkButton(master=popup, text="Ajouter", command=confirmer_ajout).pack(pady=10)

    # Fonction pour modifier un produit
    def modifier_produit():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Erreur", "Veuillez sélectionner un produit à modifier.")
            return

        produit = tree.item(selected_item)["values"]

        def confirmer_modification():
            nom = entry_nom.get()
            prix = entry_prix.get()
            quantite = entry_quantite.get()

            if nom and prix.isdigit() and quantite.isdigit():
                # Modifier le produit (à remplacer par une mise à jour dans une base de données)
                print(f"Produit modifié : {nom}, {prix} F cfa, {quantite} unités")
                charger_produits()
                popup.destroy()
            else:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs correctement.")

        popup = CTkToplevel(produits)
        popup.title("Modifier un Produit")
        popup.geometry("300x200")

        CTkLabel(master=popup, text="Nom :").pack(pady=5)
        entry_nom = CTkEntry(master=popup)
        entry_nom.insert(0, produit[1])
        entry_nom.pack(pady=5)

        CTkLabel(master=popup, text="Prix :").pack(pady=5)
        entry_prix = CTkEntry(master=popup)
        entry_prix.insert(0, produit[2])
        entry_prix.pack(pady=5)

        CTkLabel(master=popup, text="Quantité :").pack(pady=5)
        entry_quantite = CTkEntry(master=popup)
        entry_quantite.insert(0, produit[3])
        entry_quantite.pack(pady=5)

        CTkButton(master=popup, text="Modifier", command=confirmer_modification).pack(pady=10)

    # Fonction pour supprimer un produit
    def supprimer_produit():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Erreur", "Veuillez sélectionner un produit à supprimer.")
            return

        produit = tree.item(selected_item)["values"]
        confirmation = messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer le produit {produit[1]} ?")

        if confirmation:
            # Supprimer le produit (à remplacer par une suppression dans une base de données)
            print(f"Produit supprimé : {produit[1]}")
            charger_produits()

    produits.mainloop()