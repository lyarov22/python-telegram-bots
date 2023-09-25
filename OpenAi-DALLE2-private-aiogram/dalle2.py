import os
import pip
pip.main(['install', 'openai'])

import openai

apikey = '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'
openai.api_key = apikey

def returnPrompt(msg):
    prompt = msg

    response = openai.Image.create(
     prompt=prompt,
     n=1,
    size="1024x1024"
    )
    return response['data'][0]['url']