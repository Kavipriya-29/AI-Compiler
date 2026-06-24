from pydantic import BaseModel
from typing import Dict,List

class PromptRequest(BaseModel):
    prompt:str

class AppSchema(BaseModel):

    ui:Dict
    api:Dict
    database:Dict
    auth:Dict
    assumptions:List[str]