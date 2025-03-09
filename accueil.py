from ventes import afficher_interface_vente
from historique import get_historique_ventes
from customtkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import openpyxl
from tkinter import filedialog

def afficher_accueil(nom_utilisateur, utilisateur_id):
    # Configuration principale
    accueil = CTk()
    accueil.title("Accueil")
    accueil.geometry("700x400")

    # Cadre principal
    main_frame = CTkFrame(master=accueil)
    main_frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Section gauche : Menu vertical
    left_frame = CTkFrame(master=main_frame, width=150)
    left_frame.pack(side="left", fill="y", padx=10, pady=10)

    CTkLabel(master=left_frame, text=f"Bienvenue, {nom_utilisateur}!", font=("Arial Bold", 14)).pack(pady=20)

    btn_ventes = CTkButton(master=left_frame, text="Gérer les ventes", command=lambda: afficher_interface_vente(utilisateur_id), width=120, height=40)
    btn_ventes.pack(pady=10)

    btn_quitter = CTkButton(master=left_frame, text="Quitter", command=accueil.destroy, fg_color="red", hover_color="darkred", width=120, height=40)
    btn_quitter.pack(pady=10)

    # Section droite : Liste des ventes
    right_frame = CTkFrame(master=main_frame)
    right_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    CTkLabel(master=right_frame, text="Ventes effectuées", font=("Arial Bold", 16)).pack(pady=10)

    # Tableau des ventes (Treeview)
    columns = ("ID", "Date Vente", "Vendeur", "Produit")
    tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=10)

    # Configuration des colonnes
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")

    tree.pack(pady=5, padx=5, fill="both", expand=True)  # Déplacer tree.pack() ici

    # Fonction pour charger les ventes
    def charger_ventes():
        """Récupère et affiche l'historique des ventes"""
        # Supprimer les anciennes entrées
        for row in tree.get_children():
            tree.delete(row)

        ventes_table = get_historique_ventes()  

        for vente in ventes_table:
            # Formater la date si nécessaire
            date_formatee = datetime.strptime(vente[1], "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")
            tree.insert("", "end", values=(vente[0], date_formatee, vente[3], vente[4]))  # Ajuste l'ordre

    # Charger les ventes une première fois
    charger_ventes()

    # Fonction pour exporter les ventes vers un fichier Excel
    def export_to_excel():
        # Récupérer les ventes
        ventes_table = get_historique_ventes()
        
        # Créer un classeur Excel
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Ventes"

        # Ajouter les en-têtes de colonne
        ws.append(["ID", "Date Vente", "Vendeur", "Produit"])

        # Ajouter les données des ventes
        for vente in ventes_table:
            date_formatee = datetime.strptime(vente[1], "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")
            ws.append([vente[0], date_formatee, vente[3], vente[4]])

        # Demander à l'utilisateur où enregistrer le fichier
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

        if file_path:
            wb.save(file_path)
            print(f"Fichier Excel enregistré à {file_path}")

    # Bouton d'extraction
    btn_extraction = CTkButton(master=right_frame, text="Extraction", command=export_to_excel)
    btn_extraction.pack(pady=5)

    # Bouton d'actualisation
    btn_refresh = CTkButton(master=right_frame, text="Actualiser", command=charger_ventes)
    btn_refresh.pack(pady=5)

    accueil.mainloop()
