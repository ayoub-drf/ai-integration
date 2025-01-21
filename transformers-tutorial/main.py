import requests
from PIL import Image
from transformers import pipeline

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/coco_sample.png"
image_data = requests.get(url, stream=True).raw
image = Image.open(image_data)

object_detector = pipeline('object-detection')

print(object_detector(image))
