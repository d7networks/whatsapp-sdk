"""
All constants and enums are defined here
"""
from enum import Enum


class FreeFormMsgType(str, Enum):
    """
    free-form messages types
    """
    TEXT = "text"
    REACTION = "reaction"
    MEDIA = "media"
    AUDIO = "audio"
    DOCUMENT = "document"
    IMAGE = "image"
    STICKER = "sticker"
    VIDEO = "video"
    LOCATION = "location"
    CONTACTS = "contacts"
    INTERACTIVE = "interactive"
    ADDRESS = "address"
    MESSAGES = "messages"


class MediaMsgType(str, Enum):
    AUDIO = "audio"
    DOCUMENT = "document"
    IMAGE = "image"
    STICKER = "sticker"
    VIDEO = "video"


class InteractiveMsgType(str, Enum):
    LIST = "list"
    BUTTON = "button"
    CTA_URL = "cta_url"


class AddressType(str, Enum):
    HOME = "HOME"
    WORK = "WORK"


class ComponentType(str, Enum):
    HEADER = "header"
    BODY = "body"
    FOOTER = "footer"
    BUTTON = "button"


class TemplateHeaderType(str, Enum):
    TEXT = "text"
    IMAGE = "image"


class ParameterType(str, Enum):
    IMAGE = "image"
    TEXT = "text"
    CURRENCY = "currency"
    DATE_TIME = "date_time"
    PAYLOAD = "payload"
    LOCATION = "location"
    DOCUMENT = "document"
    VIDEO = "video"
    
