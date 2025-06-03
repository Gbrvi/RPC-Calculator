# server.py
from xmlrpc.server import SimpleXMLRPCServer


class Calculator():

    def add(self, x, y):
        """Soma dois números."""
        return x + y

    def subtract(self, x, y):
        """Subtrai dois números."""
        return x - y

    def multiply(self, x, y):
        """Multiplica dois números."""
        return x * y

    def divide(self, x, y):
        """Divide dois números."""
        if y == 0:
            raise ValueError("Não é possível dividir por zero.")
        return x / y

# Cria o servidor
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC ouvindo na porta 8000...")

# Registra as funções para que possam ser chamadas remotamente
c = Calculator()
server.register_function(c.add, "add")
server.register_function(c.subtract, "subtract")
server.register_function(c.multiply, "multiply")
server.register_function(c.divide, "divide")

# Inicia o servidor
server.serve_forever()