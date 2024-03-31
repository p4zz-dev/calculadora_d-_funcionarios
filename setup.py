id_usuario = input("Digite seu usuário:")
admin = ("cal777cal")

if id_usuario == "cal777cal":
    print("Bem-vindo(a)", admin)
else:
    print("Este usuário não existe!")
    print("Código de erro 0000xVOLTE_AMANHA")
    exit()
senha = input("Digite sua senha de acesso:")
password = ("root/root")

if senha == "root/root":
    print("")
else:
    print("Acesso negado. Você não tem permissão para usar este programa!")
    print("https://ggram.me")


def calcular_comissao(total_vendas, percentual_comissao_por_venda):
    return total_vendas * (percentual_comissao_por_venda / 100)

id_funcionario = input("Digite seu ID de funcionário:")
print("Bem-Vindo(a)", id_funcionario)

# Entrada das vendas diárias
vendas_segunda = float(input("Digite suas vendas de Segunda-Feira: "))
vendas_terca = float(input("Digite suas vendas de Terça-Feira: "))
vendas_quarta = float(input("Digite suas vendas de Quarta-Feira: "))
vendas_quinta = float(input("Digite suas vendas de Quinta-Feira: "))
vendas_sexta = float(input("Digite suas vendas de Sexta-Feira: "))

# Total de vendas na semana
total_semana = vendas_segunda + vendas_terca + vendas_quarta + vendas_quinta + vendas_sexta
print("Total da Semana:", total_semana)

percentual_comissao_por_venda = float(input("Digite a porcentagem da comissão por venda (em %): "))

comissao_total = calcular_comissao(total_semana, percentual_comissao_por_venda)
print(f"Sua comissão total sobre as vendas da semana é R${comissao_total:.2f},", id_funcionario)