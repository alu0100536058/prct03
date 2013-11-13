import modulo_equal  

from math import *

min_value = 1
max_value = 15
numero_test = 133
expr1 = 'a+b'
expr2 = 'b+a'

expresiones = [ ('(a*b)**3','(a**3)*(b**3)') ,
('a/b','1/(b/a)') ,
('exp(a+b)','(exp(a))*(exp(b))'),
('(log(a**b))','b*(log(a))') ,
('a-b','-(b-a)') ,  
('(a*b)**4','(a**4)*(b**4)') , 
('(a+b)**2','(a**2)+(2*a*b)+(b**2)') , 
('(a+b)*(a-b)','(a**2)-(b**2)') , 
('log(a*b)','log(a)+log(b)') , 
('a*b','exp(log(a)+log(b))') ,
('1/((1/a)+(1/b))' , '(a*b)/(a+b)'),
<<<<<<< HEAD
('(a*(sin(b))**2)+((cos(b))**2)' , 'a') ,
=======
('a*(((sin(b))**2)+((cos(b))**2))' , 'a') ,
>>>>>>> 95c5274071c9a2a3c113a8b397145fccfc8724cd
('sinh(a+b)' , '(((exp(a)*exp(b))-(exp(-a)*exp(-b)))/2)') ,
('tan(a+b)' , '(sin(a+b))/(cos(a+b))') ,
('sin(a+b)' , 'sin(a)*cos(b)+sin(b)*cos(a)')
]

 
print 'Tabla de prueba de expresiones: \n{0:40} {1:40} {2:4}'.format('expr1', 'expr2', '%fallos')


for i in expresiones:      #recorre las tuplas
	expr1 = i[0] #asigna a expr1 el primer elemento de cada tupla
	expr2 = i[1] #asigna a expr2 el segundo elemento de cada tupla
	print '{0:40} {1:40} {2:4.4}'.format(expr1, expr2, modulo_equal.equal( expr1 , expr2 , min_value , max_value , numero_test ))
	 

