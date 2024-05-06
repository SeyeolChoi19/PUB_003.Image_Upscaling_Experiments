import os

from PIL         import Image
from super_image import EdsrModel, ImageLoader

from concurrent.futures import ThreadPoolExecutor

def image_upscaler(input_file_name: str, output_file_name: str, upscale_modifier: int):    
    original_image = Image.open(input_file_name)
    upscaler_model = EdsrModel.from_pretrained("eugenesiow/edsr", scale = upscale_modifier)
    input_image    = ImageLoader.load_image(original_image)
    upscaled_image = upscaler_model(input_image)    
    ImageLoader.save_image(upscaled_image, output_file_name)    

def convert_files(upscale_modifier: int, input_directory: str, output_directory: str, files_list: list[str]):
    with ThreadPoolExecutor(max_workers = 4) as executor: 
        for file_name in files_list: 
            file_extension = file_name.split(".")[-1].lower()

            if (file_extension in ["jpg", "jpeg", "png"]):
                input_file_name  = os.path.join(input_directory, file_name)
                output_file_name = os.path.join(output_directory, f"upscaled_{file_name}")
                executor.submit(image_upscaler, input_file_name, output_file_name, upscale_modifier)

if (__name__ == "__main__"):
    files_list = os.listdir("C:/Users/User/Downloads")
    convert_files(4, "C:/Users/User/Downloads", "C:/Users/User/Pictures", files_list)