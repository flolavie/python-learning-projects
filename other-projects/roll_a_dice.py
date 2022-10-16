import random
from time import sleep
wlcm_msg="""

████████▄   ▄█   ▄████████    ▄████████ 
███   ▀███ ███  ███    ███   ███    ███ 
███    ███ ███▌ ███    █▀    ███    █▀  
███    ███ ███▌ ███         ▄███▄▄▄     
███    ███ ███▌ ███        ▀▀███▀▀▀     
███    ███ ███  ███    █▄    ███    █▄  
███   ▄███ ███  ███    ███   ███    ███ 
████████▀  █▀   ████████▀    ██████████ 


Copyright © 2022 Florian LAVIE
This program is released under license GPL-3.0-or-later

This program is part of a project called "Python Learning Projects"
Source code & license available at https://github.com/flolavie/python-learning-projects/
Author's contact: contact@flolavie.fr - www.flolavie.fr


Credits & Thanks
  ♥ Fancy text generated by 'Text ASCII Art Generator' from https://patorjk.com/

"""
print(wlcm_msg)

#=======================
#Language selection part
#=======================

def select_language():
    language=input("Select your language : \n- English type 'en'\n- Français tapez 'fr'\n-> ")
    
    match language:
        case "en":
            print("\n✔ You selected English\n")
            start_en()
        case "fr":
            print("\n✔ Vous avez sélectionné le Français.\n")
            start_fr()
        case _ :
            print("\n/!\ ERROR: Language not available. /!\ \n")
            select_language()
            

#============
# Main part
#============

# ENGLISH
def start_en():
    try:
        facenb=int(input("To roll the dice, select the number of faces on the dice :\n-> "))
    except:
        print("\n/!\ ERROR: Please enter a valid integer /!\ \n")
        start_en()
    else:
        print("\nRolling the dice...\n")
        sleep(2)
        dice_result=random.randint(1,facenb)
        print("\nThe dice rolled and the number is", dice_result, "\n")
        retry=input("Do you want to roll the dice again? (Yes/No)\n-> ")
        start_en() if retry=="yes" or retry=="y" or retry=="" else exit()
    
# FRENCH
def start_fr():
    try:
        facenb=int(input("Pour lancer le dé, renseignez le nombre de faces du dé :\n-> "))
    except:
        print("\n/!\ ERREUR: Renseignez un nombre entier /!\ \n")
        start_fr()
    else:
        print("\nLe dé tourne...\n")
        sleep(2)
        dice_result=random.randint(1,facenb)
        print("\nLe dé vient de s'arrêter, le nombre est", dice_result, "\n")
        retry=input("Voulez-vous relancer le dé ? (Oui/Non)\n-> ")
        start_fr() if retry=="oui" or retry=="o" or retry =="" else exit()

# START
select_language()