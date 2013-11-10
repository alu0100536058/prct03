import modulo_equal

i = 0
min_value = -150
max_value = 150
numero_test = 200
expr1 = 'a+b'
expr2 = 'b+a'
expresiones = ['a+b' , 'b+a' , 'a*b' , 'b*a']

print "Tabla de prueba de expresiones: "
print " expr1    expr2    min_value  max_value numero_test fallos"
while ( i < 4 ):
	expr1 = expresiones[ i ]
	expr2 = expresiones[ i + 1 ]
	print "  %s      %s      %6.1f     %6.1f     %d          %d" % (expr1, expr2, min_value, max_value, numero_test, modulo_equal.equal( expr1 , expr2 , min_value , max_value , numero_test ))  
	i = i + 2