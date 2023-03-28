! Studiare il massimo valore del fattoriale di n calcolabile da un elaboratore nel caso di variabili di tipo intero, reale e reale in doppia precisione, queste ultime in FORTRAN si dichiarano con il comando: REAL*8 lista.

PROGRAM CN_2022_2023

    INTEGER index
    INTEGER limit_number
    REAL *8 factorial

    factorial=1

    WRITE(*,*) "Inserisci un numero intero:  "
    READ(*,*) limit_number

    DO index = 1, limit_number,1
        factorial=index*factorial   
        print *, index,'!',factorial
    END DO
    
END PROGRAM CN_2022_2023