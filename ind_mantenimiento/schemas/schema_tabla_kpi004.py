from datetime import date
from typing import Optional
#pydantic
from pydantic import BaseModel

class PAM_KPI004_schema(BaseModel):
    PROD_YEAR: int
    PROD_PER: int
    ASSETNO_PPAL: str
    QTY01: Optional[int] = None
    QTY02: Optional[int] = None
    RESULTADO: Optional[float] = None
    SYSTEMDATE: Optional[date] = None

class USFAD001T_schema(PAM_KPI004_schema):
    __annotations__ = {k: Optional[v] for k, v in PAM_KPI004_schema.__annotations__.items()}
    