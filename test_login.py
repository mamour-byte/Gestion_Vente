import customtkinter as ctk

login = ctk.CTk()
login.geometry("500x600")


frame = ctk.CTkFrame(master=login)
frame.pack(pady=20 , padx = 60 , fill="both" , expand=True) 

label = ctk.CTkLabel(master=frame , text="Se connecter")
label.pack(pady = 12 , padx=10)

entry_name = ctk.CTkEntry(master=frame , placeholder_text="Identifiant")
entry_name.pack(pady=12)

entry_psw = ctk.CTkEntry(master=frame , placeholder_text="Mot de passe" , show="*")
entry_psw.pack(pady=12)

button = ctk.CTkButton(master=frame , text="Connexion" , command=)
button.pack(pady=12 , padx=10)

login.mainloop()