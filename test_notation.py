# test_notation.py
# Tests unitaires pour le module notation.py

import pytest
from notation import calculer_points, valider_notes

# ------------- Test (bonne)----------------
def test_calculer_points_cas_normal():
    vbase = 3.2
    notes = [3,2,1,2,3,3,2,2,3]
    # 5.63 -> on verifier a 2 decimals
    assert calculer_points(vbase, notes) == pytest.approx(5.63, abs=1e-2)
def test_calculer_points_plusieurs_max_min_identiques():
    vbase = 2.5
    notes = [3,3,3,2,2,2,1,1,1]
    # moyenne des 7 restants = 2.0 -> total 4.5
    assert calculer_points(vbase, notes) == pytest.approx(4.50, abs=1e-2)
def test_valider_notes_bornes_acceptable():
    # valeurs exactement aux bornes 0 et 3, taille -> 9 valide
    notes = [0,3,2,2,1,1,2,3,0]
    assert valider_notes(notes) is True
def test_calculer_points_ne_modifie_pas_la_liste():
    vbase = 3.0
    notes = [3,2,2,2,2,2,2,2,0]
    original = notes.copy()
    _=calculer_points(vbase, notes)
    assert notes == original, "calculer_points ne doit pas modifier la liste d'entree"

#------------- Test (erreur)----------------
@pytest.mark.parametrize("notes", [
    [2,2,2,2,2,2,2,2],
    [3,3,3,3,3,3,3,3, 4 ],
    [2,2,2,2,2,2,2,2,-1],
])
def test_calculer_points_erreurs(notes):
    with pytest.raises(ValueError):
        calculer_points(2.5, notes)


