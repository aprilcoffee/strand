import io
import os
import warnings
from base64 import b64decode
from pathlib import Path

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

import config

os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = config.stabilityAPI
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # API Key reference.
    verbose=True, # Print debug messages.
    # Set the engine to use for generation. For SD 2.0 use "stable-diffusion-v2-0".
    #engine="stable-diffusion-768-v2-1"
    engine="stable-diffusion-v1-5", 
    )

def generate(_prompt, _img):
    answers = stability_api.generate(
        prompt=_prompt,
        init_image=_img, # Assign our previously generated img as our Initial Image for transformation.
        start_schedule=0.6, # Set the strength of our prompt in relation to our initial image.
        #seed=123467458, # If attempting to transform an image that was previously generated with our API,
                        # initial images benefit from having their own distinct seed rather than using the seed of the original image generation.
        steps=30, # Amount of inference steps performed on image generation. Defaults to 30. 
        cfg_scale=8.0, # Influences how strongly your generation is guided to match your prompt.
                    # Setting this value higher increases the strength in which it tries to match your prompt.
                    # Defaults to 7.0 if not specified.
        width=1024, # Generation width, defaults to 512 if not included.
        height=1024, # Generation height, defaults to 512 if not included.
        sampler=generation.SAMPLER_K_DPMPP_2M # Choose which sampler we want to denoise our generation with.
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                #img.save(str(artifact.seed)+ "-img2img.png") 
                # Save our generated image with its seed number as the filename and the img2img suffix so that we know this is our transformed image.
    return img


imageDir = Path.cwd() / "output"
imageDir.mkdir(parents=True, exist_ok=True)


img = Image.open("code/images/border.png")
for i in range(5):
    generate("",img).save(imageDir / ("border_output_new_"+str(i)+".png"))
