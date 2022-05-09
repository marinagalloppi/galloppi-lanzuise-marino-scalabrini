import pgzrun

from galloppiLanzuiseMarinoScalabriniUtils import*


if _name_=='_galloppi-lanzuise-marino-scalabrini-main_':
    inizializza()

    while(game==on):
        if (muoviPersonaggio()):
            if (raccogliCaramella()):
                aggiornaPunteggio()
                if (verificaLivello() is true):
                            aggiornaLivello()
                else: pass
            else: pass
            if(colpisciOstacolo()):
                stopGame()
            else: pass
        else: pass
     else: GAMEOVER()

    

