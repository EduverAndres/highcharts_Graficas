from fastapi import APIRouter, Depends, HTTPException,  status
from sqlalchemy import func
from projects.ind_mantenimiento.models.models  import PAM_KPI001_model, PAM_KPI003_model
# PAM_KPI002_model,, PAM_KPI004_model,PAM_KPI005_model
from projects.ind_mantenimiento.schemas import schema_tabla_kpi001,schema_tabla_kpi002, schema_tabla_kpi003, schema_tabla_kpi004, schema_tabla_kpi005
from db_config.database_oracle import get_db_oracle
from sqlalchemy.orm import Session
from projects.ind_mantenimiento.functions import function





router = APIRouter()


#
@router.get("/gr1",response_model=list[schema_tabla_kpi001.PAM_KPI001_schema] ,status_code=status.HTTP_302_FOUND)
def read_all(db: Session=Depends(get_db_oracle)):
    
    

    db_datos = db.query(PAM_KPI001_model).order_by(PAM_KPI001_model.PROD_YEAR,PAM_KPI001_model.PROD_PER)
    
    if db_datos is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Registro no encontrado')
    db_datos = [function.model_to_dict(item) for item in db_datos]
    # excel_path=function.export_to_excel(db_datos, "Tabla 1")
    # function.generate_chart(excel_path,"Tabla 1")
    print(db_datos)
    return db_datos




@router.get("/gr2qty01")
def get_yearly_and_monthly_data(db: Session = Depends(get_db_oracle)):
    # Get distinct years from the database
    years = db.query(PAM_KPI001_model.PROD_YEAR).distinct().order_by(PAM_KPI001_model.PROD_YEAR).all()
    years = [year[0] for year in years]  # Extract years from tuples

    # Container for yearly data with nested monthly data
    data = []

    for year in years:
        # Get total QTY01 for the year
        yearly_total = db.query(
            func.sum(PAM_KPI001_model.QTY01).label('total_qty01')
        ).filter(PAM_KPI001_model.PROD_YEAR == year).scalar()

        # Get monthly data for the year
        monthly_data = db.query(
            PAM_KPI001_model.PROD_PER,
            func.sum(PAM_KPI001_model.QTY01).label('total_qty01')
        ).filter(
            PAM_KPI001_model.PROD_YEAR == year
        ).group_by(PAM_KPI001_model.PROD_PER).order_by(PAM_KPI001_model.PROD_PER).all()

        # Convert monthly data to list of dicts
        monthly_data_formatted = [{"PROD_PER": month, "total_qty01": total} for month, total in monthly_data]

        # Append yearly data with nested monthly data
        data.append({
            "PROD_YEAR": year,
            "total_qty01": yearly_total,
            "monthly_data": monthly_data_formatted
        })

    return data


@router.get("/gr2qty02")
def get_yearly_and_monthly_data(db: Session = Depends(get_db_oracle)):
    # Get distinct years from the database
    years = db.query(PAM_KPI001_model.PROD_YEAR).distinct().order_by(PAM_KPI001_model.PROD_YEAR).all()
    years = [year[0] for year in years]  # Extract years from tuples

    # Container for yearly data with nested monthly data
    data = []

    for year in years:
        # Get total QTY01 for the year
        yearly_total = db.query(
            func.sum(PAM_KPI001_model.QTY02).label('total_qty02')
        ).filter(PAM_KPI001_model.PROD_YEAR == year).scalar()

        # Get monthly data for the year
        monthly_data = db.query(
            PAM_KPI001_model.PROD_PER,
            func.sum(PAM_KPI001_model.QTY02).label('total_qty02')
        ).filter(
            PAM_KPI001_model.PROD_YEAR == year
        ).group_by(PAM_KPI001_model.PROD_PER).order_by(PAM_KPI001_model.PROD_PER).all()

        # Convert monthly data to list of dicts
        monthly_data_formatted = [{"PROD_PER": month, "total_qty02": total} for month, total in monthly_data]

        # Append yearly data with nested monthly data
        data.append({
            "PROD_YEAR": year,
            "total_qty02": yearly_total,
            "monthly_data": monthly_data_formatted
        })

    return data


