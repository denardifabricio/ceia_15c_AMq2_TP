from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from typing import List

app = FastAPI()

@app.get("/")
async def read_root():
    """
    Root endpoint of the Heart Disease Detector API.

    This endpoint returns a JSON response with a welcome message to indicate that the API is running.
    """
    return JSONResponse(content=jsonable_encoder({"message": "La Api de parámetros está funcionando correctamente"}))


@app.get("/currencies", response_model=List[str])
async def get_states():
    return ['USD', '$']

@app.get("/operationtypes", response_model=List[str])
async def get_operation_types():
    return ['Venta', 'En Pozo']



@app.get("/countries", response_model=List[str])
async def get_countries():
    return ["Argentina"]

@app.get("/states", response_model=List[str])
async def get_states():
    return ["Capital Federal"]

@app.get("/cities", response_model=List[str])
async def get_cities():
    return ['Belgrano', 'Recoleta', 'Parque Chacabuco', 'Monserrat', 'Palermo', 'Retiro', 
          'Villa Crespo', 'Barrio Norte', 'Flores', 'Caballito', 'Núñez', 'Boedo', 'Floresta', 
          'Balvanera', 'Villa Urquiza', 'Almagro', 'Colegiales', 'Liniers', 'Chacarita', 
          'Centro / Microcentro', 'Barracas', 'Once', 'Congreso', 'Villa del Parque', 'San Cristobal', 
          'Versalles', 'San Telmo', 'La Paternal', 'La Boca', 'Parque Centenario', 'Constitución', 
          'Villa General Mitre', 'Villa Devoto', 'Abasto', 'Saavedra', 'Mataderos', 'Coghlan', 
          'Villa Ortuzar', 'Monte Castro', 'Parque Patricios', 'San Nicolás', 'Tribunales', 
          'Villa Pueyrredón', 'Villa Luro', 'Villa Lugano', 'Otro', 'Puerto Madero', 'Catalinas', 
          'Velez Sarsfield', 'Villa Santa Rita', 'Parque Chas', 'Pompeya', 'Parque Avellaneda', 
          'Agronomía', 'Villa Real', 'Villa Soldati', 'Villa Riachuelo']