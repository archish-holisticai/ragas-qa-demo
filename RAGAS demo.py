# -*- coding: utf-8 -*-
"""RAGAS_demo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UgVIPiwH1yZJccEaNgPEwU3vUeBns30A
"""

!pip install langchain

!pip install langchain_community

!pip install llama_index

!pip install xmltodict
from langchain_community.document_loaders import PubMedLoader
loader = PubMedLoader("liver", load_max_docs=10)
documents = loader.load()

!pip install ragas
from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from google.colab import userdata
import os
os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")

# generator with openai models
generator_llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
critic_llm = ChatOpenAI(model="gpt-4")
embeddings = OpenAIEmbeddings()

generator = TestsetGenerator.from_langchain(
    generator_llm,
    critic_llm,
    embeddings
)

# Change resulting question type distribution
distributions = {
    simple: 0.5,
    multi_context: 0.4,
    reasoning: 0.1
}

# use generator.generate_with_llamaindex_docs if you use llama-index as document loader
testset = generator.generate_with_langchain_docs(documents, 10, distributions)
testset.to_pandas()

