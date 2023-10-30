from typing import Optional, List
from pydantic import BaseModel


class WASuccessResponse(BaseModel):
    pass


class WAErrorResponse(BaseModel):
    pass


class Contact(BaseModel):
    input: str
    wa_id: str


class Message(BaseModel):
    id: str
    message_status: str


class ErrorData(BaseModel):
    messaging_product: str
    details: str


class Error(BaseModel):
    message: str
    type: str
    code: int
    error_data: ErrorData
    fbtrace_id: str


class WASuccessResponse(BaseModel):
    messaging_product: Optional[str] = None
    contacts: Optional[List[Contact]] = None
    messages: Optional[List[Message]] = None


class WAErrorResponse(BaseModel):
    error: Optional[Error] = None
