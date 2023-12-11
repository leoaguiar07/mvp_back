from pydantic import BaseModel
from typing import Optional, List
from model.regiao import Regiao


class RegiaoSchema(BaseModel):
    """ Define como um nova região a ser inserida deve ser representada
    """
    id: int = 1
    nome: str = "Sudeste"


class ListagemRegioesSchema(BaseModel):
    """ Define como uma listagem de regiões será retornada.
    """
    regioes: List[RegiaoSchema]


def apresenta_regioes(regioes: List[Regiao]):
    """ Retorna uma representação da região seguindo o schema definido em
        RegiaoViewSchema.
    """
    result = []
    for regiao in regioes:
        result.append({
            "id": regiao.id,
            "nome": regiao.nome,
        })

    return {"regioes": result}


class RegiaoViewSchema(BaseModel):
    """ Define como uma região será retornada.
    """
    id: int = 1
    nome: str = "Sudeste"


def apresenta_regiao(regiao: Regiao):
    """ Retorna uma representação da região seguindo o schema definido em
        RegiaoViewSchema.
    """
    return {
        "id": regiao.id,
        "nome": regiao.nome,
    }
