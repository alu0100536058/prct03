import modulo_equal  

#import math as mt
from math import *


#exp = mt.exp
#log = mt.log
#sin = mt.sin
#cos = mt.cos
#tan = mt.tan
#asinh = mt.asinh

# Valores por defecto

#i = 0
min_value = 1
max_value = 150
numero_test = 200
expr1 = 'a+b'
expr2 = 'b+a'

expresiones = [ ('(a*b)**3','(a**3)*(b**3)') ,
('a/b','1/(b/a)') ,
('exp(a+b)','(exp(a))*(exp(b))'),
('log(a)**b','b*log(a)') ,
('a-b','-(b-a)') ,  
('(a*b)**4','(a**4)*(b**4)') , 
('(a+b)**2','(a**2)+(2*a*b)+(b**2)') , 
('(a+b)*(a-b)','(a**2)-(b**2)') , 
('log(a*b)','log(a)+log(b)') , 
('a*b','exp(log(a)+log(b))') ,
('1/((1/a)+(1/b))' , '(a*b)/(a+b)'),
('(a*(sin(b))**2)+((cos(b))**2)' , 'a') ,
('sinh(a+b)' , '(((exp(a)*exp(b))-(exp(-a)*exp(-b)))/2)') ,
('tan(a+b)' , '(sin(a+b))/(cos(a+b))') ,
('sin(a+b)' , 'sin(a)*cos(b)+sin(b)*cos(a)')
]

#('a*(sin**2(a)+cos**2(b))' , 'a')
 


print "Tabla de prueba de expresiones: "
print "%s %20s %20s" % ("expr1", "expr2", "% fallos")

for i in expresiones:      #recorre las tuplas
	expr1 = i[0] #asigna a expr1 el primer elemento de cada tupla
	expr2 = i[1] #asigna a expr2 el segundo elemento de cada tupla
	print "%s %20s %20d" % (expr1, expr2, modulo_equal.equal( expr1 , expr2 , min_value , max_value , numero_test ))  


#print "Tabla de prueba de expresiones: "
#print "%s %20s %20s %10s %10s %10s" % ("expr1", "expr2", "min_value", "max_value", "num_test", "% fallos")

#for i in expresiones:      #recorre las tuplas
#	expr1 = i[0] #asigna a expr1 el primer elemento de cada tupla
#	expr2 = i[1] #asigna a expr2 el segundo elemento de cada tupla
#	print "%s %20s %20.1f %10.1f %10d %10d" % (expr1, expr2, min_value, max_value, numero_test, modulo_equal.equal( expr1 , expr2 , min_value , max_value , numero_test ))  