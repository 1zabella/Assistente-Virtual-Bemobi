# Hackathon Bemobi - Hacktudo 2024

<p align="center">
<a href= "https://www.hacktudo.com.br/hackathonbemobi"><img src="https://static.wixstatic.com/media/8769c0_5e62b11a063e419f94421e9f325eeead~mv2.png/v1/fill/w_377,h_49,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/8769c0_5e62b11a063e419f94421e9f325eeead~mv2.png" alt="Hackatudo" width="400" border="0"></a>
</p>

# Do código à criatividade: IA em ação

## Equipe: TransformAI
### Integrantes:
- <a href="https://www.linkedin.com/in/izabellaalmeida/">Izabella Almeida</a>
- <a href="https://www.linkedin.com/in/sofia-carvalho-386a8774/">Sofia de Carvalho</a>
- <a href="https://www.linkedin.com/in/pedrocrezende/">Pedro Rezende</a>


## Descrição do Tema 🔍
### Tema
**GenAi (Inteligência Artificial Generativa)**

Como a Bemobi pode utilizar GenAI para proporcionar uma experiência melhor
para os seus clientes?

### Desafio
O desafio está centrado nos serviços baseados em assinaturas com pagamentos recorrentes. O objetivo é utilizar tecnologia de Inteligência Artificial (GenAI) para otimizar a experiência do cliente, desde o momento da contratação até o gerenciamento contínuo de contas básicas recorrentes.


## 📁 Estrutura de pastas
Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

* **backend:** Contém os arquivos relacionados à lógica da API em FastAPI e à comunicação com o dados presentes na `utils`.
* **frontend:** Contém os arquivos relacionados à interface do usuário, desenvolvida no framework `streamlit`.
* **utils:** Contém dados que são usados para demonstração do projeto e chave da OpenAI para ativamento da solução.
* **README.md:** Arquivo que serve como guia e explicação geral sobre o projeto.

## 🔧 Instalação

Este projeto pode ser instalado de duas formas: utilizando um ambiente virtual (Venv) ou Docker. Escolha o método que melhor se adequa às suas necessidades.

### 1. Instalação com Venv

A instalação utilizando um ambiente virtual permite isolar as dependências do projeto, evitando conflitos com outros pacotes instalados no sistema.

1. **Clone o repositório:**

   ```git
   git clone https://github.com/1zabella/Assistente-Virtual-Bemobi.git
   cd Assistente-Virtual-Bemobi
   ```

2. **Crie um ambiente virtual:**
    ```python
    python3 -m venv venv
    source venv/bin/activate
    ```
    ```python
    python -m venv venv
    venv\Scripts
    activate
    ```
3. **Instale as dependências:**
    ```python
    pip install -r requirements.txt
    ```


## 💻 Configuração de Desenvolvimento

Para configurar o ambiente de desenvolvimento, siga os seguintes passos:

### 1. Ambiente Virtual (Venv)

1. **Instalação de dependências para desenvolvimento:**

   Certifique-se de que seu ambiente virtual está ativo e instale os pacotes de desenvolvimento:

   ```sh
   pip install -r requirements.txt
   ```

   O arquivo `requirements.txt` deve conter todas as dependências necessárias para desenvolvimento.


3. **Rodando o projeto em modo de desenvolvimento:**

   ```sh
   python main.py
   ```

4. **Rodando o frontend:**

   ```sh
   streamlit run app.py
   ```

5. Arquivo config.json deve conter a chave da OpenAI para ativação da solução. Deve estar na pasta `utils`.

- **Exemplo de config.json:**
```json
{
    "api_key": "sua_chave_aqui"
}
```

### IMPORTANTE: o projeto foi desenvolvido com a chave da OpenAI de teste, para utilizar a solução é necessário adquirir uma chave, caso não tenha, não irá rodar.