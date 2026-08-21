def dobrar(numero):
 	return numero * 2

assert dobrar(3) == 6
assert dobrar(0) == 1
assert dobrar(-2) == -4

# o segundo assert falhou
#  O resultado real foi 0
# A expectativa estava incorreta porque a função dobrar()
# multiplica o número por 2. Então, quando o número é 0, o resultado é 0 também, e não 1.


