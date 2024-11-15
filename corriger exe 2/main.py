from nettoyer_texte import nettoyer_texte
from compter_mots import compter_mots
from detecter_mot_suspect import detecter_mot_suspects

def analyse_texte():
    texte = input("entre un texte")
    nettoyer_texte(texte)
    compter_mots(texte)
    mot = input("entre le mot a rechercher")
    detecter_mot_suspects(mot)
    if detecter_mot_suspects(mot) in mot :
        return True
    else :
        return False