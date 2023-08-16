import os
import pip
pip.main(['install', 'openai'])

import openai

apikey = os.environ['API_KEY']
openai.api_key = apikey

def returnPrompt(msg):
    prompt = msg

# Generate a response
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    response = completion.choices[0].text
    return response
