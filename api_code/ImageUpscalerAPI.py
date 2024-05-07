import io 

from PIL   import Image
from flask import Flask, jsonify, request, send_file

from image_upscaler.image_upscaler import image_upscaler

flask_image_upscaler_interface = Flask(__name__)

@flask_image_upscaler_interface.route("/convert", methods = ["POST"])
def upscale_image():
    original_name   = request.form["image_name"]
    binary_image    = request.files["image_file"]
    image_modifier  = int(request.form["upscale_modifier"])
    processed_image = Image.open(image_upscaler(original_name, binary_image, image_modifier))
    bufferer_object = io.BytesIO()
    processed_image.save(bufferer_object, format = "jpg")
    bufferer_object.seek(0)

    return send_file(bufferer_object, mimetype = "image/jpeg")
 
if (__name__ == "__main__"):
    flask_image_upscaler_interface.run()
