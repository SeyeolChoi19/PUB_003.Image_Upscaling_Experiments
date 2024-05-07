import io, json

from PIL   import Image
from flask import Flask, jsonify, request, send_file

from image_upscaler.image_upscaler import image_upscaler

flask_image_upscaler_interface = Flask(__name__)

@flask_image_upscaler_interface.route("/convert", methods = ["POST"])
def upscale_image():
    original_name   = request.form["image_name"]
    binary_image    = request.files["image_file"]
    image_modifier  = int(request.form["upscale_modifier"])
    processed_image = image_upscaler(original_name, binary_image, image_modifier)
    
    return json.dumps({"processed_image" : processed_image})

if (__name__ == "__main__"):
    flask_image_upscaler_interface.run()
