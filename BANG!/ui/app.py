from tkinter import *

#Creer une premiere fenetre
window = Tk()

#personnaliser cette fenetre
window.title("BANG!")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("c:/Users/Paul/Desktop/YDAYS/Algo&Jeu de société/BANG!/ui/logo.ico")
window.config(background='#41B77F')

#ajouter un premier texte
label_title = Label(window, text="Bienvenue sur l'application", font=("Western Bang Bang", 40), bg='#41B77F', fg='white')
label_title.pack(expand=YES)

#ajouter un second texte
label_subtitle = Label(window, text="Hey toi", font=("Western Bang Bang", 25), bg='#41B77F', fg='white')
label_subtitle.pack(expand=YES)

#afficher
window.mainloop()