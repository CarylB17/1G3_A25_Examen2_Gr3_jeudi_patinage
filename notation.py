# notation.py
from typing import List

def valider_notes(notes: list[float]) -> bool:
    """
    Valider la liste de notes selon les regles du systeme :
    - exactement 9 notes;
    - chaque note est comprise entre 0 et 3 (bornes inlcuises).
    :param notes: liste de 9 notes (int/float)
    :returns: True si la liste et valide, False sinon
    """
    if not isinstance(notes, list):
        return False

    if len(notes) != 9:
        return False

    for n in notes:
        # Autoriser int/float, mais refuser les autres types
        if not isinstance(n, (int, float)):
            return False
        if n < 0 or n > 3:
            return False
    return True

def calculer_points(vbase: float, notes: list[float]) -> float:
    """
    Calcule la note finale d’un mouvement.

    - La liste de notes doit etre valide (voir valider_notes). Sinon -> ValueError.
    - On retire UNE (1) plus grande note.
    - On fait la moyenne des 7 notes restantes.
    - On additionne la vbase

    La liste "notes" fournie en argument ne doit pas etre modifiee.

    :param vbase: valeur de base (float)
    :param notes: liste de 9 notes (int/float) entre 0 et 3 inclus
    :returns: valeur de la note finale (float)
    :raises ValueError: si la liste de notes est invalide
    """
    if not valider_notes(notes):
        raise ValueError ("Liste de notes invalide")

    note_max = max(notes)
    note_min = min(notes)

    # Cree une nouvelle liste sans les valeurs extremes
    note_filtrees =[n for n in notes if n != note_max and n != note_min]

    moyenne = sum(note_filtrees) / len(note_filtrees)
    total = vbase + moyenne
    return total





