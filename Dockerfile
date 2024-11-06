FROM ubuntu:22.04

# Set the working directory in the container
WORKDIR /usr/src/app

# Avoid prompts from apt and set frontend to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Update and install Python, pip, and necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl gnupg unixodbc-dev lsb-release && \
    curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc && \
    curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | tee /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools && \
    rm -rf /var/lib/apt/lists/*

# Set PATH to include /opt/mssql-tools/bin
ENV PATH="$PATH:/opt/mssql-tools/bin"

# Copy the requirements file into the container
COPY requirements.txt ./

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code
COPY . .

# Command to run the application
CMD ["dagster", "dev", "-f", "Dagster.py", "-h",  "0.0.0.0", "-p", "3000"]
