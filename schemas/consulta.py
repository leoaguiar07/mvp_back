from pydantic import BaseModel
from typing import Optional, List
from model.consulta import Consulta


class ConsultaSchema(BaseModel):
    """ Define como um nova consulta a ser inserida deve ser representada
    """
    # id: int = 1
    nome: str = "João Silva"
    celular: str = "21123456789"
    gasto_atual: float = 520.00
    # percentual_economia: float = 25.12
    # gasto_simulado: float = 370.00
    id_operadora: int = 12


class ListagemConsultasSchema(BaseModel):
    """ Define como uma listagem de consultas será retornada.
    """
    # consultas: List[ConsultaSchema]
    # id: int = 1
    nome: str = "João Silva"
    celular: str = "21123456789"
    gasto_atual: float = 520.00
    percentual_economia: float = 25.12
    gasto_simulado: float = 370.00
    id_operadora: int = 12


class ListagemConsultasLimitadasSchema(BaseModel):
    """ Define como uma listagem de consultas limitadas será retornada.
    """
    # consultas: List[ConsultaSchema]
    # id: int = 1
    nome: str = "João Silva"
    # celular: str = "21123456789"
    gasto_atual: float = 520.00
    percentual_economia: float = 25.12
    gasto_simulado: float = 370.00
    id_operadora: int = 12


def apresenta_consultas(consultas: List[Consulta]):
    """ Retorna uma representação da Consulta seguindo o schema definido em
        ConsultaViewSchema.
    """
    result = []
    for consulta in consultas:
        result.append({
            # "id": consulta.id,
            "nome": consulta.nome,
            "celular": consulta.celular,
            "gasto_atual": consulta.gasto_atual,
            "percentual_economia": consulta.percentual_economia,
            "gasto_simulado": consulta.gasto_simulado,
            "id_operadora": consulta.id_operadora,

        })

    return {"consultas": result}


def apresenta_consultas_limitadas(consultas: List[Consulta]):
    """ Retorna uma representação da Consulta limitada seguindo o schema definido em
        ConsultaViewSchema.
    """
    result = []
    for consulta in consultas:
        result.append({
            # "id": consulta.id,
            "nome": consulta.nome,
            # "celular": consulta.celular,
            "gasto_atual": consulta.gasto_atual,
            "percentual_economia": consulta.percentual_economia,
            "gasto_simulado": consulta.gasto_simulado,
            "id_operadora": consulta.id_operadora,

        })

    return {"consultas": result}


class ConsultaViewSchema(BaseModel):
    """ Define como uma Consulta será retornada.
    """
   # id: int = 1
    nome: str = "João Silva"
    celular: str = "21123456789"
    gasto_atual: float = 520.00
    percentual_economia: float = 25.12
    gasto_simulado: float = 370.00
    id_operadora: int = 12


class ConsultaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da consulta.
    """
#    nome: str = "Nome"
    celular: str = "celular"


def apresenta_consulta(consulta: Consulta):
    """ Retorna uma representação da Consulta seguindo o schema definido em
        ConsultaViewSchema.
    """
    return {
        # "id": consulta.id,
        "nome": consulta.nome,
        "celular": consulta.celular,
        "gasto_atual": consulta.gasto_atual,
        "percentual_economia": consulta.percentual_economia,
        "gasto_simulado": consulta.gasto_simulado,
        "id_operadora": consulta.id_operadora,

    }


class ConsultaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str
