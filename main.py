
from dotenv import load_dotenv
from agents import Runner,Agent, AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig
import os
import sys

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")



if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

desiredLan=None

agent =Agent(
    name='Fucking Translator',
    instructions=f'you are translator/interpreter agent fro human languages, translate the given text to this {desiredLan or 'urdu'}'
)
userInput=str(input('Enter the text to translate: '))
desiredLan=str(input('Enter language in which you want output asshole: '))

res= Runner.run_sync(
    agent,
    input=userInput,
    run_config=config,
)
print(res)

sys.exit()
