# FlattenList

Making complicated list flatten into list.

For example:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','ca"t',2,3,'dog'",4,5] 


Turkish:

Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) 
oluşabileceği gibi, non-scalar verilerden de oluşabilir. 

Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','ca"t',2,3,'dog'",4,5] 
