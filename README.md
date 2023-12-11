# Mercado Livre de Energia - API

Em setembro de 2022, o governo federal publicou uma portaria que permite a migração de todos os 
consumidores ligados em alta tensão para o Mercado Livre de Energia. A partir de janeiro de 2024,
qualquer tipo de negócio, como padaria ou restaurante, poderão ser beneficiados.

Os preços de aquisição de energia são menores no mercado livre.
Os fornecedores e consumidores negociam as condições de compra e venda de energia. 
Fatores como preços, prazos, fonte da geração e flexibilidades são discutidos entre as duas partes.

Pesquisando inúmeros sites, verifiquei que não era possível ter uma noção da redução de gasto, 
todos exibiam um formulário onde o usuário deveria informar seus dados pessoais 
e de sua conta de energia para um posterior contato.<br>

Com isso a página permite que os usuários possam simular a sua redução de gasto com sua conta de energia elétrica, atráves de um simulador. Informando Nome, Celular, Região e Operadora de energia atual. Tendo como resultado o gasto simulado, percentual de economia e valor da economia.<br>

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


