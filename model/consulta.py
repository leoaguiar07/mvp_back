from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from unidecode import unidecode
from model import Base, Regiao, Operadora


class Consulta(Base):
    __tablename__ = 'consulta'

    id = Column("pk_consulta", Integer, primary_key=True)
    nome = Column(String(140), nullable=False)
    nome_uniform = Column(String(140), nullable=False)
    celular = Column("celular", String(11), unique=True)
    gasto_atual = Column(Float, nullable=False)
    percentual_economia = Column(Float, nullable=False)
    gasto_simulado = Column(Float, nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre consulta e operadora.
    # Aqui está sendo definido a coluna 'id_operadora' que vai guardar
    # a referencia a operadora , a chave estrangeira que relaciona
    # uma consulta a operadora.
    id_operadora = Column(Integer, ForeignKey(
        "operadora.pk_operadora"), nullable=False)

    def __init__(self, nome: str, celular: str, gasto_atual: float,
                 percentual_economia: float, gasto_simulado: float,
                 id_operadora: int, data_insercao: Union[DateTime, None] = None):
        """
        Cria uma Consulta

        Arguments:
            nome: nome do usuário.
            celular: Número telefone celular usuario (21123456789)
            gasto_atual: gasto de energia atual
            percentual_economia: percentual aproximado possível a economizar
            gasto_simulado: valor simulado do possível gasto de energia
            data_insercao: data de quando o produto foi inserido à base
            id_operadora: id da operadora de energia ellétrica atual

        """
        self.nome = nome
        self.celular = celular
        self.gasto_atual = gasto_atual
        self.percentual_economia = percentual_economia
        self.gasto_simulado = gasto_simulado
        self.id_operadora = id_operadora
        self.nome_uniform = unidecode(nome).lower()
        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
