# client.py
import xmlrpc.client

# Conecta ao servidor RPC
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Chama as funções remotas
try:
    soma = proxy.add(4, 1)
    print(f"4 + 1 = {soma}")

    subtracao = proxy.subtract(1, 6)
    print(f"1 - 6 = {subtracao}")

    multiplicacao = proxy.multiply(2, 7)
    print(f"2 * 7 = {multiplicacao}")

    divisao = proxy.divide(24, 4)
    print(f"8 / 4 = {divisao}")

    # Exemplo de erro (divisão por zero)
    divisao_por_zero = proxy.divide(7, 0)
    print(f"7 / 0 = {divisao_por_zero}")

except xmlrpc.client.Fault as err:
    print("\nOcorreu um erro no servidor:")
    print(f"Código de falha: {err.faultCode}")
    print(f"String de falha: {err.faultString}")
except Exception as e:
    print(f"Ocorreu um erro no cliente: {e}")