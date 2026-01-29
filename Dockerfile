FROM ubuntu:22.04

# Install General Requirements (Python 3.10 is native in Ubuntu 22.04)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create directory and set it as workdir
RUN mkdir /work
WORKDIR /work

# Copy dependencies and install them
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the code (including run.sh)
COPY . .

# Fix windows line endings and permissions
RUN sed -i 's/\r$//' run.sh
RUN chmod +x run.sh

# ENTRYPOINT is mandatory for passing arguments to the script
ENTRYPOINT ["./run.sh"]