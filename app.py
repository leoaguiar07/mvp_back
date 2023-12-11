from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from unidecode import unidecode
from model import Session, Regiao, Operadora, Consulta

from logger import logger
from schemas import *
# from schemas import regiao_
from flask_cors import CORS

##


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# definindo tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
consulta_tag = Tag(
    name="Consulta",
    description="Adição, visualização e remoção de Consultas à base")
operadora_tag = Tag(
    name="Operadora",
    description="Lista todas as operadoras cadastradas na base de dados")
regiao_tag = Tag(
    name="Região",
    description="Lista todas as regiões cadastradas na base de dados")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/regioes', tags=[regiao_tag],
         responses={"200": ListagemRegioesSchema, "404": ErrorSchema})
def get_regioes():
    """Faz a busca por todas as regiões cadastradas

    Retorna uma representação da listagem de regiões.
    """
    logger.debug(f"Coletando regiões ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    regioes = session.query(Regiao).all()

    if not regioes:
        # se não há regiões cadastradas
        return {"regioes": []}, 200
    else:
        logger.debug(f"%d Regiões econtradas" % len(regioes))
        # retorna a representação de produto
        print(regioes)
        return apresenta_regioes(regioes), 200


@app.get('/operadora_regiao', tags=[operadora_tag],
         responses={"200": ListagemOperadorasSchema, "404": ErrorSchema})
def get_operadora_regiao(query: OperadoraRegiaoBuscaSchema):
    """Faz a busca por uma operadora a partir do id da regiao

    Retorna uma representação da operadora.
    """
    operadora_id_regiao = query.id_regiao
    logger.debug(
        f"Coletando dados sobre operadora de id = #{operadora_id_regiao}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    operadoras = session.query(Operadora).filter(
        Operadora.id_regiao == operadora_id_regiao).all()

    if not operadoras:
        # se a operadora não foi encontrado
        error_msg = "Operadora não encontrado na base"
        logger.warning(
            f"Erro ao buscar operadora de id_região =  '{operadora_id_regiao}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"%d operadoras econtradas" % len(operadoras))
        # retorna a representação de operadoras
        print(operadoras)
        return apresenta_operadoras(operadoras), 200

# ________


@app.get('/consultas', tags=[consulta_tag],
         responses={"200": ListagemConsultasSchema, "404": ErrorSchema})
def get_consultas():
    """Faz a busca por todas as consultas cadastradas

    Retorna uma representação da listagem de consulta.
    """
    logger.debug(f"Coletando consultas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    consultas = session.query(Consulta).all()

    if not consultas:
        # se não há consultas cadastradas
        return {"consultas": []}, 200
    else:
        logger.debug(f"%d Consultas econtradas" % len(consultas))
        # retorna a representação de consultas
        print(consultas)
        return apresenta_consultas(consultas), 200


@app.delete('/consulta', tags=[consulta_tag],
            responses={"200": ConsultaDelSchema, "404": ErrorSchema})
def del_consulta(query: ConsultaBuscaSchema):
    """Deleta uma consulta a partir do celular do usuário informado

    Retorna uma mensagem de confirmação da remoção.
    """

    # consulta_nome = unidecode(unquote(unquote(query.nome)).lower())
    consulta_celular = query.celular

    print(consulta_celular)
    logger.debug(f"Deletando dados sobre consulta #{consulta_celular}")
    # criando conexão com a basel
    session = Session()
    # fazendo a remoção
    count = session.query(Consulta).filter(
        Consulta.celular == consulta_celular).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado consulta #{consulta_celular}")
        return {"message": "Consulta removida", "Celular": query.celular}
    else:
        # se o produto não foi encontrado
        error_msg = "Consulta não encontrada na base"
        logger.warning(
            f"Erro ao deletar consulta #'{consulta_celular}', {error_msg}")
        return {"message": error_msg}, 404


def get_operadora_id(operadora_id):
    """Faz a busca por um operadora a partir do id da operadora

    Retorna operadora.
    """
    # operadora_id = query.id
    logger.debug(f"Coletando dados sobre operadora #{operadora_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    operadora = session.query(Operadora).filter(
        Operadora.id == operadora_id).first()

    if not operadora:
        # se o produto não foi encontrado
        error_msg = "Operadora não encontrado na base"
        logger.warning(
            f"Erro ao buscar operadora '{operadora_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Operadora econtrada: '{operadora.nome}'")
        # retorna a representação de operadora
        return operadora


@app.post('/consulta', tags=[consulta_tag],
          responses={"200": ConsultaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_consulta(form: ConsultaSchema):
    """Adiciona uma nova consulta à base de dados

    Retorna uma representação das consultas.
    """
    operadora_id = form.id_operadora
    operadora = get_operadora_id(operadora_id)
    percentual_economia = operadora.percentual_reducao
    gasto_atual = form.gasto_atual
    gasto_simulado = gasto_atual-(gasto_atual*(percentual_economia/100))
    consulta_celular = form.celular

    consulta = Consulta(
        nome=form.nome,
        celular=form.celular,
        gasto_atual=form.gasto_atual,
        # gasto_simulado=form.gasto_simulado,
        id_operadora=form.id_operadora,
        percentual_economia=percentual_economia,
        gasto_simulado=gasto_simulado
    )

    logger.debug(f"Adicionando consulta de celular: '{consulta.celular}'")
    try:
        # criando conexão com a base
        session = Session()

        # fazendo a busca
        consulta_db = session.query(Consulta).filter(
            Consulta.celular == consulta_celular).first()

        if not consulta_db:
            # se a CONSULTA não foi encontrado
            # adicionando consulta
            session.add(consulta)
            # efetivando o camando de adição de novo item na tabela
            session.commit()
            logger.debug(
                f"Adicionado consulta com celular: '{consulta.celular}'")
            return apresenta_consulta(consulta), 200
        else:
            logger.debug(
                f"Atualizando consulta com celular: '{consulta.celular}'")
            # efetivando o camando de adição de novo item na tabela

            consulta_db.nome = consulta.nome
            # celular=form.celular,
            consulta_db.gasto_atual = consulta.gasto_atual
            consulta_db.gasto_simulado = consulta.gasto_simulado
            consulta_db.id_operadora = consulta.id_operadora
            consulta_db.percentual_economia = consulta.percentual_economia
            # consulta_db.gasto_simulado = gasto_simulado

            session.commit()
            return apresenta_consulta(consulta), 200

    except IntegrityError as e:
        # como a duplicidade do CELULAR é a provável razão do IntegrityError
        error_msg = "Consulta com mesmo celular já salva na base"
        logger.warning(
            f"Erro ao adicionar consulta '{consulta.celular}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item"
        logger.warning(
            f"Erro ao adicionar consulta '{consulta.celular}', {error_msg}")
        return {"message": error_msg}, 400
