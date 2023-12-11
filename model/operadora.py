from datetime import datetime
from typing import Union
from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from model import Base, Regiao


class Operadora(Base):
    __tablename__ = 'operadora'

    id = Column("pk_operadora", Integer, primary_key=True)
    nome = Column(String(140), unique=True, nullable=False)
    percentual_reducao = Column(Float, nullable=False)

    # Definição do relacionamento entre operadora e região.
    # Aqui está sendo definido a coluna 'id_regiao' que vai guardar
    # a referencia a região , a chave estrangeira que relaciona
    # uma operadora a região.
    id_regiao = Column(Integer, ForeignKey("regiao.pk_regiao"), nullable=False)

    def __init__(self, nome: str, percentual_reducao: float, id_regiao: int):
        """
        Cria uma Operadora

        Arguments:
            nome: nome do produto.
            percentual_reducao: percentual de economia referente a operadora
            id_regiao: Identificador de Região
        """
        self.nome = nome
        self.percentual_reducao = percentual_reducao
        self.id_regiao = id_regiao

    