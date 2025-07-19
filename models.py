from pydantic import BaseModel, Field
from typing import Optional

class Language(BaseModel):
    id: int
    name: str = Field(..., description="Name of the language")
    type: Optional[str] = Field(None, description="Compiled / Interpreted / Hybrid")
    is_static: Optional[bool] = Field(None, description="Is statically typed?")
    data_types: Optional[list[str]] = Field(None, description="Core data types")
    year: Optional[int] = Field(None, description="Year of creation")
    usage_side: Optional[str] = Field(None, description="Backend / Frontend / Fullstack")
    creator: Optional[str] = Field(None, description="Language creator")
    country: Optional[str] = Field(None, description="Origin country")
    typical_use: Optional[str] = Field(None, description="Games / Web / AI / etc.")
