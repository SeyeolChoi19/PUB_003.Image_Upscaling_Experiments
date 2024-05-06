import io, os

from PIL         import Image
from super_image import EdsrModel, ImageLoader

def image_upscaler(image_file_name: str, image_file: str, upscale_modifier: int):    
    def convert_image_to_binary(image_file_name: str, upscale_modifier: int):
        with open(f"upscaled_{upscale_modifier}_{image_file_name}", "rb") as f:
            binary_image_string = f.read()        

        os.remove(f"upscaled_{upscale_modifier}_{image_file_name}")

        return binary_image_string

    binary_data    = io.BytesIO(image_file)
    original_image = Image.open(binary_data)
    upscaler_model = EdsrModel.from_pretrained("eugenesiow/edsr", scale = upscale_modifier)
    input_image    = ImageLoader.load_image(original_image)
    upscaled_image = upscaler_model(input_image)    
    ImageLoader.save_image(upscaled_image, f"upscaled_{upscale_modifier}_{image_file_name}")    

    return convert_image_to_binary(image_file_name, upscale_modifier)