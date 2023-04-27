import base64
import qrcode
from io import BytesIO
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return '''
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <link
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
                    rel="stylesheet"
                    crossorigin="anonymous"
                />
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Saira+Condensed&display=swap" rel="stylesheet">
                <title>QR Code Generator</title>
                <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
                <script>
                    $(document).ready(function() {
                        $('#send-btn').click(function() {
                            var input_url = $('#input-url').val();
                            $.ajax({
                                url: '/qr',
                                type: 'GET',
                                data: {'s': input_url},
                                success: function(data) {
                                    $('#qr-code').attr('src', 'data:image/png;base64,' + data.image);
                                }
                            });
                        });
                    });
                </script>
            </head>
            <body style="font-family: 'Saira Condensed', sans-serif;">
              <div class="row align-items-center" style="height: 30vh;">
                <div class="mx-auto col-10 col-md-8 col-lg-6">
                  <!-- Form -->
                  <form class="form-example" action="qr" method="get">
                    <h1>QR Generator</h1>
                    <p class="description">Write your URL or text to make QR code for it. Also you can access API sending 'GET: /qr?s={YOUR_TEXT}'</p>
                    <!-- Input fields -->
                    <div class="input-group mb-3">
                      <input type="text" class="form-control" id="input-url" maxlength="255">
                      <button class="btn btn-outline-primary" id="send-btn" type="button">Generate</button>
                    </div>
                  </form>
                  <!-- Form end -->
                </div>
              </div>
              <div class="row align-items-center" style="height: 10vh;">
                <div class="d-flex justify-content-center">
                    <img id="qr-code" src="" alt="">
                </div>    
              </div>
            </body>
        </html>
    '''


@app.route("/qr")
def generate_qr():
    url = request.args.get('s')
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    img_bytes = img_io.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode()
    return jsonify({'image': img_base64})


if __name__ == '__main__':
    app.run()
