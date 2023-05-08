import math

class Vector(object):
    
    def __init__(self,vector=[]) -> None:
        self.__vector=vector
    
    def norma_uno(self,vector=[]):
        if len(vector) == 0:
            n = len(self.__vector)
            summatory = 0

            for i in range(n):
                summatory += abs(self.__vector[i])

            return summatory
        else:
            n = len(vector)
            summatory = 0

            for i in range(n):
                summatory += abs(vector[i])

            return summatory


    def norma_due(self,vector=[]):
        if len(vector)== 0:
            n = len(self.__vector)
            summatory = 0

            for i in range(n):
                summatory += self.__vector[i]*self.__vector[i]

            return math.sqrt(summatory)
        else:
            n = len(vector)
            summatory = 0

            for i in range(n):
                summatory += vector[i]*vector[i]

            return math.sqrt(summatory)

    def norma_inf(self,vector=[]):

        if len(vector) == 0:
            max_value = self.__vector[0]
            
            for x in self.__vector:
                temp=abs(x)
                if temp > max_value:
                    max_value=temp
            return max_value
        else:
            max_value = vector[0]
            
            for x in vector:
                temp=abs(x)
                if temp > max_value:
                    max_value=temp

            return max_value
        

    def check_corollario(self)->str:


        n = len(self.__vector)
        n_square= math.sqrt(n)
        norma_1 = self.norma_uno()
        norma_2 = self.norma_due()
        norma_inf = self.norma_inf()

        check_1 = norma_inf <= norma_2 <=  n_square*norma_inf
        check_2 = norma_2 <= norma_1 <=  n_square*norma_2
        check_3 = norma_inf <= norma_1 <= n* norma_inf
       
        return 'Check Corollario Teorema di Equivalenza delle Norme.'\
                '\n\nA=%s' % (self.__vector)+\
                '\n\n1.[ norma_inf(A) = %f <= norma_2(A) = %f <= √%d norma_inf(A) = %f ] --> %s' %(norma_inf,norma_2,n, n_square*norma_inf,check_1)+\
                '\n2.[ norma_2(A) = %f <= norma_1(A) = %f <= √%d * norma_2(A) = %f ] --> %s' %(norma_2,norma_1,n, n_square*norma_2,check_2)+\
                '\n3.[ norma_inf(A) = %f <= norma_1(A) = %f <= %d * norma_inf(A) = %f ] --> %s'% (norma_inf,norma_1,n,n*norma_inf,check_3)
    
    
    #esercizio gruppo due numero due 
    def confronta_norme(self):

        
        n_max = 20
        #estremi dell'intervallo
        a = -1
        b = 1
        #distanza tra i due numeri
        h = (b-a)/n_max
        #lista che conterrà tutti i vettori creati
        lista_vettori=[]
       
       #crean n vettori a partire da un numero di componenti uguale a due 
        for n in range(2,n_max+1):
            #calcolo per ogni vettore, in base alla dimensione , la distanza tra due numeri
            h = (b-a)/n
            i = 0
            vettore = []
            item = a
            #riempi il vettore n-esimo con i valori
            while i < n:
                item += h
                vettore.append(item)
                i+=1
                #appende il vettore alla lista dei vettori
            lista_vettori.append(vettore)  

        return lista_vettori             
          
            
        """         check_dict={}
        
        for vettore in lista_vettori:
            for item in vettore:
                if a<=item<=b:
                    check_dict[lista_vettori.index(vettore)]=True
                else:
                    check_dict[lista_vettori.index(vettore)]=False
        
        print(check_dict) """
        
    def norma_vettori(self,lista_vettori):
        
        with open('result.csv','w') as my_file:
            for vector in lista_vettori:
                norma_uno=self.norma_uno(vector)
                norma_due=self.norma_due(vector)
                norma_inf=self.norma_inf(vector)
                my_file.write(str(norma_uno)+':'+str(norma_due)+':'+str(norma_inf)+'\n')
            
        
   
                


  

     
        

