PROGRAM CN_2022_2023
    
    real *4division
    real *4one
    one=1
    division =1
    
    DO WHILE((1+division).NE.1)

        division=division/2

    END DO

    if ( 1+division.eq.1) then
        
        print*,'ok'
        
    end if
    print*, 1+division
    division=division*2

    print*,division
    
    
END PROGRAM CN_2022_2023
