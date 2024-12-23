# Initialize the bank
from src.EbankMain import EBank

bancoLB = EBank('Banco Luso-Brasileiro das Ilusoes')

# Open a new account for Huguinho
conta_Huguinho = bancoLB.abrir_conta("Huguinho", "123456789")
assert bancoLB.numero_de_contas_ativas() == 1

# Attempt to close Huguinho's account with an invalid PIN (before setting it)
assert not bancoLB.encerrar_conta(conta_Huguinho.numero_da_conta, "123")

# Set a valid PIN for Huguinho
assert conta_Huguinho.definir_pin("Abc123!")

# Attempt to close Huguinho's account with an incorrect PIN
assert not bancoLB.encerrar_conta(conta_Huguinho.numero_da_conta, "Abc")

# Close Huguinho's account with the correct PIN
assert bancoLB.encerrar_conta(conta_Huguinho.numero_da_conta, "Abc123!")
assert bancoLB.numero_de_contas_ativas() == 0

# Open accounts for Zezinho and Luisinho
conta_Zezinho = bancoLB.abrir_conta("Zezinho", "123456789")
conta_Luisinho = bancoLB.abrir_conta("Luisinho", "987654321")
assert bancoLB.numero_de_contas_ativas() == 2

# Verify account details
assert conta_Zezinho.nome == "Zezinho"
assert conta_Luisinho.nif == "987654321"

# Set invalid PINs for Zezinho
assert not conta_Zezinho.definir_pin("123")  # Too short
assert not conta_Zezinho.definir_pin("Abcdefghijk")  # Too long
assert not conta_Zezinho.definir_pin("abcdef")  # No uppercase letter
assert not conta_Zezinho.definir_pin("ABCDEF")  # No lowercase letter
assert not conta_Zezinho.definir_pin("Abcdef")  # No special character

# Set valid PINs for Zezinho and Luisinho
assert conta_Zezinho.definir_pin("Abc123!")
assert conta_Luisinho.definir_pin("abC123*")

# Perform a deposit and withdrawal for Zezinho
assert conta_Zezinho.depositar(5000)
assert conta_Zezinho.consulta() == 5000
conta_Zezinho.levantar(30)
assert conta_Zezinho.consulta() == 4970

# Test transfer between accounts with processing later
assert bancoLB.transferencia(conta_Zezinho.numero_da_conta, conta_Luisinho.numero_da_conta, 1000, False)
assert conta_Zezinho.consulta() == 4970
bancoLB.processamento()
assert conta_Luisinho.consulta() == 1000
assert conta_Zezinho.consulta() == 3970

# Open a new account for Patricia
conta_Patricia = bancoLB.abrir_conta("Patricia", "192837465")
assert bancoLB.numero_de_contas_ativas() == 3

# Attempt to access Patricia's account with an invalid PIN
acesso = bancoLB.aceder_conta(conta_Patricia.numero_da_conta, "123")
assert not acesso

# Set a valid PIN for Patricia
ps = "Ab1$@!*"
assert conta_Patricia.definir_pin(ps)

# Test instant transfer from Zezinho to Patricia
assert bancoLB.transferencia(conta_Zezinho.numero_da_conta, conta_Patricia.numero_da_conta, 500, True)
assert conta_Zezinho.consulta() == 3470
assert conta_Patricia.consulta() == 500

# Access Patricia's account with the correct PIN
conta_PatriciaB = bancoLB.aceder_conta(conta_Patricia.numero_da_conta, ps)
assert conta_Patricia == conta_PatriciaB

# Close Patricia's account
assert bancoLB.encerrar_conta(conta_PatriciaB.numero_da_conta, ps)
assert bancoLB.numero_de_contas_ativas() == 2

# Print Zezinho's transaction history
conta_Zezinho.historico()

# Additional Tests
# Reopen Huguinho's account with a different NIF and validate operations
conta_Huguinho2 = bancoLB.abrir_conta("Huguinho", "987654321")
# Use a valid PIN with a length of 6 to 8 characters
assert conta_Huguinho2.definir_pin("Passw0$")
assert bancoLB.numero_de_contas_ativas() == 3

# Deposit, withdraw and transfer with new Huguinho account
assert conta_Huguinho2.depositar(2000)
assert conta_Huguinho2.consulta() == 2000
conta_Huguinho2.levantar(500)
assert conta_Huguinho2.consulta() == 1500

# Transfer from Huguinho to Luisinho and validate balances
assert bancoLB.transferencia(conta_Huguinho2.numero_da_conta, conta_Luisinho.numero_da_conta, 1000, True)
assert conta_Huguinho2.consulta() == 500
assert conta_Luisinho.consulta() == 2000

# Close Huguinho's new account
assert bancoLB.encerrar_conta(conta_Huguinho2.numero_da_conta, "Passw0$")
assert bancoLB.numero_de_contas_ativas() == 2

print("All tests passed successfully.")
