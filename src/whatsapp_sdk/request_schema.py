from typing import List, Optional, Union

from pydantic import BaseModel, Field

from .enums import (AddressType, FreeFormMsgType, InteractiveMsgType,
                    MediaMsgType)


# -------------- Reply Messages --------------
class Context(BaseModel):
    message_id: str


class WhatsappFreeFormMsg(BaseModel):
    messaging_product: str = "whatsapp"
    recipient_type: str = "individual"
    preview_url: bool = False
    to: str
    context: Optional[Context] = None


# -------------- Text Messages --------------

class Text(BaseModel):
    preview_url: bool = False
    body: str


class WhatsappFreeFormTextMsg(WhatsappFreeFormMsg):
    type: FreeFormMsgType = FreeFormMsgType.TEXT
    text: Text


# -------------- Reaction Messages --------------

class Reaction(BaseModel):
    message_id: str
    emoji: str


class WhatsappFreeFormReactionMsg(WhatsappFreeFormMsg):
    type: FreeFormMsgType = FreeFormMsgType.REACTION
    reaction: Reaction


# -------------- Media Messages --------------

class Media(BaseModel):
    link: Union[str, None] = None
    id: Union[str, None] = None


class WhatsappFreeFormMediaImageMsg(WhatsappFreeFormMsg):
    type: MediaMsgType = MediaMsgType.IMAGE
    image: Media


class WhatsappFreeFormMediaVideoMsg(WhatsappFreeFormMsg):
    type: MediaMsgType = MediaMsgType.VIDEO
    video: Media


class WhatsappFreeFormMediaAudioMsg(WhatsappFreeFormMsg):
    type: MediaMsgType = MediaMsgType.AUDIO
    audio: Media


class WhatsappFreeFormMediaDocumentMsg(WhatsappFreeFormMsg):
    type: MediaMsgType = MediaMsgType.DOCUMENT
    document: Media


class WhatsappFreeFormMediaStickerMsg(WhatsappFreeFormMsg):
    type: MediaMsgType = MediaMsgType.STICKER
    sticker: Media


# -------------- Location Messages --------------

class Location(BaseModel):
    longitude: str = None,
    latitude: str = None
    name: Optional[str] = None
    address: Optional[str] = None


class WhatsappFreeFormLocationMsg(WhatsappFreeFormMsg):
    type: FreeFormMsgType = FreeFormMsgType.LOCATION
    location: Location


# -------------- Contacts Messages --------------

class Name(BaseModel):
    formatted_name: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    suffix: Optional[str] = None
    prefix: Optional[str] = None


class Phone(BaseModel):
    phone: Optional[str] = None
    type: Optional[str] = None


class Url(BaseModel):
    url: Optional[str] = None
    type: Optional[str] = None


class Organization(BaseModel):
    company: Optional[str] = None
    department: Optional[str] = None
    title: Optional[str] = None


class Email(BaseModel):
    email: Optional[str] = None
    type: Optional[str] = None


class Address(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    type: Optional[AddressType] = None


class Contact(BaseModel):
    addresses: Optional[list[Address]] = None
    birthday: Optional[str] = None  # YEAR_MONTH_DAY
    emails: Optional[list[Email]] = None
    name: Name
    org: Optional[Organization] = None
    phones: Optional[list[Phone]] = None
    urls: Optional[list[Url]] = None


class WhatsappFreeFormContactsMsg(WhatsappFreeFormMsg):
    type: FreeFormMsgType = FreeFormMsgType.CONTACTS
    contacts: List[Contact]


# -------------- Interactive Messages --------------

class Header(BaseModel):
    type: str = "text"
    text: str


class Body(BaseModel):
    text: str


class Footer(BaseModel):
    text: str


class Row(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None


class Section(BaseModel):
    title: str
    rows: List[Row]


class Reply(BaseModel):
    id: str
    title: Optional[str] = None


class ReplyButton(BaseModel):
    type: str = "reply"
    reply: Reply


class CtaParameters(BaseModel):
    display_text: str
    url: str


class ListAction(BaseModel):
    button: str
    sections: List[Section]


class ButtonAction(BaseModel):
    buttons: List[ReplyButton]


class CtaUrlAction(BaseModel):
    name: str = "cta_url"
    parameters: CtaParameters


class InteractiveBase(BaseModel):
    header: Optional[Header] = None
    body: Body
    footer: Optional[Footer] = None


class InteractiveListMsg(InteractiveBase):
    type: InteractiveMsgType = InteractiveMsgType.LIST
    action: ListAction


class InteractiveReplyButton(InteractiveBase):
    type: InteractiveMsgType = InteractiveMsgType.BUTTON
    action: ButtonAction


class InteractiveCtaButton(InteractiveBase):
    type: InteractiveMsgType = InteractiveMsgType.CTA_URL
    action: CtaUrlAction


class FreeFormInteractiveListMsg(WhatsappFreeFormMsg):
    type: FreeFormMsgType = FreeFormMsgType.INTERACTIVE
    interactive: InteractiveListMsg


class FreeFormInteractiveReplyButtonMsg(WhatsappFreeFormMsg):
    type: FreeFormMsgType = FreeFormMsgType.INTERACTIVE
    interactive: InteractiveReplyButton


class FreeFormInteractiveCtaButtonMsg(WhatsappFreeFormMsg):
    type: FreeFormMsgType = FreeFormMsgType.INTERACTIVE
    interactive: InteractiveCtaButton
