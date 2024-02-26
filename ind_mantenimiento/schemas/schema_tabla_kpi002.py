from datetime import date
from typing import Optional
#pydantic
from pydantic import BaseModel

class PAM_KPI002_schema(BaseModel):
    PROD_YEAR: int
    WEEKOFYEAR: int
    QTY01: Optional[int] = None
    QTY02: Optional[int] = None
    RESULTADO: Optional[float] = None
    SYSTEMDATE: Optional[date] = None

class USFAD001T_schema(PAM_KPI002_schema):
    __annotations__ = {k: Optional[v] for k, v in PAM_KPI002_schema.__annotations__.items()}
    