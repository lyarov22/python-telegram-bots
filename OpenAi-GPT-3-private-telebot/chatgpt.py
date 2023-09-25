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
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=1,
    )

    response = completion.choices[0].text
    return response
