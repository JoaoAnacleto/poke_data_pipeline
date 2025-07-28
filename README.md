# Poke Data Pipeline

Este projeto implementa um pipeline de dados para extrair, transformar e relatar informações sobre Pokémon usando a PokeAPI.

## Funcionalidades

- **Extração de Dados:** Coleta dados de Pokémon da PokeAPI.
- **Transformação de Dados:** Categoriza Pokémon por experiência, conta Pokémon por tipo, calcula estatísticas por tipo e identifica os 5 Pokémon com maior experiência base.
- **Geração de Relatórios:** Gera gráficos de distribuição de Pokémon por tipo e exporta dados transformados para arquivos CSV.

## Estrutura do Projeto

```
poke_data_pipeline/
├── config/
│   ├── __init__.py
│   ├── logging.conf
│   └── settings.py
├── output/
├── src/
│   ├── __init__.py
│   ├── extractor.py
│   ├── reporter.py
│   └── transformer.py
├── tests/
│   ├── test_extractor.py
│   └── test_transformer.py
├── Dockerfile
├── LICENSE
├── README.md
├── app.log
├── main.py
├── requirements.txt
└── task_list.md
```


## Documentação do Código

Para uma documentação detalhada do código-fonte, classes, funções e configurações, consulte o arquivo [DOCS.md](DOCS.md).


## Instalação

### Pré-requisitos

- Python 3.8+
- Docker (opcional, para execução em containers)

### Via pip

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/poke_data_pipeline.git
   cd poke_data_pipeline
   ```

2. Crie e ative um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Via Docker

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/poke_data_pipeline.git
   cd poke_data_pipeline
   ```

2. Construa a imagem Docker:

   ```bash
   docker build -t poke-data-pipeline .
   ```

## Uso

### Execução com Docker Compose

Para executar o pipeline usando Docker Compose, navegue até o diretório raiz do projeto e execute:

```bash
docker-compose up --build
```

- `--build`: Constrói a imagem Docker antes de iniciar o container (útil na primeira execução ou após alterações no `Dockerfile`).

Os relatórios gerados serão salvos no diretório `output/` do seu projeto local, devido ao mapeamento de volume configurado no `docker-compose.yml`.

### Execução Local

Para executar o pipeline localmente, certifique-se de que as dependências estejam instaladas e execute o arquivo `main.py`:

```bash
python main.py
```

Os relatórios gerados (gráficos e CSVs) serão salvos no diretório `output/`.



## Configuração

As configurações da aplicação são gerenciadas através do arquivo `config/settings.py` e variáveis de ambiente no arquivo `config/.env`.

### `config/settings.py`

Este arquivo define as configurações base da aplicação, como a URL da PokeAPI e o diretório de saída dos relatórios.

```python
# Exemplo de conteúdo de config/settings.py
import os

class Settings:
    BASE_URL: str = os.getenv("BASE_URL", "https://pokeapi.co/api/v2")
    OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "output")

```

### `config/.env`

Você pode sobrescrever as configurações padrão definindo variáveis de ambiente neste arquivo. Crie um arquivo `.env` dentro do diretório `config/` com o seguinte formato:

```ini
# Exemplo de conteúdo de config/.env
BASE_URL=https://pokeapi.co/api/v2
OUTPUT_DIR=./meus_relatorios
```


## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
