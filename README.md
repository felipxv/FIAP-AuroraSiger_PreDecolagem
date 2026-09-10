# Missão Aurora Siger — Relatório Operacional de Pré-Decolagem

Atividade integradora que simula o sistema de verificação de pré-decolagem da nave **Aurora Siger**, juntando lógica computacional, automação em Python, análise energética, apoio de IA e reflexão ética e sustentável.

## Sobre o projeto

O trabalho está dividido em seis etapas:

| Etapa | Descrição |
|---|---|
| 1.1 | Telemetria da nave: parâmetros monitorados, unidades e faixas seguras (temperaturas, integridade estrutural, energia, pressão dos tanques, módulos críticos) |
| 1.2 | Algoritmo de verificação em fluxograma e pseudocódigo, decidindo entre **"PRONTO PARA DECOLAR"** e **"DECOLAGEM ABORTADA"** |
| 1.3 | Implementação do algoritmo em Python, testada em dois cenários (nominal e com falhas) |
| 1.4 | Análise energética: autonomia inicial a partir de capacidade, carga, consumo e perdas |
| 1.5 | Análise assistida por IA: classificação dos parâmetros, detecção de anomalias e sugestão de risco |
| 1.6 | Reflexão crítica sobre ética, impacto social da exploração espacial e sustentabilidade tecnológica |

A entrega tem duas partes. O relatório escrito, com as seis etapas, está no notebook [`Analise_Pre_Decolagem_Aurora_Siger.ipynb`](./Analise_Pre_Decolagem_Aurora_Siger.ipynb), que é só texto e não precisa ser executado. O código do item 1.3 está separado em [`main.py`](./main.py).

## Estrutura do repositório

```
.
├── Analise_Pre_Decolagem_Aurora_Siger.ipynb   # Relatório escrito (itens 1.1 a 1.6)
├── main.py                                    # Script de verificação e análise energética
├── README.md
└── imagens/
    ├── fluxograma_verificacao.png              # Fluxograma do algoritmo (item 1.2)
    └── analise_energetica.png                  # Gráficos da análise energética (item 1.4)
```

## Como executar

O script roda direto, sem dependências externas:

```bash
git clone https://github.com/<seu-usuario>/aurora-siger-pre-decolagem.git
cd aurora-siger-pre-decolagem
python3 main.py
```

Ele imprime a verificação dos dois cenários de telemetria (nominal e com falhas) e, em seguida, a análise energética com a autonomia estimada. Essas mesmas saídas estão transcritas no notebook, nos itens 1.3 e 1.4.

O notebook pode ser aberto no Jupyter (`jupyter notebook Analise_Pre_Decolagem_Aurora_Siger.ipynb`), no VS Code ou no Google Colab. Como ele só contém texto, basta ler, não há células para rodar. As imagens são carregadas da pasta `imagens/`, então mantenha a pasta junto do notebook.

### Requisitos
- Python 3.9 ou superior
- Nenhuma biblioteca externa para rodar o `main.py`

## Relatório em PDF

O PDF com o relatório completo (telemetria, algoritmo, código, análise energética, análise assistida por IA e reflexão crítica) acompanha a entrega da atividade.

## Grupo 18

- Felipe de Barros Franco
- Guilherme Santos
