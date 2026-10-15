# Importamos todos los modelos acá para que:
# 1) Alembic pueda detectarlos a través de SQLModel.metadata al autogenerar migraciones.
# 2) Las relaciones (Relationship) entre modelos puedan resolverse correctamente,
#    ya que ambos archivos usan referencias "diferidas" (TYPE_CHECKING) entre sí.

from models.proveedores import Proveedor  # noqa: F401
from models.articulos import Articulo  # noqa: F401
