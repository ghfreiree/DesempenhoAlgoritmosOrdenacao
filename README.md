# Análise de Desempenho de Algoritmos de Ordenação

Este projeto implementa uma ferramenta interativa em Python para analisar e comparar o desempenho (tempo de execução) de diferentes algoritmos de ordenação. O sistema permite gerar listas de números inteiros, ordená-las utilizando algoritmos clássicos e visualizar os resultados através de gráficos.

## 🚀 Funcionalidades

O projeto oferece um menu interativo com as seguintes capacidades:

1.  **Simulação de Ordenação**:
    * Escolha entre diferentes tamanhos de lista (N): 1.000, 5.000, 10.000, 25.000 e 50.000 elementos.
    * Execução de 4 algoritmos de ordenação:
        * Bubble Sort
        * Selection Sort
        * Insertion Sort
        * Merge Sort
    * O sistema executa cada teste 3 vezes e calcula o tempo médio para garantir precisão.
2.  **Manipulação de Arquivos**:
    * Geração automática de arquivos com listas desordenadas (`lista_desordenada_N.txt`).
    * Salvamento das listas ordenadas em novos arquivos (`lista_ordenada_N_Algoritmo.txt`).
3.  **Visualização de Dados**:
    * Geração de gráfico comparativo (`grafico_desempenho.png`) utilizando `matplotlib` para visualizar a curva de crescimento de tempo x tamanho da lista.

## 🛠️ Tecnologias Utilizadas

* **Python 3.13**
* **Matplotlib**: Para plotagem dos gráficos de desempenho.
* **OS/Random/Time**: Bibliotecas padrão para manipulação de sistema, geração de dados e medição de tempo.

## 📦 Pré-requisitos

Para rodar este projeto, você precisará ter o Python instalado e a biblioteca `matplotlib`.

```bash
pip install matplotlib
