from typing import List, Optional, Union

from pydantic import BaseModel, Field

from ..enums import ComponentType, ParameterType


class Language(BaseModel):
    code: str = "en_US"


class Image(BaseModel):
    """
    Image object
    """
    link: str


class Video(BaseModel):
    """
    Video object
    """
    link: str

class Document(BaseModel):
    """
    Document object
    """
    link: str

class Location(BaseModel):
    """
    Location object
    """
    latitude: float
    longitude: float
    name: str
    address: str


class Currency(BaseModel):
    fallback_value: str
    code: str = "USD"
    amount_1000: int = 0


class DateTime(BaseModel):
    fallback_value: str = ""  # MONTH DAY, YEAR


class ImageParameter(BaseModel):
    type: ParameterType = ParameterType.IMAGE
    image: Image


class TextParameter(BaseModel):
    type: ParameterType = ParameterType.TEXT
    text: str


class VideoParameter(BaseModel):
    type: ParameterType = ParameterType.VIDEO
    video: Video


class DocumentParameter(BaseModel):
    type: ParameterType = ParameterType.DOCUMENT
    document: Document


class LocationParameter(BaseModel):
    type: ParameterType = ParameterType.LOCATION
    location: Location


class DateTimeParameter(BaseModel):
    type: ParameterType = ParameterType.DATE_TIME
    date_time: DateTime


class CurrencyParameter(BaseModel):
    type: ParameterType = ParameterType.CURRENCY
    currency: Currency

class PayloadParameter(BaseModel):
    type: ParameterType = ParameterType.PAYLOAD
    payload: str



class Header(BaseModel):
    type: ComponentType = ComponentType.HEADER
    parameters: List[
        Union[
            TextParameter,
            ImageParameter,
            VideoParameter,
            DocumentParameter,
            LocationParameter
        ]
    ] = []


class Body(BaseModel):
    type: ComponentType = ComponentType.BODY
    parameters: List[
        Union[
            TextParameter,
            CurrencyParameter,
            DateTimeParameter
        ]
    ] = []


class Footer(BaseModel):
    type: ComponentType = ComponentType.FOOTER
    parameters: List[TextParameter] = []


class Template(BaseModel):
    name: str
    language: Language
    components: List[Union[Header, Body, Footer]]


class TemplateMsg(BaseModel):
    messaging_product: str = "whatsapp"
    recipient_type: str = "individual"
    type: str = "template"
    to: str
    template: Template
