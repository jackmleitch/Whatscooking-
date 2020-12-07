# Include where we get the image from (operating system)
FROM ubuntu:18.04

# We cannot press Y so we do it automatically 
RUN apt-get update && apt-get install -y \
    git \
    curl \
    ca-certificates \
    python3 \
    python3-pip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /whatscooking 
ADD . /whatscooking

# Install all of the requirements 
RUN pip3 install -r requirements.txt

# Download wordnet 
RUN python3 -c "import nltk; nltk.download('wordnet')"



    

