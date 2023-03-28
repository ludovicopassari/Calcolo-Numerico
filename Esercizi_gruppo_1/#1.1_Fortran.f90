! Dati due numeri interi dire se il primo èmultiplo del secondo. Caso particolare dato un numero intero dire se è pari o dispari.

PROGRAM CN_2022_2023
    ! dichiaro due variabili x e y che conterranno i due valori inseriti successivamente dall'utente
    INTEGER x,y
    !Assegnamento primo valore in x
    WRITE(*,*) 'Immetti Il primo numero: '
    READ(*,*) x
    !Assegnamento secondo valore ad y
    WRITE(*,*) 'Immetti Il secondo numero: '
    READ(*,*) y
   
    ! Verifico che il resto della divisione tra x e y sia 0, ciò significa che x è multiplo di y
    if (mod(x,y) .EQ. 0) then
        WRITE(*,*) x,' è multiplo di ',y
    else
        WRITE(*,*) x,' non è multiplo di ',y
    end if

END PROGRAM CN_2022_2023