import io
import os
import warnings
from pathlib import Path

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

from base64 import b64decode
from pathlib import Path
import os
import io
import warnings
# Our Host URL should not be prepended with "https" nor should it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# Sign up for an account at the following link to get an API Key.
# https://dreamstudio.ai/

# Click on the following link once you have created an account to be taken to your API Key.
# https://dreamstudio.ai/account

# Paste your API Key below.
os.environ['STABILITY_KEY'] = 'sk-uYyievZhJHctT307ZMV3vKeSgpRy0b3c922UUcguafqUBoMK'

# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # API Key reference.
    verbose=True, # Print debug messages.
    engine="stable-diffusion-xl-beta-v2-2-2", # Set the engine to use for generation. For SD 2.0 use "stable-diffusion-v2-0".
    # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0
    # stable-diffusion-512-v2-1 stable-diffusion-768-v2-1 stable-diffusion-xl-beta-v2-2-2 stable-inpainting-v1-0 stable-inpainting-512-v2-0
)
# Set up our initial generation parameters.

IMAGE_DIR = Path.cwd() / "generatedImage"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

for i in range(0,731):
    img = Image.open("test/img"+str(i)+".jpg")

    answers2 = stability_api.generate(
        prompt="space",
        start_schedule=0.6, # Set the strength of our prompt in relation to our initial image.
        init_image=img, # Assign our previously generated img as our Initial Image for transformation.
        width=1280, # Generation width, defaults to 512 if not included.
        height=720, # Generation height, defaults to 512 if not included.
    )

    fileName2 = "img"+str(i)+".jpg"

    for resp in answers2:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img2 = Image.open(io.BytesIO(artifact.binary))
                
                image_file2 = IMAGE_DIR / fileName2
                img2.save(image_file2) # Save our generated image with its seed number as the filename and the img2img suffix so that we know this is our transformed image.
                