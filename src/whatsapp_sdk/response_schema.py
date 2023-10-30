from pydantic import BaseModel, Field


class Contact(BaseModel):
    input: str
    wa_id: str


class MessageDetails(BaseModel):
    id: str  # "wamid.ID"


class WhatsappMsgResponse(BaseModel):
    messaging_product: str = "whatsapp"
    contacts: list[Contact] = Field(..., alias="contacts")
    messages: list[MessageDetails] = Field(..., alias="messages")