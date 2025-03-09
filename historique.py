import sqlite3
import tkinter as tk
from tkinter import ttk

def get_historique_ventes():
    """Récupère l'historique des ventes avec les détails des produits."""
    conn = sqlite3.connect("database/gestion_vente.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT v.id, v.date_vente, v.total, u.nom, 
               GROUP_CONCAT(p.nom || ' (x' || dv.quantite || ')') AS produits
        FROM ventes v
        JOIN utilisateurs u ON v.utilisateur_id = u.id
        JOIN detail_ventes dv ON v.id = dv.vente_id
        JOIN produits p ON dv.produit_id = p.id
        GROUP BY v.id
        ORDER BY v.date_vente DESC
    """)
    
    ventes = cursor.fetchall()
    conn.close()
    return ventes

