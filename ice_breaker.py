import os
import requests
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
if api_key:
    print(f"API Key cargada correctamente: {api_key}")
else:
    print("API Key no encontrada. Revisa el archivo .env")

information = """Elon Reeve Musk (Pretoria, June 28, 1971) is a conservative businessman, investor, and political activist 4​5and tycoon.footnote 1He is the founder, CEO, and chief engineer of SpaceX; angel investor, CEO and product architect of Tesla, Inc.; founder of The Boring Company; and co-founder of Neuralink and OpenAI.footnote 2In addition, he is the chief technology officer of X Corp.6Currently, since January 2025, he has served as administrator of the White House Department of Government Efficiency in the second administration of Donald Trump.7​8​

With an estimated net worth of about four hundred billion dollars in December 2024,9he is the richest person in the world according to the Forbes Real-Time Billionaires Index.10​11​

Musk was born and raised in a wealthy family in Pretoria, South Africa. His mother is Canadian and his father is a white South African. He studied briefly at the University of Pretoria before moving to Canada at age 17. He enrolled at Queen's University and transferred to the University of Pennsylvania two years later, where he majored in Economics and Physics. In 1995 he moved to California to attend Stanford University, but instead decided to pursue an entrepreneurial career, co-founding the web software company Zip2 with his brother Kimbal. Zip2 was acquired by Compaq for $307 million in 1999. That same year, Musk co-founded the online bank X.com, which merged with Confinity in 2000 to form PayPal. The company was bought by eBay in 2002 for $1.5 billion.

In 2002, Musk founded SpaceX, an aerospace manufacturer and space transportation services company, of which he is CEO and chief engineer. In 2003, he joined electric vehicle manufacturer Tesla Motors, Inc. (now Tesla, Inc.) as president and product architect, becoming its CEO in 2008. In 2006, he helped create SolarCity, a solar energy services company that was later acquired by Tesla and became Tesla Energy. In 2015, he co-founded OpenAI, a non-profit research company that promotes friendly artificial intelligence. In 2016, he co-founded Neuralink, a neurotechnology company focused on developing brain-computer interfaces, and founded The Boring Company, a tunnel construction company. It also agreed to buy the major U.S. social network Twitter in 2022 for $44 billion. Musk has also proposed the hyperloop. In November 2021, Tesla's CEO was the first person in history to amass a fortune of three hundred billion dollars.12​

He has been criticized for making unscientific and controversial statements. In 2018, he was sued by the U.S. Securities and Exchange Commission (SEC) for falsely tweeting that he had secured financing for a private takeover of Tesla. He settled with the SEC but did not admit guilt, temporarily resigning from his chairmanship and agreeing to limitations on his use of Twitter. In 2019, he won a libel suit brought against him by a British spelunker who advised on the rescue of Tham Luang Cave. Musk has also been criticized for spreading misinformation about the COVID-19 pandemic and conspiracy theories; and for his controversial opinions on matters such as artificial intelligence, cryptocurrencies and public transport.
"""

if __name__ == "__main__":
    print("Hello Langchain!")

    summary_template = """
given the information {information} abaut a person from I want you to create:
1. translate spanish a short summary
2. two interesting facts abaout them like you are a farmer without internet en español
"""

summary_prompt_templates = PromptTemplate(
    input_variables=["information"], template=summary_template
)


def call_azure_openai(prompt: str, azure_endpoint: str, api_key: str) -> str:
    """Make a call to Azure OpenAI endpoint"""
    headers = {"Content-Type": "application/json", "api-key": api_key}

    payload = {"messages": [{"role": "user", "content": prompt}]}

    response = requests.post(azure_endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Azure OpenAI API call failed: {response.text}")


prompt = summary_prompt_templates.format(information=information)


res = call_azure_openai(prompt, azure_endpoint, api_key)

print(res)
