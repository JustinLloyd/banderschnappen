import json
import math
import os
import re

import openai
import tiktoken

openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatGPT:
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"
    MAX_TOKENS_4K = 4096
    MAX_TOKENS_16K = 16384

    def __init__(self, response_name=None, preferred_model=GPT_3_5_TURBO_16K, temperature=0.2, top_p=0.95):
        print(os.getenv("OPENAI_API_KEY"))
        self.encoder = tiktoken.encoding_for_model(ChatGPT.GPT_3_5_TURBO_16K)
        self.preferred_model = preferred_model
        self.encoder = tiktoken.encoding_for_model(preferred_model)
        self.temperature = temperature
        self.top_p = top_p
        self.messages = []
        self.response = {}
        self.response_name = response_name

    def estimate_token_message(self):
        estimated_tokens = sum([len(self.encoder.encode(msg['content'])) for msg in self.messages])
        print(f"Estimated number of tokens = {estimated_tokens}")
        return estimated_tokens

    def get_content(self):
        # add some error checking here
        # remove triple quotes from the start and end of string, if they exist, strip out the XML tags we use to embed data
        content = self.response['choices'][0]['message']['content']
        content = re.sub(r'^"{3}|"{3}$', '', content)
        content = re.sub(r'^<data>|</data>$', '', content)
        return content

    def add_system_message(self, message):
        self.messages.append({"role": "system", "content": message})
        return self.messages

    def save_response(self, response):
        self.response = response
        # emit debug log message indicating that no response name is set, so we will skip saving the response to a specific file
        if not os.path.exists('responses'):
            os.makedirs('responses')

        if self.response_name:
            with open(f'responses/{self.response_name}.json', 'w') as file:
                json.dump(self.response, file)

        # consider switching to a sqlite db or using am ndjson file instead
        if os.path.exists(f'responses/responses.json'):
            with open(f'responses/responses.json') as file:
                responses = json.load(file)
        else:
            responses = []

        responses.append(self.response)
        with open(f'responses/responses.json', 'w') as file:
            json.dump(responses, file)

    def has_cached_response(self):
        return os.path.exists(f'responses/{self.response_name}.json')

    def load_response(self):
        if os.path.exists(f'responses/{self.response_name}.json'):
            print(f"responses/{self.response_name}.json exists, so we're loading that instead")
            with open(f'responses/{self.response_name}.json') as file:
                self.response = json.load(file)
        return self.response

    def invoke_gpt_4k(self, temperature=None, top_p=None, max_tokens=MAX_TOKENS_4K):
        if max_tokens > ChatGPT.MAX_TOKENS_4K:
            raise ValueError(f"Maximum number of tokens is {ChatGPT.MAX_TOKENS_4K}")

        return self._invoke_gpt(preferred_model=ChatGPT.GPT_3_5_TURBO, temperature=temperature, top_p=top_p, max_tokens=max_tokens)

    def invoke_warm_16k(self, top_p=None, max_tokens=MAX_TOKENS_16K):
        if max_tokens > ChatGPT.MAX_TOKENS_16K:
            raise ValueError(f"Maximum number of tokens is {ChatGPT.MAX_TOKENS_16K}")

        return self.invoke_gpt_16k(temperature=0.4, top_p=top_p, max_tokens=max_tokens)

    def invoke_gpt_16k(self, temperature=None, top_p=None, max_tokens=MAX_TOKENS_16K):
        if max_tokens > ChatGPT.MAX_TOKENS_16K:
            raise ValueError(f"Maximum number of tokens is {ChatGPT.MAX_TOKENS_16K}")

        return self._invoke_gpt(preferred_model=ChatGPT.GPT_3_5_TURBO_16K, temperature=temperature, top_p=top_p, max_tokens=max_tokens)

    def _invoke_gpt(self, preferred_model, temperature=None, top_p=None, max_tokens=MAX_TOKENS_16K):
        if preferred_model != ChatGPT.GPT_3_5_TURBO and preferred_model != ChatGPT.GPT_3_5_TURBO_16K:
            raise ValueError(f"Model must be not specified, {ChatGPT.GPT_3_5_TURBO} or {ChatGPT.GPT_3_5_TURBO_16K}")

        if preferred_model == ChatGPT.GPT_3_5_TURBO:
            max_permitted_tokens = ChatGPT.MAX_TOKENS_4K
        elif preferred_model == ChatGPT.GPT_3_5_TURBO_16K:
            max_permitted_tokens = ChatGPT.MAX_TOKENS_16K
        else:
            max_permitted_tokens = ChatGPT.MAX_TOKENS_4K

        if max_tokens > max_permitted_tokens:
            raise ValueError("You cannot specify more tokens than the model can handle")

        response = openai.ChatCompletion.create(
            model=preferred_model,
            messages=self.messages,
            # max_tokens=min(max_tokens, max_permitted_tokens - self.estimate_token_message()),
            temperature=temperature if temperature else self.temperature,
            top_p=top_p if top_p else self.top_p,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        self.save_response(response)
        return response

    def add_assistant_message(self, message):
        self.messages.append({"role": "assistant", "content": message})
        return self.messages

    def add_user_message(self, message):
        self.messages.append({"role": "user", "content": message})
        return self.messages

    def get_message(self):
        return self.messages


ChatGPT()
