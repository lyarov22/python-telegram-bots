import openai

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY
# you can name this function anything you want, the name "logic" is arbitrary
# Set up the model and prompt
model_engine = "text-davinci-003"

def returnPrompt(msg):
    prompt = msg #"y =x^2, g = x^2 + 2, describe transformations of the function"

# Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=1,
    )

    response = completion.choices[0].text
    return response