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

# Add a new user called "user"
RUN useradd -m user

# Make our user own its own home directory 
RUN chown -R user:user /home/user/

# Copy all files from this directory to a directory called app 
COPY --chown=user *.* /home/user/app

# Change user to user 
USER user 
RUN mkdir /home/user/data/ 

# Install all of the requirements 
RUN cd /home/user/app/ && pip3 install -r requirements.txt

# Download wordnet 
RUN python -c "import nltk; nltk.download('wordnet')"

# When we log into docker container it will go inside directory automatically
WORKDIR /home/user/app

    

