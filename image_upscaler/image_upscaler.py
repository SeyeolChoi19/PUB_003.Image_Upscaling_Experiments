import io

from PIL         import Image
from super_image import EdsrModel, ImageLoader

def image_upscaler(image_file: str, upscale_modifier: int):    
    binary_data    = io.BytesIO(image_file)
    original_image = Image.open(binary_data)
    upscaler_model = EdsrModel.from_pretrained("eugenesiow/edsr", scale = upscale_modifier)
    input_image    = ImageLoader.load_image(original_image)
    upscaled_image = upscaler_model(input_image)
    output_stream  = io.BytesIO()
    upscaled_image.save(output_stream, format = "JPEG")    

    return output_stream.get_value()
