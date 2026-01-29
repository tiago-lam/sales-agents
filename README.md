## Sales Agent

The sales agent is an example of a LLM-based agent application. It contains a dataset (in a csv format) with sales information, and provide responses for queries about the content of the document.

This page contains instructions for running it.

1. Install the most up to date version of [Docker](https://www.docker.com/get-started/).
2. Download this repository on your local machine.
3. Unzip it.
4. On your terminal, access the root of the repository folder you just unzipped.
5. Create a `.env` file.
6. Open the `.env` file, and type `GOOGLE_API_KEY=your_google_api_key`. Save it.
7. Back on the terminal, type `DOCKER_BUILDKIT=0 docker build -t sales-agent .`
8. Then, type `sh ./docker_run.sh`
9. After a few seconds you will see on the terminal, the agent response to a pre-selected query on the `docker_run.sh` file.

## How to send other queries to the agent

The `docker_run.sh` file is a wrapper for the `docker run` command. It contains basic parameters to control the agent's output, such as:

- `--verbose` : `(True | False)` It defines how much text traces the agent will print before the output. It's useful if you want to see the Pandas functions the agent uses to answer the queries.
- `--max_output_tokens` : `(Integer)` The max amount of tokens to be generated
- `query` : `(String)` The input to the agent.

Therefore, if you want to see how the agent responds to other queries, you just need to change the `query` value and run the command `sh ./docker_run.sh` again.


