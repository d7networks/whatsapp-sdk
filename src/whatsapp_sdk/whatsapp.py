import json
import logging
from typing import List

from .enums import FreeFormMsgType
from .request_schema import *
from .schema.template import Language, Template, TemplateMsg

log = logging.getLogger(__name__)


class Whatsapp:

    def __init__(self, client):
        self._client = client

    def send_free_form_message(
            self,
            msg_type: str = "text",
            recipient_type: str = "individual",
            to: str = None,
            recipient_id: str = None,
            preview_url: bool = False,
            media_link: str = None,
            media_id: str = None,
            text: str = None,
            msg_id: str = None,
            emoji: str = None,
            longitude: str = None,
            latitude: str = None,
            location_name: str = None,
            location_address: str = None,
            contacts: List[Contact] = [],
            header: Optional[Header] = None,
            body: Optional[Body] = None,
            footer: Optional[Footer] = None,
            action: Union[ListAction, CtaUrlAction, ButtonAction] = None,
            context:Optional[Context] = None,
            **kwargs
    ):
        """
        Supported message types:
        - Text
        - Reaction
        - Media
        - Location
        - Contacts
        - Interactive
        - Address messages
        :return:
        """
        msg_body = {}
        if msg_type == "text":
            if text is None:
                raise ValueError("Text cannot be empty")
            msg_body = WhatsappFreeFormTextMsg(to=to, text=Text(preview_url=preview_url, body=text), context=context)
        elif msg_type == "reaction":
            if emoji is None:
                raise ValueError("Emoji cannot be empty")
            if msg_id is None:
                raise ValueError("Message ID cannot be empty")
            msg_body = WhatsappFreeFormReactionMsg(to=to, reaction=Reaction(message_id=msg_id, emoji=emoji))
        elif msg_type == "image":
            if media_link is None and media_id is None:
                raise ValueError("Media Link  and Media ID cannot be empty")
            msg_body = WhatsappFreeFormMediaImageMsg(to=to, image=Media(link=media_link, id=media_id), context=context)
        elif msg_type == "video":
            if media_link is None and media_id is None:
                raise ValueError("Media Link  and Media ID cannot be empty")
            msg_body = WhatsappFreeFormMediaVideoMsg(to=to, video=Media(link=media_link, id=media_id), context=context)
        elif msg_type == "audio":
            msg_body = WhatsappFreeFormMediaAudioMsg(to=to, audio=Media(link=media_link, id=media_id), context=context)
        elif msg_type == "document":
            msg_body = WhatsappFreeFormMediaDocumentMsg(to=to, document=Media(link=media_link, id=media_id), context=context)
        elif msg_type == "sticker":
            msg_body = WhatsappFreeFormMediaStickerMsg(to=to, sticker=Media(link=media_link, id=media_id), context=context)
        elif msg_type == "location":
            msg_body = WhatsappFreeFormLocationMsg(
                to=to, 
                location=Location(longitude=longitude,latitude=latitude,name=location_name,address=location_address), 
                context=context
            )
        elif msg_type == "contact":
            msg_body = WhatsappFreeFormContactsMsg(to=to, contacts=contacts)       
        elif msg_type == "interactive":
            if action is None:
                raise ValueError("Action cannot be empty")
            if body is None:
                raise ValueError("Body cannot be empty")
            if type(action) == ListAction:
                msg_body = FreeFormInteractiveListMsg(
                    to=to,
                    interactive=InteractiveListMsg(header=header, body=body, footer=footer, action=action),
                    context=context
                )
            elif type(action) == ButtonAction:
                msg_body = FreeFormInteractiveReplyButtonMsg(
                    to=to,
                    interactive=InteractiveReplyButton(header=header, body=body, footer=footer, action=action),
                    context=context
                )
            elif type(action) == CtaUrlAction:
                msg_body = FreeFormInteractiveCtaButtonMsg(
                    to=to,
                    interactive=InteractiveCtaButton(header=header, body=body, footer=footer, action=action),
                    context=context
                )
            else:
                raise ValueError("Invalid action type")
        elif msg_type == "address":
            pass
        elif msg_type == "messages":
            pass
        else:
            raise ValueError("Invalid msg_type")
        return self._client.post(path="/messages", params=msg_body.model_dump())

    def send_template_message(
        self,
        name: str,
        to: str,
        language: str = "en",
        header: Optional[Header] = None,
        body: Optional[Body] = None,
        footer: Optional[Footer] = None,
        recipient_type: str = "individual",
    ):
        components = []
        if header is not None:
            components.append(header)
        if body is not None:
            components.append(body)
        if footer is not None:
            components.append(footer)
        template = Template(
            name=name,
            components=components,
            language=Language(code=language)
        )
        msg_body = TemplateMsg(to=to, template=template, recipient_type=recipient_type)
        msg_body_dict = msg_body.model_dump()
        return self._client.post(path="/messages", params=msg_body_dict)

    def mark_message_as_read(self):
        pass


if __name__ == '__main__':
    whatsapp = Whatsapp('client')
    whatsapp.send_free_form_message(msg_type="text", to="919876543210")
