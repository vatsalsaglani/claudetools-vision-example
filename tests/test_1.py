import json
import base64
import requests
import mimetypes
from typing import Dict


def get_payload(image_path: str):
    media_type, _ = mimetypes.guess_type(image_path)
    if not media_type:
        raise Exception(f"Unable to determine the media type for {image_path}")

    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
    except IOError:
        raise Exception(f"Error opening image file {image_path}")

    image_base64 = base64.b64encode(image_data).decode('utf-8')

    return {"image_str": image_base64, "media_type": media_type}


def make_call(payload: Dict):
    response = requests.post("http://localhost:8890/api/extract", json=payload)
    data = response.json()
    return data


if __name__ == "__main__":
    # payload = get_payload("./images/test_img_1.png")
    # payload = get_payload("./images/test_img_LR_1.png")
    # payload = get_payload("./images/test_img_LR_2.png")
    payload = get_payload("./images/test_img_LR_3.png")
    print(json.dumps(make_call(payload), indent=4))
