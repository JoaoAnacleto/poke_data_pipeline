# Documentação do Código - Poke Data Pipeline

Este documento detalha a estrutura e funcionalidade do código-fonte da aplicação `poke_data_pipeline`.

## `main.py`

**Resumo:** Ponto de entrada principal da aplicação, orquestra a execução do pipeline de extração, transformação e relatório de dados de Pokémon.

**Componentes Detalhados:**

- **Funções/Métodos:**
  - `main()`:
    - **Descrição:** Inicializa as classes `PokemonExtractor`, `DataTransformer` e `DataReporter`, e executa as etapas do pipeline: busca dados de Pokémon, transforma-os e gera relatórios. Lida com exceções durante a execução.
    - **Parâmetros:** Nenhum.
    - **Retorno:** Nenhum.
    - **Exceções:** `Exception`: Captura e registra quaisquer erros que ocorram durante a execução do pipeline.

## `src/extractor.py`

**Resumo:** Módulo responsável pela extração de dados de Pokémon da PokeAPI e pela construção de um DataFrame pandas com esses dados.

**Componentes Detalhados:**

- **Classes:**
  - `PokemonExtractor`:
    - **Descrição:** Gerencia a conexão com a PokeAPI e a extração de dados de Pokémon.
    - **Atributos Principais:**
      - `configs`: Instância da classe `Settings` para acessar configurações da aplicação.
      - `logger`: Instância de `logging.Logger` para registro de eventos.
    - **Métodos Principais:**
      - `__init__(self, logger: logging.Logger)`
      - `fetch_pokemon_data(self, limit: int = 100, offset: int = 0) -> list[dict]`
      - `_extract_pokemon_id(self, pokemon_url: str) -> int`
      - `_fetch_pokemon_details(self, pokemon_id: int) -> dict`
      - `_build_pokemon_dict(self, pokemon_data: dict) -> dict`
      - `build_pokemons_dataframe(self, pokemons_data: list[dict]) -> pd.DataFrame`

## `src/transformer.py`

**Resumo:** Módulo responsável pela transformação e agregação dos dados de Pokémon extraídos.

**Componentes Detalhados:**

- **Classes:**
  - `DataTransformer`:
    - **Descrição:** Realiza diversas transformações nos dados de Pokémon, como categorização de experiência, contagem por tipo e cálculo de estatísticas.
    - **Atributos Principais:**
      - `logger`: Instância de `logging.Logger` para registro de eventos.
    - **Métodos Principais:**
      - `__init__(self, logger: logging.Logger)`
      - `categorize_experience(self, pokemon_dataframe: pd.DataFrame) -> pd.DataFrame`
      - `count_pokemon_by_type(self, pokemon_dataframe: pd.DataFrame) -> pd.DataFrame`
      - `calculate_type_statistics(self, pokemon_dataframe: pd.DataFrame) -> pd.DataFrame`
      - `find_top_pokemon(self, pokemon_dataframe: pd.DataFrame) -> pd.DataFrame`
      - `transform_pokemon_data(self, pokemon_dataframe: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]`

## `src/reporter.py`

**Resumo:** Módulo responsável pela geração de relatórios e visualizações a partir dos dados de Pokémon transformados.

**Componentes Detalhados:**

- **Classes:**
  - `DataReporter`:
    - **Descrição:** Gera gráficos e exporta dados para arquivos CSV no diretório de saída configurado.
    - **Atributos Principais:**
      - `logger`: Instância de `logging.Logger` para registro de eventos.
      - `configs`: Instância da classe `Settings` para acessar configurações da aplicação.
    - **Métodos Principais:**
      - `__init__(self, logger: logging.Logger)`
      - `__clean_reports_directory(self)`
      - `generate_type_distribution_chart(self, pokemon_by_type_dataframe: pd.DataFrame)`
      - `export_top_5_pokemon_csv(self, pokemon_top_5_dataframe: pd.DataFrame)`
      - `export_type_statistics_csv(self, pokemon_type_statistics_dataframe: pd.DataFrame)`
      - `_validate_reports_directory(self) -> bool`
      - `generate_all_reports(self, pokemon_by_type_dataframe: pd.DataFrame, pokemon_top_5_dataframe: pd.DataFrame, pokemon_type_statistics_dataframe: pd.DataFrame) -> bool`

## `config/settings.py`

**Resumo:** Define as configurações globais da aplicação, como URLs de API e diretórios de saída.

**Componentes Detalhados:**

- **Classes:**
  - `Settings`:
    - **Descrição:** Classe que carrega as configurações da aplicação, permitindo que sejam sobrescritas por variáveis de ambiente.
    - **Atributos Principais:**
      - `BASE_URL`: URL base da PokeAPI (padrão: `https://pokeapi.co/api/v2`).
      - `OUTPUT_DIR`: Diretório para salvar os relatórios gerados (padrão: `output`).

## `config/logging.conf`

