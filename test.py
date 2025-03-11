
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Interface Ventes avec formulaire a implemanter apres et ajouter les actions sur la base de données 



def afficher_interface_vente(utilisateur_id):
    vente_fenetre = ctk.CTk()
    vente_fenetre.title("Gestion des Ventes")
    
    # Définir la taille de la fenêtre
    window_width = 500  
    window_height = 350
    vente_fenetre.geometry(f"{window_width}x{window_height}")

    # Obtenir la taille de l'écran
    screen_width = vente_fenetre.winfo_screenwidth()
    screen_height = vente_fenetre.winfo_screenheight()

    # Calculer la position pour centrer la fenêtre
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)

    # Appliquer la position
    vente_fenetre.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
    
    produits = get_produits()

    ctk.CTkLabel(vente_fenetre, text="Sélectionnez un produit :", font=("Arial", 14)).pack(pady=5)

    produit_var = ctk.StringVar()
    produit_menu = ctk.CTkOptionMenu(vente_fenetre, variable=produit_var, 
                                     values=[f"{p[1]} - {p[2]}€ (Stock: {p[3]})" for p in produits])
    produit_menu.pack(pady=5)

    ctk.CTkLabel(vente_fenetre, text="Quantité :", font=("Arial", 14)).pack(pady=5)
    quantite_entry = ctk.CTkEntry(vente_fenetre, width=200)
    quantite_entry.pack(pady=5)

    ctk.CTkLabel(vente_fenetre, text="Nom du client :", font=("Arial", 14)).pack(pady=5)
    nom_client_entry = ctk.CTkEntry(vente_fenetre, width=200)
    nom_client_entry.pack(pady=5)

    ctk.CTkLabel(vente_fenetre, text="Numéro de téléphone :", font=("Arial", 14)).pack(pady=5)
    numero_telephone_entry = ctk.CTkEntry(vente_fenetre, width=200)
    numero_telephone_entry.pack(pady=5)

    ctk.CTkLabel(vente_fenetre, text="Adresse :", font=("Arial", 14)).pack(pady=5)
    adresse_entry = ctk.CTkEntry(vente_fenetre, width=200)
    adresse_entry.pack(pady=5)

    def ajouter_vente():
        if not produit_var.get():
            messagebox.showerror("Erreur", "Veuillez sélectionner un produit")
            return
        
        quantite = quantite_entry.get()
        if not quantite.isdigit():
            messagebox.showerror("Erreur", "Veuillez entrer une quantité valide")
            return

        nom_client = nom_client_entry.get()
        numero_telephone = numero_telephone_entry.get()
        adresse = adresse_entry.get()

        if not nom_client or not numero_telephone or not adresse:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs du client")
            return

        quantite = int(quantite)
        produit_id = [p[0] for p in produits if f"{p[1]} - {p[2]}€ (Stock: {p[3]})" == produit_var.get()][0]

        enregistrer_vente(produit_id, quantite, utilisateur_id, nom_client, numero_telephone, adresse, vente_fenetre)

    bouton_valider = ctk.CTkButton(vente_fenetre, text="Enregistrer la vente", command=ajouter_vente, fg_color="#008000")
    bouton_valider.pack(pady=10)

    vente_fenetre.mainloop()
