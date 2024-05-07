import io, os

from PIL         import Image
from super_image import EdsrModel, ImageLoader

def image_upscaler(image_file_name: str, binary_image_file: str, upscale_modifier: int):    
    def convert_image_to_binary(image_file_name: str, upscale_modifier: int):
        with open(f"upscaled_{upscale_modifier}_{image_file_name}", "rb") as f:
            binary_image_string = f.read()        

        os.remove(f"upscaled_{upscale_modifier}_{image_file_name}")

        return binary_image_string

    original_image = Image.open(binary_image_file)
    upscaler_model = EdsrModel.from_pretrained("eugenesiow/edsr", scale = upscale_modifier)
    input_image    = ImageLoader.load_image(original_image)
    upscaled_image = upscaler_model(input_image)    
    ImageLoader.save_image(upscaled_image, f"upscaled_{upscale_modifier}_{image_file_name}")    

    binary_image = convert_image_to_binary(image_file_name, upscale_modifier)
    Image.open(binary_image).show()

    return binary_image
