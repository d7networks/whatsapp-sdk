from typing import List, Optional, Union

from pydantic import BaseModel, Field


class TemplateMsg(BaseModel):
    messaging_product: str = "whatsapp"
    recipient_type: str = "individual"
    preview_url: bool = False
    to: str
