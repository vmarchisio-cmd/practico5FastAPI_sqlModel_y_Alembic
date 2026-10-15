# Schemas "anidados": combinan datos de ambas entidades relacionadas
# (requisito del práctico: clases de SQLModel para datos anidados).
#
# Lo ponemos en un archivo aparte (en vez de meterlo directo en articulos.py o
# proveedores.py) para evitar import circular: este archivo importa de los dos,
# pero ninguno de los dos necesita importar este.

from typing import List, Optional
from pydantic import Field

from schemas.articulos import ArticuloRead
from schemas.proveedores import ProveedorRead


class ArticuloReadConProveedor(ArticuloRead):
    """Un artículo, incluyendo los datos completos de su proveedor (si tiene)."""
    proveedor: Optional[ProveedorRead] = None


class ProveedorReadConArticulos(ProveedorRead):
    """Un proveedor, incluyendo la lista completa de sus artículos."""
    articulos: List[ArticuloRead] = Field(default_factory=list)

