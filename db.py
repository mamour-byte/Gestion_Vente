import sqlite3
import os

def init_db():


    if not os.path.exists("database"):
        os.makedirs("database")

    # Connexion à la base de données
    dataBase = sqlite3.connect("database/gestion_vente.db")
    cursor = dataBase.cursor()

    # Création des tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mot_de_passe TEXT NOT NULL
        )
    ''')

    # Insertion des utilisateurs si la table est vide
    cursor.execute("SELECT COUNT(*) FROM utilisateurs")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO utilisateurs (nom, email, mot_de_passe) VALUES (?, ?, ?)
        ''', [
            ('Admin', 'admin@gmail.com', 'admin123'),
            ('Mamour Fall', 'mamour@gmail.com', 'mamour123'),
            ('User Test', 'test@gmail.com', 'test123')
        ])

    # Création des autres tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prix REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')

    # Insertion de quelques produits 
    cursor.execute("SELECT COUNT(*) FROM produits")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO produits (nom, prix,stock) VALUES (?, ?, ?)
        ''', [
            ('Sopalin 100', '2500', '50'),
            ('Sopalin 200', '3500', '50'),
            ('Cleanex 50', '2000', '100'),
            ('Cleanex 100', '3000', '100')
        ])

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            utilisateur_id INTEGER,
            date_vente TEXT,
            total REAL,
            FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detail_ventes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vente_id INTEGER,
            produit_id INTEGER,
            quantite INTEGER,
            prix_unitaire REAL,
            sous_total REAL,
            FOREIGN KEY (vente_id) REFERENCES ventes(id),
            FOREIGN KEY (produit_id) REFERENCES produits(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS factures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vente_id INTEGER,
            date_facture TEXT,
            montant_total REAL,
            FOREIGN KEY (vente_id) REFERENCES ventes(id)
        )
    ''')

    # Validation des modifications
    dataBase.commit()
    dataBase.close()

def verifier_utilisateur(email, mot_de_passe):
    dataBase = sqlite3.connect("database/gestion_vente.db")
    cursor = dataBase.cursor()
    cursor.execute("SELECT * FROM utilisateurs WHERE email=? AND mot_de_passe=?", (email, mot_de_passe))
    utilisateur = cursor.fetchone()
    dataBase.close()
    return utilisateur