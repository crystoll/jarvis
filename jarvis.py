from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

if __name__ == "__main__":
    print('hello world!')
    # response = client.chat.completions.create(
    #     model="gpt-4",
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": "What is love?",
    #         }
    #     ])
    # print(f'ChatGPT response: {response}')
