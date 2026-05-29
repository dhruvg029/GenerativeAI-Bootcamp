## Simple fetch from the NVIDIA APIs
from openai import OpenAI

## Get the client from NVIDIA with the API key
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1/",
    api_key = "<YOUR NVIDIA API KEY HERE>"
)

try:
    ## Call the completions API using an open-source model hosted by NVIDIA
    completion = client.chat.completions.create(
        model = "meta/llama-3.1-70b-instruct", 
        messages = [{"role": "user", "content": "How are you doing?"}],
        temperature = 0.5,
        top_p = 1,
        max_tokens = 1024,
        stream = True
    )

    ## Stream the response chunk by chunk
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)

except Exception as e:
    print(f"An error occurred: {e}")