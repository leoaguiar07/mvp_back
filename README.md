# Mercado Livre de Energia - API 

A partir de janeiro de 2024, qualquer tipo de negócio, como padaria ou restaurante, poderá ser beneficiado com o mercado livre de energia.

Os preços de aquisição de energia são menores no mercado livre. 

Pesquisando inúmeros sites de empresas que oferecem esses serviços, verifiquei que não era possível ter uma noção da redução de gasto, 
todos exibiam um formulário solicitando informações do usuário.<br>

A página desenvolvida permite que os usuários possam simular a sua redução de gasto, atráves de um simulador. Tendo como resultado o gasto simulado, percentual e valor de  da economia.<br>

* Valores utilizados para cálculo de economia são aproximados e foram obtidos através de pesquisas na internet, os mesmos podem ser alterados.


## Como executar

Inserir os dados necessários no banco de dados. (ver seção SQL deste documento).

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

## SQL

Os arquivos contendo os scripts necessários para inserção no banco de dados estão na pasta SQL deste projeto.<br>
Executar na seguinte ordem:<br>
1 - create_database.sql<br>
2 - create_tables.sql<br>
3 - insert.sql<br>

## Objetivo

Atender ao MVP da disciplina de Desenvolvimento Full Stack Básico (PUC-RIO).

## Autor

Leonardo Rodrigues de Aguiar.


