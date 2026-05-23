from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

lista_clientes = []

#CLASE
class Cliente(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None

#RECONOCER CLIENTES 
@app.get("/clientes")
def listas_clientes():
    return {"Clientes": lista_clientes}

#NUEVO CLIENTE
@app.post("/clientes")
def new_cliente(datos_cliente: Cliente):
    for cliente in lista_clientes:
        if cliente.id == datos_cliente.id:   
    lista_clientes.append(datos_cliente)
    return {"mensaje": "Se creó el cliente", "cliente": datos_cliente}

#CONSULTA POR ID
@app.get("/clientes/{id}")
def cliente_por_id(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return {"Cliente": cliente}

#UPDATE
@app.put("/clientes/{id}")
def editar_cliente(id: int, datos_actualizados: Cliente):

    for indice, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            lista_clientes[indice] = datos_actualizados
            return {"mensaje": "Cliente actualizado correctamente", "cliente": datos_actualizados}
        


# DELETE
@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):

    for indice, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            cliente_eliminado = lista_clientes.pop(indice)
            return {"mensaje": f"Cliente con ID {id} eliminado", "cliente": cliente_eliminado}