# Missão Aurora Siger — Relatório Operacional de Pré-Decolagem

Atividade integradora que simula o sistema de verificação de pré-decolagem da nave **Aurora Siger**, juntando lógica computacional, automação em Python, análise energética, apoio de IA e reflexão ética e sustentável.

## Sobre o projeto

O relatório está dividido em seis etapas:

| Etapa | Descrição |
|---|---|
| 1.1 | Telemetria da nave: parâmetros monitorados, unidades e faixas seguras (temperaturas, integridade estrutural, energia, pressão dos tanques, módulos críticos) |
| 1.2 | Algoritmo de verificação em fluxograma e pseudocódigo, decidindo entre **"PRONTO PARA DECOLAR"** e **"DECOLAGEM ABORTADA"** |
| 1.3 | Implementação do algoritmo em Python, testada em dois cenários (nominal e com falhas) |
| 1.4 | Análise energética: autonomia inicial a partir de capacidade, carga, consumo e perdas |
| 1.5 | Análise assistida por IA: classificação dos parâmetros, detecção de anomalias e sugestão de risco |
| 1.6 | Reflexão crítica sobre ética, impacto social da exploração espacial e sustentabilidade tecnológica |

Tudo está no notebook [`Analise_Pre_Decolagem_Aurora_Siger.ipynb`](./Analise_Pre_Decolagem_Aurora_Siger.ipynb).

## Estrutura do repositório

```
.
├── Analise_Pre_Decolagem_Aurora_Siger.ipynb   # Notebook principal (todas as etapas)
├── README.md
└── imagens/
    ├── fluxograma_verificacao.png              # Fluxograma do algoritmo (item 1.2)
    ├── analise_energetica.png                  # Gráficos da análise energética (item 1.4)
    ├── print_execucao_nominal.png              # Print: verificação do cenário nominal
    ├── print_execucao_falha.png                # Print: verificação do cenário com falhas
    └── print_execucao_energia.png              # Print: saída da análise energética
```

## Prints da execução

Verificação no cenário nominal, com todos os parâmetros dentro da faixa segura:

![Execução cenário nominal](./imagens/print_execucao_nominal.png)

Verificação no cenário com falhas, mostrando o caminho de abort do algoritmo:

![Execução cenário com falhas](./imagens/print_execucao_falha.png)

Análise energética e autonomia inicial da nave:

![Execução análise energética](./imagens/print_execucao_energia.png)

## Como executar

### Opção 1 — Google Colab (não requer instalação)
1. Acesse [https://colab.research.google.com](https://colab.research.google.com);
2. Vá em `Arquivo → Fazer upload de notebook` e selecione `Analise_Pre_Decolagem_Aurora_Siger.ipynb` (ou abra direto do GitHub, colando a URL do repositório);
3. Suba também a pasta `imagens/` na mesma sessão (painel lateral esquerdo, ícone de pasta, *upload*), senão o fluxograma e os gráficos não aparecem;
4. Rode tudo com `Ambiente de execução → Executar tudo`.

### Opção 2 — Localmente com Jupyter
```bash
# 1. Clone o repositório
git clone https://github.com/<seu-usuario>/aurora-siger-pre-decolagem.git
cd aurora-siger-pre-decolagem

# 2. Crie um ambiente virtual (opcional)
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install jupyter pandas matplotlib

# 4. Abra o notebook
jupyter notebook Analise_Pre_Decolagem_Aurora_Siger.ipynb
```

Depois execute todas as células (`Cell → Run All` ou `Kernel → Restart & Run All`).

### Requisitos
- Python 3.9 ou superior
- `pandas`
- `matplotlib`
- Jupyter Notebook/JupyterLab (ou o Google Colab)

## Relatório em PDF

O PDF com o relatório completo (telemetria, algoritmo, código, análise energética, análise assistida por IA e reflexão crítica) acompanha a entrega da atividade.

## Grupo 18

- Felipe de Barros Franco
- Guilherme Santos