@router.get("/readt3",response_model=list[schema_tabla_kpi003.PAM_KPI003_schema] ,status_code=status.HTTP_302_FOUND)
def read_all(db: Session=Depends(get_db_oracle)):
    db_datos = db.query(PAM_KPI003_model.PROD_PER, PAM_KPI003_model.PROD_PER,PAM_KPI003_model.QTY01).order_by(PAM_KPI003_model.PROD_YEAR)
    if db_datos is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Registro no encontrado')
    #db_datos = [function.model_to_dict(item) for item in db_datos]
    excel_path=function.export_to_excel(db_datos, "Tabla 3")
    function.generate_chart(excel_path,"Tabla 3")
    return db_datos


@router.get("/gr2prueba")
def get_yearly_and_monthly_data(db: Session = Depends(get_db_oracle)):
    # Get distinct years from the database
    years = db.query(PAM_KPI001_model.PROD_YEAR).distinct().order_by(PAM_KPI001_model.PROD_YEAR).all()
    years = [year[0] for year in years]  # Extract years from tuples

    # Container for yearly data with nested monthly data
    data = []

    for year in years:
        # Get total QTY01 for the year
        
        yearly_totalq1 = db.query(
            func.sum(PAM_KPI001_model.QTY01).label('total_qty01')
        ).filter(PAM_KPI001_model.PROD_YEAR == year).scalar()
        
        yearly_totalq2 = db.query(
            func.sum(PAM_KPI001_model.QTY02).label('total_qty02')
        ).filter(PAM_KPI001_model.PROD_YEAR == year).scalar()
        
        yearly_totalRes = db.query(
            func.sum(PAM_KPI001_model.RESULTADO).label('total_Res')
        ).filter(PAM_KPI001_model.PROD_YEAR == year).scalar()

        # Get monthly data for the year
        monthly_dataQ1 = db.query(
            PAM_KPI001_model.PROD_PER,
            func.sum(PAM_KPI001_model.QTY01).label('total_qty01')
        ).filter(
            PAM_KPI001_model.PROD_YEAR == year
        ).group_by(PAM_KPI001_model.PROD_PER).order_by(PAM_KPI001_model.PROD_PER).all()
        
        monthly_dataQ2 = db.query(
            PAM_KPI001_model.PROD_PER,
            func.sum(PAM_KPI001_model.QTY02).label('total_qty02')
        ).filter(
            PAM_KPI001_model.PROD_YEAR == year
        ).group_by(PAM_KPI001_model.PROD_PER).order_by(PAM_KPI001_model.PROD_PER).all()
        
        monthly_dataQ3 = db.query(
            PAM_KPI001_model.PROD_PER,
            func.sum(PAM_KPI001_model.RESULTADO).label('total_res')
        ).filter(
            PAM_KPI001_model.PROD_YEAR == year
        ).group_by(PAM_KPI001_model.PROD_PER).order_by(PAM_KPI001_model.PROD_PER).all()

        # Convert monthly data to list of dicts
        monthly_data_Q1= [{"PROD_PER": month, "total_qty01": total} for month, total in monthly_dataQ1]
        monthly_data_Q2= [{"PROD_PER": month, "total_qty02": total} for month, total in monthly_dataQ2]
        monthly_data_Res= [{"PROD_PER": month, "total_Resultado": total} for month, total in monthly_dataQ3]
        
        # monthly_data_all= [{"PROD_PER": month, "total_qty01": total, "total_qty02": total2, "total_Resultado": total3} for month, total in monthly_dataQ1, ]


        # Append yearly data with nested monthly data
        data.append({
            "PROD_YEAR": year,
            "total_qty01": yearly_totalq1,
            "total_qty02": yearly_totalq2,
            "total_res": yearly_totalRes,
            "monthly_dataQ1": monthly_data_Q1,
            "monthly_dataQ2": monthly_data_Q2,
            "monthly_dataQ3": monthly_data_Res,
            
        })

    return data
    # env\Scripts\activate.bat
    # uvicorn projects.ind_mantenimiento.main:app --reload --port 8004
    
    
    
#----------------------------------------------------------------------------------------------------------------------------------------------



    
    


