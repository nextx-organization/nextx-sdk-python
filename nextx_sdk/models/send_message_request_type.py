from typing import Literal

SendMessageRequestType = Literal['Audio', 'Comment', 'Contact', 'File', 'Image', 'Location', 'Product', 'Sticker', 'SystemNote', 'Text', 'Video']

SEND_MESSAGE_REQUEST_TYPE_VALUES: set[SendMessageRequestType] = { 'Audio', 'Comment', 'Contact', 'File', 'Image', 'Location', 'Product', 'Sticker', 'SystemNote', 'Text', 'Video',  }

def check_send_message_request_type(value: str) -> SendMessageRequestType:
    if value in SEND_MESSAGE_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEND_MESSAGE_REQUEST_TYPE_VALUES!r}")
