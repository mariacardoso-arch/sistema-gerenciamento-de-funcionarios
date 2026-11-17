# sistema-gerenciamento-de-funcionarios
Sistema desenvolvido em Python para gerenciamento de funcionários.

Descrição: Ele permite que os usuários  de uma empresa se cadastrem, permite consultar os cadastros, atualizar ou excluir informações dos funcionários.

Objetivo: Facilitar o sistema de gerenciamento de funcionários, com os dados de forma fácil e organizada de achar ou acessar.

Tecnologias: 
Python / JSON / Git / GitHub / Visual Studio Code

Funcionalidades:

Cadastrar funcionário: permite adicionar um novo funcionário, informando nome, idade, cargo e e-mail.

Consultar funcionários: permite visualizar os funcionários cadastrados.

Atualizar funcionário: permite modificar as informações de um funcionário existente.

Excluir funcionário: permite remover um funcionário cadastrado, com confirmação antes da exclusão.

Menu interativo: permite escolher qual operação deseja realizar.

Armazenamento: 
Os dados dos funcionários são armazenados no arquivo funcionarios.json, localizado na pasta data.
O formato JSON permite salvar as informações e recuperá-las quando o sistema for executado novamente.

A estrutura:

```
sistema-gerenciamento-de-funcionarios/
│
├── data/
│   └── funcionarios.json
│
├── src/
│   ├── atualizacoes.py
│   ├── consultas.py
│   ├── exclusoes.py
│   ├── funcionarios.py
│   └── main.py
│
├── tests/
│   └── test_funcionarios.py
│
├── .gitignore
└── README.md
```

Como usar: No terminal main.py use "python src/main.py" para o código iniciar.