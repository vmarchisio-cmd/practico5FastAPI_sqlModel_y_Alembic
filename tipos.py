from typing import Annotated

from sqlmodel import Field

# Modularizar los tipos personalizados (Type Aliases)
# La nomenclatura recomendada es PascalCase, entonces quedaría:
# Nota: ahora usamos Field de SQLModel (superset de pydantic.Field),
# así son compatibles tanto con schemas normales como con modelos de tabla.

IntPositivo = Annotated[int, Field(gt=0)]
StrCortito = Annotated[str, Field(max_length=30)]
IntPrecioVenta = Annotated[int, Field(gt=500, lt=999999)]
BoolActivo = Annotated[bool, Field(description="Sigue disponible?")]
