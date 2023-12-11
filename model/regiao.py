from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Regiao(Base):
    __tablename__ = 'regiao'

    id = Column("pk_regiao", Integer, primary_key=True)
    nome = Column(String(140), unique=True, nullable=False)

   # data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome: str):
        """
        Cria uma Região

        Arguments:
            nome: nome da região.
            data_insercao: data de quando a região foi inserida à base
        """
        self.nome = nome
