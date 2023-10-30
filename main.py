from src.whatsapp_sdk.client import Client

API_TOKEN = "EAAFRdFR07ToBO1Lc7lfbytQsu4A1zaQOSrBf5ZCT0pZBvA0ATa4uCbT7cGo7S5Ly7O5C6cjC8O9Oh42azOeX0ZCwZBMPXUgjVXjxNc9bnoBd6frhPb9Ua4Xa7582226fy7DdR24DmXgjfARZC8ZBJrcDU0pwfNgRJHprFFGFtH8bhftdfhE44RKwtt3QrOyluOV6ZBt3MXPusdNOXhXZCtZA56H4nCFYZD"
PHONE_NUMBER_ID = "112252381489646"

if __name__ == '__main__':
    client = Client(api_token=API_TOKEN, phone_number_id=PHONE_NUMBER_ID)
    # response = client.whatsapp.send_free_form_message(msg_type="text", to="+971509001994", text="Welcome to D7 Networks")
    # print(response)
    message_id = "wamid.HBgMOTcxNTA5MDAxOTk0FQIAERgSQkY2N0YxRDhERDk3QUZGNkIwAA=="
    # send reaction
    # response = client.whatsapp.send_free_form_message(msg_type="reaction", to="+971509001994", msg_id=message_id, emoji="😀")
    # print(response)
    # send  media image
    # response = client.whatsapp.send_free_form_message(msg_type="image", to="+971509001994", media_link="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png")
    # print(response)
    # send media video
    # response = client.whatsapp.send_free_form_message(msg_type="video", to="+971509001994", media_link="http://www.onirikal.com/videos/mp4/nestlegold.mp4")
    # print(response)
    # send media audio
    # response = client.whatsapp.send_free_form_message(msg_type="audio", to="+971509001994", media_link="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    # print(response)
    # send document
    # response = client.whatsapp.send_free_form_message(msg_type="document", to="+971509001994", media_link="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
    # print(response)
    # send sticker
    # response = client.whatsapp.send_free_form_message(msg_type="sticker", to="+971509001994", media_link="https://raw.githubusercontent.com/sagarbhavsar4328/dummys3bucket/master/sample3.webp")
    # print(response)
    # send location
    response = client.whatsapp.send_free_form_message(msg_type="location", to="+971509001994", longitude="25.2048",
                                                      latitude="55.2708", location_name="Dubai",
                                                      location_address="Dubai")
    print(response)
