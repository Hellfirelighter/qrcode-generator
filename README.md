## Ultra simple QR Generator

## About

Ultra simple web application that can generate QR-Code image from text string. You can use its API by sending GET request to "/qr" endpoint with "url" parameter that contains your text, like:

http://127.0.0.1/qr?url=www.google.com (if running locally)

in response you will get an JSON with BASE64 encoded PNG image.

## Installation

- First of all you need to install dependencies: "pip install flask qrcode"
- Then run application "python app.py"
- Finish. Yes, that's all you need to do.

In fact, you can run it in container or somewhere else on your server or host it using special service
