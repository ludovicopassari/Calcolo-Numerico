PROGRAM CN_2022_2023
    !Creo un parametro che corrisponde alla dimensione del vettore
    parameter(j=10)
    !Creo un array con j elementi, delle variabili che conterranno il valore immesso dall'utente e il massimo valore corrente
    REAL N(j),values,max
    !Chiedo all'utente j volte di inserire un valore da inserire nel vettore
    do i = 1,j
        WRITE(*,*) 'Immetti un numero:'
        READ(*,*) values
        N(i)= values
    end do

    !Considero come elemento più grande il primo elemento del vettore 
    max = N(1)
    !Per ogni elemento del vettore confronto il massimo corrente con l'elemento i-esimo  
    do i = 1,j
        !Se l'elemento i-esimo è maggiore del massimo aggiorno
        if(N(i) .GE. max) then
            max=N(i)
        end if
    end do
    
    print*, 'Il valore massimo: ',max
    
END PROGRAM CN_2022_2023
