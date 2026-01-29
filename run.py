import pandas as pd
import os
import argparse
from dotenv import load_dotenv
from utils import parse_and_print
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found. Check your .env file")

def load_data(data_path="./dataset/sales.csv"):

    df = pd.read_csv(data_path, sep=";", 
            parse_dates=['date'], dayfirst=True, 
            dtype={'promotion_type': str})
    return df

def initialize_llm(model="models/gemini-2.5-flash", 
                   temperature=0, max_output_tokens=2048):

    llm = ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        max_output_tokens=max_output_tokens
    )
    return llm

def start_agent(llm, df, verbose=True, allow_dangerous_code=True, agent_type="openai-tools"):

    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=verbose,
        allow_dangerous_code=allow_dangerous_code,
        agent_type=agent_type 
    )
    return agent

def query_agent(query, agent):

    try:
        response = agent.invoke(query)
        response = response['output']
        response = parse_and_print(response)
        print(f"#####\nquery : {query}\n#####")
        print(f"response : {response}\n#####")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():

    parser = argparse.ArgumentParser(
        description="Program to interfacing an agent using a csv dataset"
    )
    parser.add_argument("--data_path", type=str, 
        help="The path to dataset to be used by the model."
    )
    parser.add_argument("--model", type=str,
        help="Model the agent is based on"
    )
    parser.add_argument("--max_output_tokens", type=str,
        help="The max amount of tokens to be generated"
    )
    parser.add_argument("--verbose", type=str,
        help="How much text traces the model will print before the output"
    )
    parser.add_argument("--query", type=str,
        help="Input to the model"
    )
    args = parser.parse_args()

    data_path = args.data_path
    model = args.model 
    verbose = args.verbose
    max_output_tokens = args.max_output_tokens
    query = args.query

    df = load_data(data_path)
    llm = initialize_llm(model, max_output_tokens=max_output_tokens)
    agent = start_agent(llm, df, verbose)
    query_agent(query, agent)

if __name__ == "__main__":
    main()