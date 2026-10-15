from sqlmodel import SQLModel

from models.articulos import ArticuloBase


class ArticuloCreate(ArticuloBase):
    """Schema de entrada: datos para crear un artículo (POST)."""
    pass


class ArticuloUpdate(SQLModel):
    """Schema de entrada: datos para editar un artículo (PUT). Todo opcional."""
    nombre: str | None = None
    precio: int | None = None
    activo: bool | None = None
    proveedor_id: int | None = None


class ArticuloRead(ArticuloBase):
    """Schema de salida: lo que devuelve la API (incluye el id)."""
    id: int
