
from pydantic import BaseModel, Field


#* payload
class SamplePayload(BaseModel):
    type_name: str = Field(
        title="SAMPLE1 or SAMPLE2", 
        max_length=50
    )
    id: int = Field(
        title="ID number"
    )
    labels: list[str]
    service: str | None = Field(
        default= None, 
        title="Lables"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "type_name": "SAMPLE1",
                "id": 12345,
                "labels": ["label1", "label2"],
            }
        }


class SomeEnum:
    
    STATUS:str = "Testing"

