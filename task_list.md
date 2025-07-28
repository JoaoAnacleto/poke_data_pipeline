# Checklist - Teste de Pipeline de Dados PokeAPI

---

### Tarefa 1: Extração de Dados

- [x] **Consumo da API Principal:** Acessar a rota `/pokemon?limit=100&offset=0` para obter a lista inicial.
- [x] **Consumo da API de Detalhes:** Para cada Pokémon da lista, consultar a rota `/pokemon/{id}` ou a URL de detalhe fornecida.
- [x] **Criação do DataFrame:** Construir um DataFrame principal com o resultado das extrações.
- [x] **Estrutura do DataFrame:** Verificar se o DataFrame contém as seguintes colunas:
  - [x] `ID`: Identificador único.
  - [x] `Name`: Nome do Pokémon, normalizado para o formato Título (Ex: "Pikachu").
  - [x] `Base Experience`: Valor do campo `base_experience`.
  - [x] `Types`: Uma lista de strings com os tipos (Ex: `['Electric', 'Fire']`).
  - [x] `HP`: Valor da estatística "HP".
  - [x] `Attack`: Valor da estatística "Attack".
  - [x] `Defense`: Valor da estatística "Defense".

---

### Tarefa 2: Transformação de Dados

- [ ] **Categorização por Experiência:** Adicionar a coluna `Category` ao DataFrame.
  - [ ] Categoria "Weak" para `base_experience < 50`.
  - [ ] Categoria "Medium" para `base_experience` entre 50 e 100 (inclusivo).
  - [ ] Categoria "Strong" para `base_experience > 100`.
- [ ] **Contagem por Tipo:** Criar um novo DataFrame separado que mostra a contagem de Pokémon por tipo.
- [ ] **Análise Estatística por Tipo:** Calcular a média de `Attack`, `Defense` e `HP` para cada tipo de Pokémon.
- [ ] **Análise de Top Pokémon:** Identificar e listar os 5 Pokémon com a maior `Base Experience`.
- [ ] **Geração de Gráfico:** Gerar um gráfico de barras (`matplotlib` ou `seaborn`) mostrando a distribuição de Pokémon por tipo.

---

### Tarefa 3: Relatório e Exportação

- [ ] **Exportar Tabela dos Top 5:** Salvar a tabela dos 5 Pokémon com maior experiência em um arquivo `.csv`.
- [ ] **Exportar Tabela de Médias:** Salvar a tabela com as médias de ataque, defesa e HP por tipo em um arquivo `.csv`.
- [ ] **Exportar Gráfico:** Salvar o gráfico de distribuição de tipos como uma imagem (`.png`).
- [ ] **Verificar Saídas:** Confirmar que todos os arquivos foram salvos corretamente no diretório de saída (ex: `output/`).

---

### Tarefa 4: Pipeline Automatizado

- [ ] **Script Modular:** O código está organizado em módulos (ex: `extractor.py`, `transformer.py`, `reporter.py`).
- [ ] **Script Principal:** Um script principal (ex: `main.py`) executa todas as tarefas em sequência.
- [x] **Implementação de Logs:** A biblioteca `logging` é utilizada para registrar o progresso do pipeline e os principais passos.
- [ ] **Tratamento de Erros:** O pipeline lida com possíveis erros (ex: falhas na chamada da API, dados faltantes) usando `try...except`.
