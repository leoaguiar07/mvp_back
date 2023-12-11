from pydantic import BaseModel
from typing import Optional, List
from model.operadora import Operadora


class OperadoraSchema(BaseModel):
    """ Define como um nova operadora a ser inserida deve ser representada
    """
    id: int = 1
    nome: str = "Sudeste"
    percentual_reducao: float = 22.65
    id_regiao: int = 5


class ListagemOperadorasSchema(BaseModel):
    """ Define como uma listagem de operadoras será retornada.
    """
    operadoras: List[OperadoraSchema]


def apresenta_operadoras(operadoras: List[Operadora]):
    """ Retorna uma representação da Operadora seguindo o schema definido em
        OperadoraViewSchema.
    """
    result = []
    for operadora in operadoras:
        result.append({
            "id": operadora.id,
            "nome": operadora.nome,
            "percentual_reducao": operadora.percentual_reducao,
            "id_regiao": operadora.id_regiao
        })

    return {"operadoras": result}


class OperadoraViewSchema(BaseModel):
    """ Define como uma Operadora será retornada.
    """
    id: int = 1
    nome: str = "Sudeste"
    percentual_reducao: float = 22.65
    id_regiao: int = 5


def apresenta_operadora(operadora: Operadora):
    """ Retorna uma representação da Operadora seguindo o schema definido em
        OperadoraViewSchema.
    """
    return {
        "id": operadora.id,
        "nome": operadora.nome,
        "percentual_reducao": operadora.percentual_reducao,
        "id_regiao": operadora.id_regiao,
    }


class OperadoraBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id da operadora.
    """
    id: int = 30


class OperadoraRegiaoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id da operadora.
    """
    id_regiao: int = 3
