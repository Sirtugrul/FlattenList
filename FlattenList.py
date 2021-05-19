"""Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) 
oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','ca"t',2,3,'dog'",4,5] """


gliste = [1, [2, 3, [4, 5]], 6, [[7], [8, 9]]]
flat_liste = []

def flatten_liste(gliste):
    
    for i in gliste:
        
        if type(i) == list:
            flatten_liste(i)
        else:
            flat_liste.append(i)


flatten_liste(gliste)
print(flat_liste)

