from flask import Flask, Jsonify, request

from image_upscaler.image_upscaler import image_upscaler

flask_image_upscaler_interface = Flask(__name__)

@flask_image_upscaler_interface.route("/convert", methods = ["POST"])
def upscale_image():
    original_name   = request.json["image_name"]
    binary_image    = request.json["image_file"]
    image_modifier  = request.json["upscale_modifier"]
    processed_image = image_upscaler(original_name, binary_image, image_modifier)
    return_object   = {
        "status" : f"{original_name} converted",
        "image"  : processed_image
    }

    return Jsonify(return_object)

if (__name__ == "__main__"):
    flask_image_upscaler_interface.run()