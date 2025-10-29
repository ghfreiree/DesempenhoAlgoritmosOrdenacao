"""
CP05: Análise de Desempenho de Algoritmos de Ordenação

Feito por:
- Gustavo Freire, RM 561334
- Pedro Gomes, RM 562606
- Lucas Lopes, RM 563544

Este código implementa uma análise de desempenho interativa entre algoritmos de ordenação.

1. Ao iniciar, ele gera arquivos com listas de números inteiros desordenados
2. O menu principal permite ao usuário:
    a. Simular uma ordenação (escolhendo N e o algoritmo).
    b. Gerar um gráfico com os resultados de desempenho (tempos médios) de todas as simulações feitas.
    c. Sair.
3. Os resultados são armazenados em memória e usados pela função de gerar gráfico.
"""

import time
import random
import os  # Usado para limpar o console
import matplotlib.pyplot as plt # Biblioteca para criar o gráfico


# --- 1. Funções dos algoritmos de ordenação ---

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        troca = False
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                troca = True
        if not troca:
            break
    return lista


def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        L = lista[:meio]
        R = lista[meio:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista


# --- 2. Funções auxiliares ---

def gerar_lista_aleatoria(tamanho):
    """Gera uma lista com N inteiros aleatórios."""
    return [random.randint(0, tamanho * 10) for _ in range(tamanho)]


def ler_arquivo(nome_arquivo):
    """Lê um arquivo de texto e retorna uma lista de inteiros."""
    try:
        with open(nome_arquivo, 'r') as f:
            lista = [int(linha) for linha in f ]
        return lista
    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada '{nome_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None


def salvar_arquivo(nome_arquivo, lista):
    """Salva uma lista em um arquivo de texto."""
    try:
        with open(nome_arquivo, 'w') as f:
            for item in lista:
                f.write(f"{item}\n")
        return True
    except Exception as e:
        print(f"Erro ao salvar o arquivo '{nome_arquivo}': {e}")
        return False


def gerar_grafico(resultados, tamanhos_n):
    """Gera e salva um gráfico comparativo."""
    print("\nGerando gráfico de desempenho...")

    dados_grafico = {}
    for nome, tempos in resultados.items():
        # Filtra os pontos para jogar para o gráfico apenas onde temos dados
        pontos_n = []
        pontos_tempo = []
        for i, tempo in enumerate(tempos):
            if tempo is not None:
                pontos_n.append(tamanhos_n[i])
                pontos_tempo.append(tempo)
        dados_grafico[nome] = (pontos_n, pontos_tempo)

    plt.figure(figsize=(12, 7))

    for nome, (pontos_n, pontos_tempo) in dados_grafico.items():
        if pontos_tempo:  # Só plota se houver dados
            plt.plot(pontos_n, pontos_tempo, marker='o', linestyle='-', label=nome)

    plt.title("Comparativo de Desempenho de Algoritmos de Ordenação")
    plt.xlabel("Tamanho da Lista (N)")
    plt.ylabel("Tempo Médio de Execução (segundos)")
    plt.legend()
    plt.grid(True)
    plt.xticks(tamanhos_n)

    nome_arquivo_grafico = "grafico_desempenho.png"
    plt.savefig(nome_arquivo_grafico)

    print(f"Gráfico salvo como '{nome_arquivo_grafico}'")
    print("Pressione Enter para voltar ao menu.")
    input()
    return


def preparar_arquivos_base(tamanhos):
    """Cria os arquivos de base."""
    print("Criando arquivos de base...")
    for n in tamanhos:
        nome_arquivo = f"lista_desordenada_{n}.txt"
        lista_aleatoria = gerar_lista_aleatoria(n)
        salvar_arquivo(nome_arquivo, lista_aleatoria)
        print(f"Arquivo '{nome_arquivo}' gerado com {n} elementos.")
    print("Todos os arquivos de base estão prontos.")


# --- 3. Função da simulação ---

def rodar_simulacao(algoritmos_map, resultados_map, n_lista, n_map):
    """
    - Executa uma simulação de ordenação escolhida pelo usuário.
    - Lê o arquivo de base, executando 3 vezes para obter uma média de resultado
    - Salva o resultado na matriz/dicionário.
    """

    print("\n--- Simular Ordenação de Arquivo ---")

    # 1. Pergunta o tamanho N
    print("Escolha o tamanho da lista (N) que deseja ordenar:")
    for i, n in enumerate(n_lista):
        print(f"{i + 1} - {n} elementos")
    escolha_n_idx = input(f"Digite o número (1 a {len(n_lista)}): ")

    try:
        n_idx = int(escolha_n_idx) - 1
        if n_idx < 0 or n_idx >= len(n_lista):
            print(f"Escolha '{escolha_n_idx}' inválida.")
        n_escolhido = n_lista[n_idx]
    except ValueError:
        print(f"Erro: Escolha '{escolha_n_idx}' inválida.")
        print("Pressione Enter para voltar ao menu.")
        input()
        return

    # 2. Pergunta o algoritmo
    print("\nEscolha o algoritmo de ordenação:")
    for chave in algoritmos_map.keys():
        print(f"{chave}: {algoritmos_map[chave][0]}")
    escolha_alg = input(f"Digite o número (1 a {len(algoritmos_map)}): ")

    if escolha_alg not in algoritmos_map:
        print(f"Erro: Escolha '{escolha_alg}' inválida.")
        print("Pressione Enter para voltar ao menu.")
        input()
        return

    # 3. Pega os dados da escolha
    nome_alg_escolhido, func_alg_escolhido = algoritmos_map[escolha_alg]

    # 4. Define os nomes dos arquivos
    arquivo_entrada = f"lista_desordenada_{n_escolhido}.txt"
    arquivo_saida = f"lista_ordenada_{n_escolhido}_{nome_alg_escolhido.replace(' ', '_')}.txt"

    print(f"\nIniciando simulação (Média de 3 amostras):")
    print(f"Algoritmo: {nome_alg_escolhido}")
    print(f"Arquivo de base:   {arquivo_entrada}")

    tempos_amostra = []
    lista_ordenada_final = []

    # 5. Loop de testes (3 vezes)
    for i in range(3):
        print(f"Executando amostra {i + 1}/3...")

        # Lê a mesma lista desordenada do arquivo a cada vez
        lista_para_ordenar = ler_arquivo(arquivo_entrada)
        if lista_para_ordenar is None:
            print("Erro ao ler arquivo. Abortando simulação.")
            print("Pressione Enter para voltar ao menu.")
            input()
            return

        inicio = time.time()
        func_alg_escolhido(lista_para_ordenar)  # Ordena in-place
        fim = time.time()

        tempos_amostra.append(fim - inicio)

        # No último loop do laço, guarda a lista ordenada para salvar
        if i == 2:
            lista_ordenada_final = lista_para_ordenar

    # 6. Calcula a média e salva o resultado
    tempo_medio = sum(tempos_amostra) / 3

    # 7. Armazena na "matriz" (dicionário de listas)
    # Pega o índice do tamanho N a partir do dicionário de mapa_n_com_indice
    idx_n_no_mapa = n_map[n_escolhido]

    # Insere o tempo médio das três amostras no dicionário de resultados
    resultados_map[nome_alg_escolhido][idx_n_no_mapa] = tempo_medio

    # 8. Salva o arquivo com a lista já ordenada
    salvar_arquivo(arquivo_saida, lista_ordenada_final)

    print("\n--- Simulação Concluída ---")
    print(f"Amostra 1: {tempos_amostra[0]:.3f}s")
    print(f"Amostra 2: {tempos_amostra[1]:.3f}s")
    print(f"Amostra 3: {tempos_amostra[2]:.3f}s")
    print(f"Tempo Médio: {tempo_medio:.3f}s")
    print(f"Resultado salvo para o gráfico.")
    print(f"Arquivo ordenado salvo em: '{arquivo_saida}'")
    print("Pressione Enter para voltar ao menu.")
    input()


# --- 4. Função principal ---

def main():
    """Função principal que exibe o menu interativo."""

    tamanhos_n = [1000, 5000, 10000, 25000, 50000]

    algoritmos = {
        '1': ("Bubble Sort", bubble_sort),
        '2': ("Selection Sort", selection_sort),
        '3': ("Insertion Sort", insertion_sort),
        '4': ("Merge Sort", merge_sort)
    }

    # Mapeia o valor de N com o seu índice
    mapa_n_com_indice = {n: i for i, n in enumerate(tamanhos_n)} # 1000:0 5000:1...

    # "Matriz" dos resultados de desempenho, com os espaços preenchidos por 'None'
    # Cada algoritmo possui um espaço de resultado para cada lista de tamanho N (5 resultados)
    resultados_para_grafico = {
        nome_alg: [None] * len(tamanhos_n) # Ex: (Bubble Sort: [None, None, None, None, None])
        for nome_alg, func in algoritmos.values() # Pega os dados do dicionário "algoritmos"
    }


    # 1. Prepara todos os arquivos de base (listas desordenadas) para os testes
    preparar_arquivos_base(tamanhos_n)
    print("Pressione Enter para iniciar o menu.")
    input()


    # 2. Inicia o loop do menu principal
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=" * 50)
        print("Atividade Prática: Análise de Algoritmos ")
        print("=" * 50)

        print("\nEscolha uma opção:")
        print("1. Simular Ordenação (Escolher N e Algoritmo)")
        print("2. Gerar Gráfico (com resultados atuais)")
        print("3. Sair")

        escolha = input("\nDigite sua escolha (1, 2 ou 3): ")

        if escolha == '1':
            rodar_simulacao(algoritmos, resultados_para_grafico, tamanhos_n, mapa_n_com_indice)

        elif escolha == '2':
            gerar_grafico(resultados_para_grafico, tamanhos_n)

        elif escolha == '3':
            print("Encerrando o programa.")
            break  # Quebra o loop 'while True'

        else:
            print(f"Opção '{escolha}' inválida. Pressione Enter para tentar novamente.")


if __name__ == "__main__":
    main()