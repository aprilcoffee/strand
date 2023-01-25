import transformers 
from PIL import Image
#device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
pipe = transformers.pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

width = 512
height = 512
url = f"https://picsum.photos/{width}/{height}"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
image = image.resize((width, height))


print ( pipe(image)[0]["generated_text"])