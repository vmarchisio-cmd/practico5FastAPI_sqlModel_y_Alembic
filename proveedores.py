from sqlmodel import SQLModel

from models.proveedores import ProveedorBase


class ProveedorCreate(ProveedorBase):
    """Schema de entrada: datos para crear un proveedor (POST)."""
    pass


class ProveedorUpdate(SQLModel):
    """Schema de entrada: datos para editar un proveedor (PUT). Todo opcional."""
    nombre: str | None = None
    telefono: str | None = None
    email: str | None = None


class ProveedorRead(ProveedorBase):
    """Schema de salida: lo que devuelve la API (incluye el id)."""
    id: int
