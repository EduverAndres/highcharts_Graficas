from sqlalchemy import Column, Integer, Float, Date,String
from sqlalchemy.dialects.oracle import VARCHAR, FLOAT
#db_config
from db_config.database_oracle import Base_oracle


class BASE_MODEL(Base_oracle):
    __abstract__ = True
    def to_dict(self):
        return {field.name:getattr(self, field.name) for field in self.__table__.c}
    

class PAM_KPI001_model(Base_oracle):
    "En espera del señor Jairo"
    __tablename__ = "PAM_KPI001"
    __table_args__ = {"schema": "MSDB1"}
    comment = "Este es el modelo de connecion a la tabla en la base de datos relacionada"
    PROD_YEAR = Column(Integer, primary_key=True, nullable=False, comment="Año de produccion")
    PROD_PER = Column(Integer, primary_key=True, nullable=False, comment="Periodo de prueba")
    QTY01 = Column(Integer, nullable=False, comment="En espera del señor Jairo")
    QTY02 = Column(Integer, nullable=False, comment="En espera del señor Jairo")
    RESULTADO = Column(Float, nullable=True, comment="Resultado")
    SYSTEMDATE = Column(Date, nullable=False, comment="En espera del señor Jairo")
    
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
# class PAM_KPI002_model(Base_oracle):
#     "En espera del señor Jairo"
#     __tablename__ = "PAM_KPI002"
#     __table_args__ = {"schema": "MSDB1"}
#     comment = "Este es el modelo de connecion a la tabla en la base de datos relacionada"
#     PROD_YEAR = Column(Integer, primary_key=True, nullable=False, comment="Año de produccion")
#     WEEKOFYEAR = Column(Integer, primary_key=True, nullable=False, comment="Periodo de prueba")
#     QTY01 = Column(Integer, nullable=False, comment="En espera del señor Jairo")
#     QTY02 = Column(Integer, nullable=False, comment="En espera del señor Jairo")
#     RESULTADO = Column(FLOAT, nullable=True, comment="Resultado")
#     SYSTEMDATE = Column(Date, nullable=False, comment="En espera del señor Jairo")
    
    
    
    #------------------------------------------------------------------------------------------------------------------------------------------------------
class PAM_KPI003_model(Base_oracle):
    "En espera del señor Jairo"
    __tablename__ = "PAM_KPI003"
    __table_args__ = {"schema": "MSDB1"}
    comment = "Este es el modelo de connecion a la tabla en la base de datos relacionada"
    PROD_YEAR = Column(Integer, primary_key=True, nullable=False, comment="Año de produccion")
    PROD_PER = Column(Integer, primary_key=True, nullable=False, comment="Periodo de prueba")
    ASSETNO_PPAL=Column(String(5),nullable=False)
    QTY01 = Column(Float, nullable=False, comment="En espera del señor Jairo")
    QTY02 = Column(Float, nullable=False, comment="En espera del señor Jairo")
    RESULTADO = Column(Float, nullable=True, comment="Resultado")
    SYSTEMDATE = Column(Date, nullable=False, comment="En espera del señor Jairo")



    
#------------------------------------------------------------------------------------------------------------------------------------------------------

# class PAM_KPI004_model(Base_oracle):
#     "En espera del señor Jairo"
#     __tablename__ = "PAM_KPI004"
#     __table_args__ = {"schema": "MSDB1"}
#     comment = "Este es el modelo de connecion a la tabla en la base de datos relacionada"
#     PROD_YEAR = Column(Integer, primary_key=True, nullable=False, comment="Año de produccion")
#     PROD_PER = Column(Integer, primary_key=True, nullable=False, comment="Periodo de prueba")
#     ASSETNO_PPAL= Column(nullable=False)
#     QTY01 = Column(Integer, nullable=False, comment="En espera del señor Jairo")
#     QTY02 = Column(Integer, nullable=False, comment="En espera del señor Jairo")
#     RESULTADO = Column(FLOAT, nullable=True, comment="Resultado")
#     SYSTEMDATE = Column(Date, nullable=False, comment="En espera del señor Jairo")


# class PAM_KPI005_model(Base_oracle):
#     "En espera del señor Jairo"
#     __tablename__ = "PAM_KPI005"
#     __table_args__ = {"schema": "MSDB1"}
#     comment = "Este es el modelo de connecion a la tabla en la base de datos relacionada"
#     PROD_YEAR = Column(Integer, primary_key=True, nullable=False, comment="Año de produccion")
#     PROD_PER = Column(Integer, primary_key=True, nullable=False, comment="Periodo de prueba")
#     QTY01 = Column(Integer, nullable=True, comment="En espera del señor Jairo")
#     QTY02 = Column(Integer, nullable=True, comment="En espera del señor Jairo")
#     RESULTADO = Column(Float, nullable=True, comment="Resultado")
#     SYSTEMDATE = Column(Date, nullable=True, comment="En espera del señor Jairo")