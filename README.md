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

## Instalação

### Pré-requisitos

- Python 3.12+
- Docker (opcional, para execução em containers)

### Via pip

1. Clone o repositório:

   ```bash
   git clone https://github.com/JoaoAnacleto/poke_data_pipeline.git
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
   git clone https://github.com/JoaoAnacleto/poke_data_pipeline.git
   cd poke_data_pipeline
   ```

2. Construa a imagem Docker:

   ```bash
   docker build -t poke-data-pipeline .
   ```

## Uso

### Execução Local

Para executar o pipeline localmente, certifique-se de que as dependências estejam instaladas e execute o arquivo `main.py`:

```bash
python main.py
```

Os relatórios gerados (gráficos e CSVs) serão salvos no diretório `output/`.

### Execução com Docker

Para executar o pipeline usando Docker, execute o seguinte comando:

```bash
docker run --rm -v $(pwd)/output:/app/output poke-data-pipeline
```

- `--rm`: Remove o container automaticamente após a execução.
- `-v $(pwd)/output:/app/output`: Mapeia o diretório `output` do seu host para o diretório `output` dentro do container, permitindo que você acesse os relatórios gerados.

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

## Gerenciamento de Containers com Portainer

Para facilitar o gerenciamento e a visualização dos seus containers Docker, recomendamos o uso do Portainer.

### O que é Portainer?

Portainer é uma ferramenta de gerenciamento de código aberto que simplifica a implantação, o gerenciamento e a operação de ambientes Docker (e Kubernetes). Ele fornece uma interface de usuário intuitiva que permite gerenciar containers, imagens, volumes, redes e muito mais.

### Instalação do Portainer

Para instalar o Portainer em um ambiente Docker, execute os seguintes comandos:

1. Crie um volume Docker para persistir os dados do Portainer:

   ```bash
   docker volume create portainer_data
   ```

2. Execute o container do Portainer:

   ```bash
   docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
   ```

   - `-p 8000:8000`: Porta para a comunicação HTTP (opcional).
   - `-p 9443:9443`: Porta para a interface web HTTPS (recomendado).
   - `--name portainer`: Nomeia o container como `portainer`.
   - `--restart always`: Garante que o Portainer reinicie automaticamente com o Docker.
   - `-v /var/run/docker.sock:/var/run/docker.sock`: Permite que o Portainer se comunique com o daemon Docker.
   - `-v portainer_data:/data`: Mapeia o volume `portainer_data` para o diretório de dados do Portainer.

### Acessando o Portainer

Após a instalação, você pode acessar a interface web do Portainer em `https://localhost:9443` (ou `https://seu_ip_do_servidor:9443`). Na primeira vez, você será solicitado a criar um usuário e senha de administrador.

### Gerenciando o `poke-data-pipeline` no Portainer

1. **Adicionar Imagem:** No Portainer, navegue até "Images" e você verá a imagem `poke-data-pipeline` que você construiu.

2. **Criar Container:** Vá para "Containers" e clique em "Add container".
   - **Name:** `poke-data-pipeline-instance` (ou outro nome de sua preferência)
   - **Image:** `poke-data-pipeline`
   - **Volumes:** Adicione um mapeamento de volume para o diretório `output`:
     - `host path`: `/caminho/completo/para/seu/projeto/poke_data_pipeline/output` (substitua pelo caminho real no seu sistema)
     - `container path`: `/app/output`
   - Clique em "Deploy the container".

3. **Visualizar Logs e Status:** No Portainer, você pode facilmente visualizar os logs do container, iniciar, parar, reiniciar e remover o container, além de inspecionar seus detalhes.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.



