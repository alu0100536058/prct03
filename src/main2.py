import modulo_equal  

# Valores por defecto

#i = 0
min_value = -150
max_value = 150
numero_test = 200
expr1 = 'a+b'
expr2 = 'b+a'

expresiones = [('a+b','b+a'),('a*b','b*a') , ('a**3*b**3','(a*b)**3') , ('a/b','1/(b/a)') , ('log(a**b)','b*log(a)')]

# expresiones = [ ('a**3*b**3','(a*b)**3') , ('a/b','1/(b/a)') , ('exp(a+b)','exp(a)*exp(b)') , ('log(a**b)','b*log(a)') , ('a-b','-(b-a)') , ('a**4*b**4','(a*b)**4') , ('(a+b)**2','a**2+2*a*b+b**2') , ('(a+b)*(a-b)','a**2-b**2') , ('log(a+b)','log(a)+log(b)') , ('a*b','exp**(log(a)+log(b))') ]


print "Tabla de prueba de expresiones: "
print " expr1  expr2 min_value  max_value numero_test %fallos"
for i in expresiones:      #recorre las tuplas
	expr1 = i[0] #asigna a expr1 el primer elemento de cada tupla
	expr2 = i[1] #asigna a expr2 el segundo elemento de cada tupla
	print "  %s      %s      %6.1f     %6.1f     %d          %d" % (expr1, expr2, min_value, max_value, numero_test, modulo_equal.equal( expr1 , expr2 , min_value , max_value , numero_test ))  
	