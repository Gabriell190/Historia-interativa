def criar_historia():
    print("\nBem-vindo ao Historias.com, seu site para criar histórias curtas!")
    print("PS: Forneça um input claro para uma melhor experiência.\n")

    protagonista = input("Nome do protagonista: ")
    local = input("Local da história: ")
    acao_inicial = input("O que o protagonista estava fazendo? ")
    evento = input("Evento inesperado que ocorreu: ")
    reacao = input("Reação do protagonista: ")
    desfecho = input("O que aconteceu depois? ")
    final_feliz = input("Final feliz: ")
    
    historia = f"""
    ---------------------------------------------------------
    Aqui está sua história:
    
    Era uma vez, em {local}, uma pessoa chamada {protagonista}.
    Certo dia, {protagonista} estava {acao_inicial}, até que, de repente, {evento}.
    Imediatamente, {protagonista} {reacao}, e então, {desfecho}.
    Felizmente, {final_feliz}. Fim.
    """
    
    print(historia)

if __name__ == "__main__":
    criar_historia()
