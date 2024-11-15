from compter_mots import compter_mots
texte=compter_mots()
def nettoyer_texte(textes):
    textes.replace("."," ")
    texte=textes.lower()
    return texte

