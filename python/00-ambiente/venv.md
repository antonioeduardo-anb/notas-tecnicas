# `venv`

O módulo `venv` é a implementação padrão do Python para a criação de ambientes virtuais (*virtual environments*).

Um ambiente virtual é um diretório que contém uma instalação isolada do interpretador Python e das bibliotecas necessárias para um projeto específico.

Seu principal objetivo é impedir que dependências de projetos diferentes entrem em conflito.

## Por que utilizar o `venv`?

Sem um ambiente virtual, todas as bibliotecas são instaladas no mesmo local:

```text
Sistema
│
├── requests 2.31
├── flask 3.0
└── numpy 2.0
```

Isso pode causar problemas quando projetos diferentes dependem de versões distintas da mesma biblioteca.

Com o `venv`, cada projeto possui o seu próprio ambiente:

```text
projeto-a/
├── .venv
└── app.py

projeto-b/
├── .venv
└── app.py
```

## Criando um ambiente virtual

Crie o diretório do projeto:

```bash
mkdir meu_projeto
cd meu_projeto
```

Crie o ambiente virtual:

```bash
python3 -m venv .venv
```

Nesse exemplo, `.venv` é o diretório que armazenará o ambiente virtual.

## Ativando o ambiente

No Linux:

```bash
source .venv/bin/activate
```

No Windows (Prompt de Comando):

```cmd
.venv\Scripts\activate.bat
```

No Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Após a ativação, o terminal exibirá algo semelhante a isto:

```text
(.venv) usuario@maquina:~/projeto$
```

## Instalando bibliotecas

```bash
pip install flask
```

## Exibindo as dependências instaladas

```bash
pip list
```

## Gerando um arquivo de dependências

```bash
pip freeze > requirements.txt
```

Exemplo:

```text
flask==3.1.2
requests==2.32.5
```

## Instalando as dependências do projeto

```bash
pip install -r requirements.txt
```

## Desativando o ambiente

```bash
deactivate
```

## Estrutura do diretório

```text
meu_projeto/
├── .venv/
├── app.py
├── requirements.txt
└── README.md
```

## Observações

- O diretório `.venv` normalmente não é enviado para o GitHub.

- O arquivo `requirements.txt` deve ser versionado.

- Cada projeto deve possuir o seu próprio ambiente virtual.

- O uso de `venv` é recomendado mesmo em ambientes executados em contêineres.
