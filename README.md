<h1 align="center">Missão Aurora Siger — Relatório Operacional de Pré-Decolagem</h1>

Atividade integradora que simula o sistema de verificação de pré-decolagem da nave **Aurora Siger**, unindo lógica computacional, automação em Python, análise energética, apoio de IA e reflexão ética/sustentável.


## 📌 Sobre o projeto

O projeto está dividido em seis etapas:

| Etapa | Descrição |
|---|---|
| 1.1 | Organização e descrição da telemetria da nave (temperaturas, integridade estrutural, energia, pressão do tanque, módulos críticos) |
| 1.2 | Algoritmo de verificação (fluxograma + pseudocódigo) que decide **"DECOLAGEM AUTORIZADA"** ou **"DECOLAGEM NÃO AUTORIZADA"** |
| 1.3 | Implementação do algoritmo em Python (`service.py` + `main.py`), testada em dois cenários (nominal e com falhas) |
| 1.4 | Análise energética: cálculo da energia restante pós-decolagem (capacidade, carga, consumo e perdas) |
| 1.5 | Análise assistida por IA: classificação dos dados, detecção de anomalias, sugestão de risco — e um relato do uso de IA durante o próprio desenvolvimento |
| 1.6 | Reflexão crítica sobre ética, impacto social da exploração espacial e sustentabilidade tecnológica |

Todo o desenvolvimento está consolidado no notebook [`Analise_Pre_Decolagem_Aurora_Siger.ipynb`](./Analise_Pre_Decolagem_Aurora_Siger.ipynb) e implementado nos módulos [`service.py`](./service.py) e [`main.py`](./main.py).

## 🗂️ Estrutura do repositório

```
.
├── main.py                                     # Leitura de dados, cálculos de energia e orquestração
├── service.py                                  # Funções de validação de telemetria
├── Analise_Pre_Decolagem_Aurora_Siger.ipynb    # Relatório escrito (itens 1.1 a 1.6)
├── README.md
├── Documentacao_AuroraSiger.pdf                # Documentação detalhado do projeto
├── pyproject.toml / uv.lock                    # Metadados do projeto (sem dependências externas)
└── imagens/
    ├── fluxograma_verificacao.png              # Fluxograma do algoritmo (item 1.2)
    ├── analise_energetica.png                  # Gráfico da análise energética (item 1.4)
    ├── print_execucao_nominal.png              # Print: execução completa, cenário nominal
    └── print_execucao_falha.png                # Print: execução completa, cenário com falhas
```

## 🧩 Arquitetura do código

O algoritmo de verificação está separado em dois arquivos, cada um com uma única responsabilidade:

- **`service.py`** — as regras de validação. Seis funções (`verificar_temperatura_interna`, `verificar_temperatura_externa`, `verificar_integridade_estrutural`, `verificar_nivel_energia`, `verificar_pressao_tanque`, `verificar_modulos_criticos`), cada uma recebendo um valor e devolvendo `(válido, mensagem_de_erro)`. `pre_decolagem()` chama as seis e reúne os erros em uma lista; `decolagem()` recebe essa lista e imprime o veredito final. Nenhuma função lê ou escreve em variável fora de si mesma.
- **`main.py`** — lê a telemetria via `input()`, calcula a análise energética, imprime as tabelas de saída e chama `pre_decolagem()` / `decolagem()`.

## 🖥️ Prints da execução

**Cenário nominal** (todos os parâmetros dentro da faixa segura: decolagem autorizada):

![Execução cenário nominal](./imagens/print_execucao_nominal.png)

**Cenário com falhas** (quatro não conformidades: decolagem não autorizada):

![Execução cenário com falhas](./imagens/print_execucao_falha.png)

## ▶️ Instruções de execução

### Opção 1 — Localmente com Python
O projeto não tem dependências externas (veja `pyproject.toml`), então basta ter Python 3.13+ instalado:

```bash
git clone https://github.com/felipxv/FIAP-AuroraSiger_PreDecolagem.git
cd FIAP-AuroraSiger_PreDecolagem
python3 main.py
```

O programa vai pedir, em sequência: temperatura interna, temperatura externa, integridade estrutural, pressão do tanque, status dos módulos críticos, carga atual e perdas energéticas estimadas.

**Valores para reproduzir o cenário nominal** (decolagem autorizada):
```
21.5
-42.3
1
182
1
87
6
```

**Valores para reproduzir o cenário com falhas** (decolagem não autorizada):
```
29.8
-41.0
1
141
0
33
6
```

### Opção 2 — Com `uv`
Se preferir usar o gerenciador `uv` (o projeto já inclui `pyproject.toml` e `uv.lock`):
```bash
git clone https://github.com/felipxv/FIAP-AuroraSiger_PreDecolagem.git
cd FIAP-AuroraSiger_PreDecolagem
uv run main.py
```

### Opção 3 — Google Colab (para o notebook)
1. Acesse [https://colab.research.google.com](https://colab.research.google.com) e abra `Analise_Pre_Decolagem_Aurora_Siger.ipynb` diretamente a partir do GitHub;
2. Faça upload da pasta `imagens/` para a mesma sessão, para que o fluxograma e o gráfico sejam exibidos;
3. Execute todas as células com `Ambiente de execução → Executar tudo`.

## 🤖 Uso de IA neste projeto

A Inteligências Artificiais: Claude (Anthropic), Codex (OpenAI) e GitHub Copilot (Microsoft) foram usadas em duas frentes bem diferentes, e vale documentar as duas.

**Na análise de telemetria (item 1.5):** os dois cenários de dados foram enviados à IA pedindo classificação por parâmetro (nominal/atenção/crítico), identificação de anomalias entre parâmetros, não só violações isoladas de faixa, e uma sugestão objetiva de risco. O resultado completo está no notebook e no relatório em PDF.

**No próprio desenvolvimento do código:** ao longo da escrita de `service.py` e `main.py`, a IA foi usada como revisora de código já escrito pelo grupo, não como geradora de solução pronta. Dois problemas reais foram encontrados e corrigidos dessa forma:


2. **Um `NameError` de arquitetura** — uma lista no escopo do módulo chamava funções de verificação usando variáveis que só existiam em `main.py`. Como o Python executa o corpo de um arquivo inteiro no import, isso quebrava o programa antes mesmo dele pedir dados ao usuário.
3. **Estado global** — a lista de erros e a impressão do veredito dependiam de uma variável fora de qualquer função, o que acumularia erros de execuções anteriores caso o código fosse chamado mais de uma vez.

Cada correção só foi incorporada depois de entendida, revisada e testada. Com uso prático e crítico de ferramentas de IA, não para gerar código às cegas, mas para revisar, depurar e justificar cada decisão. Tratar a IA como uma classificadora de cenários e revisora que indica o "porquê" de cada sugestão, foi uma boa prática deliberada ao longo do projeto.

## 📄 Relatório em PDF

O relatório completo em `.pdf` (telemetria, algoritmo, código, análise energética, análise assistida por IA, incluindo o relato do item acima, e reflexão crítica) acompanha esta entrega.

## Integrantes: Grupo 18

- Felipe de Barros Franco
- Guilherme Santos
