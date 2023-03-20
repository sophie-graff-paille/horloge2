from tkinter import *
from time import *
from pygame import mixer

# Création de la fenêtre avec Tkinter
window = Tk()
window.title("Horloge")
window.geometry("500x500")

# création des labels heure et date
label_heure = Label(window, text="", font=("Comic sans MS", 50), bg="black", fg="green")
label_heure.pack(pady=20)

label_date = Label(window, text="", font=("Comic sans MS", 14))
label_date.pack(pady=10)

# création de ma frame pour les boutons pause et choix 12h/24h
frame_boutons = Frame(window)
frame_boutons.pack(pady=10)

# fonction pour afficher l'heure
def afficher_heure():
    global heure, jour, date, mois, annee # global pour pouvoir utiliser les variables dans les autres fonctions
    if not paused: # si la variable paused est à False
        if bouton_choix["text"] == "choix 24h": # et si sur le bouton choix apparaît 24h
            heure = strftime("%I:%M:%S %p") # alors on affiche l'heure en 12h
        else :
            heure = strftime("%H:%M:%S") # sinon en 24h

    # affichage de la date
    jour = strftime("%A")
    date = strftime("%d")
    mois = strftime("%B")
    annee = strftime("%Y")
    # création du label pour afficher la date complète
    label_heure.config(text=heure)
    label_date.config(text= jour + " " + date + " " + mois + " " + annee)
    window.after(1000, afficher_heure) # rappelle la fonction afficher_heure toutes les secondes

# fonction pour mettre l'horloge en pause
def pause():
    global paused, heure # global pour pouvoir utiliser la variable dans les autres fonctions
    if not paused: # si la variable paused est à False
        bouton_pause.config(text="play", bg="red") # alors le texte du bouton pause est play et le bouton passe en rouge
        paused = True # la variable paused passe à True
    else:
        bouton_pause.config(text="pause", bg="green") # sinon le texte du bouton pause est pause et le bouton passe en vert
        paused = False # la variable paused passe à False
        afficher_heure() # et on rappelle la fonction afficher_heure pour que l'horloge reprenne

paused = False # variable pour mettre l'horloge en pause

# création du boutons pause
bouton_pause = Button(frame_boutons, text="pause", command=pause, borderwidth=10, width=10, bg="green", fg="white", font=("Comic sans MS", 10))
bouton_pause.pack(side=LEFT, pady=10)

# fonction pour changer le format de l'heure
def choix_1224():
    global heure # global pour pouvoir utiliser la variable dans les autres fonctions
    if bouton_choix["text"] == "choix 12h": # si sur le bouton choix apparaît 12h
        bouton_choix["text"]= "choix 24h" # alors on change le texte du bouton choix en 24h
    else:
        bouton_choix["text"]= "choix 12h" # sinon on change le texte du bouton choix en 12h
    afficher_heure() # et on rappelle la fonction afficher_heure pour que l'horloge reprenne

# création du bouton choix 12h/24h
bouton_choix = Button(frame_boutons, text="choix 12h", command=choix_1224, borderwidth=10, width=10, bg="green", fg="white", font=("Comic sans MS", 10))
bouton_choix.pack(side=RIGHT, pady=10)

# fonction pour créer une alarme
def alarm():
    alarm_time = alarm_entry.get() # récupère l'heure dans l'entry de l'alarme
    if alarm_time == strftime("%H:%M:%S"): # si l'heure de l'alarme est égale à l'heure actuelle en 24h
        mixer.init() # initialisation de pygame
        mixer.music.load("sons/1651.wav") # chargement du son
        mixer.music.play() # lecture du son
        open_popup() # ouverture de la popup
        remise_a_zero() # remise à zéro de l'entry de l'alarme
    elif alarm_time == strftime("%I:%M:%S %p"): # et si l'heure de l'alarme est égale à l'heure actuelle en 12h
        mixer.init()
        mixer.music.load("sons/coucou.wav") # chargement d'un autre son pour différencier les deux formats d'heure
        mixer.music.play()
        open_popup()
        remise_a_zero()
    else:
        window.after(1000, alarm) #

# création du label et de l'entry pour l'alarme
label_alarm = Label(window, text="Entrez votre heure d'alarme", font=("Comic sans MS", 14))
label_alarm.pack(pady=10)

alarm_entry = Entry(window, width=25, borderwidth=5)
alarm_entry.pack(pady=10)

# création du bouton pour enregistrer l'alarme
bouton_alarm = Button(window, text="Enregistrer l'alarme", command=alarm, borderwidth=10, width=16, bg="green", fg="white", font=("Comic sans MS", 10))
bouton_alarm.pack(pady=15)

# fonction pour ouvrir une popup
def open_popup():
   top= Toplevel(window) # création d'une fenêtre secondaire
   top.geometry("350x100")
   top.title("Avis")
   # création d'un label pour afficher le message
   Label(top, text= "L'heure de votre alarme a bien été prise en compte", font=("Comic Sans MS", 10), bg="blue", fg="white").pack(pady=10)

# fonction pour remettre à zéro l'entry de l'alarme
def remise_a_zero():
    alarm_entry.delete(0, END) # supprime le texte de l'entry

afficher_heure() # appel de la fonction afficher_heure

window.mainloop()