**Resumo:** Arquivo de configuração para o sistema de logging da aplicação, definindo formatos, handlers e níveis de log.

**Componentes Detalhados:**

- **Arquivos de Configuração:**
  - **Seção:** `[loggers]`
    - **Parâmetro:** `keys`
    - **Descrição:** Define os loggers utilizados na aplicação.
    - **Valores Possíveis:** `root, main_logger`
  - **Seção:** `[handlers]`
    - **Parâmetro:** `keys`
    - **Descrição:** Define os handlers de log, como `consoleHandler` e `fileHandler`.
    - **Valores Possíveis:** `consoleHandler, fileHandler`
  - **Seção:** `[formatters]`
    - **Parâmetro:** `keys`
    - **Descrição:** Define os formatadores de log, como `simpleFormatter`.
    - **Valores Possíveis:** `simpleFormatter`
  - **Seção:** `[logger_root]`
    - **Parâmetro:** `level`
    - **Descrição:** Nível de log para o logger raiz.
    - **Valores Possíveis:** `INFO`
    - **Parâmetro:** `handlers`
    - **Descrição:** Handlers associados ao logger raiz.
    - **Valores Possíveis:** `consoleHandler, fileHandler`
  - **Seção:** `[logger_main_logger]`
    - **Parâmetro:** `level`
    - **Descrição:** Nível de log para o logger `main_logger`.
    - **Valores Possíveis:** `INFO`
    - **Parâmetro:** `handlers`
    - **Descrição:** Handlers associados ao logger `main_logger`.
    - **Valores Possíveis:** `consoleHandler, fileHandler`
    - **Parâmetro:** `qualname`
    - **Descrição:** Nome qualificado do logger.
    - **Valores Possíveis:** `main_logger`
    - **Parâmetro:** `propagate`
    - **Descrição:** Se as mensagens de log devem ser propagadas para loggers pais.
    - **Valores Possíveis:** `0`
  - **Seção:** `[handler_consoleHandler]`
    - **Parâmetro:** `class`
    - **Descrição:** Classe do handler.
    - **Valores Possíveis:** `StreamHandler`
    - **Parâmetro:** `level`
    - **Descrição:** Nível de log para o handler do console.
    - **Valores Possíveis:** `INFO`
    - **Parâmetro:** `formatter`
    - **Descrição:** Formatador a ser usado.
    - **Valores Possíveis:** `simpleFormatter`
    - **Parâmetro:** `args`
    - **Descrição:** Argumentos para o handler (neste caso, `(sys.stdout,)`).
    - **Valores Possíveis:** `(sys.stdout,)`
  - **Seção:** `[handler_fileHandler]`
    - **Parâmetro:** `class`
    - **Descrição:** Classe do handler.
    - **Valores Possíveis:** `FileHandler`
    - **Parâmetro:** `level`
    - **Descrição:** Nível de log para o handler de arquivo.
    - **Valores Possíveis:** `INFO`
    - **Parâmetro:** `formatter`
    - **Descrição:** Formatador a ser usado.
    - **Valores Possíveis:** `simpleFormatter`
    - **Parâmetro:** `args`
    - **Descrição:** Argumentos para o handler (neste caso, `("app.log",)`).
    - **Valores Possíveis:** `("app.log",)`
  - **Seção:** `[formatter_simpleFormatter]`
    - **Parâmetro:** `format`
    - **Descrição:** Formato das mensagens de log.
    - **Valores Possíveis:** `%(asctime)s - %(name)s - %(levelname)s - %(message)s`

## `config/.env`

**Resumo:** Arquivo para variáveis de ambiente que podem sobrescrever as configurações padrão definidas em `settings.py`.

**Componentes Detalhados:**

- **Arquivos de Configuração:**
  - **Seção:** Variáveis de Ambiente
    - **Parâmetro:** `BASE_URL`
    - **Descrição:** URL base da PokeAPI.
    - **Valores Possíveis:** Qualquer URL válida (ex: `https://pokeapi.co/api/v2`)
  - **Seção:** Variáveis de Ambiente
    - **Parâmetro:** `OUTPUT_DIR`
    - **Descrição:** Caminho do diretório onde os relatórios serão salvos.
    - **Valores Possíveis:** Qualquer caminho de diretório válido (ex: `./meus_relatorios`)

## Dependências Externas e Internas

### Bibliotecas Externas (Python)

- `pandas`: Para manipulação e análise de dados em DataFrames.
- `requests`: Para fazer requisições HTTP à PokeAPI.
- `matplotlib`: Para criação de gráficos e visualizações.
- `seaborn`: Para visualizações de dados estatísticos baseadas em Matplotlib.
- `python-dotenv`: Para carregar variáveis de ambiente do arquivo `.env`.

### Módulos Internos (do projeto)

- `src.extractor`: Módulo de extração de dados.
- `src.transformer`: Módulo de transformação de dados.
- `src.reporter`: Módulo de geração de relatórios.
- `config.settings`: Módulo de configurações da aplicação.


