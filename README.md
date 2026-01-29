## Sales Agent

The sales agent is an example of a LLM-based agent application. It contains a dataset (in a csv format) with sales information, and provide responses for queries about the content of the document.

This page contains instructions for running it.

1. Install the most up to date version of [Docker](https://www.docker.com/get-started/).
2. Download this repository on your local machine.
3. Unzip it.
4. On your terminal, access the root of the repository folder you just unzipped.
5. Create a `.env` file.
6. Open the `.env` file, and type `GOOGLE_API_KEY=your_google_api_key`
5. Type `DOCKER_BUILDKIT=0 docker build -t sales-agent .`
6. Then, type `sh ./docker_run.sh`
