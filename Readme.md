# Autost

Autost is a powerful automation platform designed to streamline and manage your data processing workflows using Dagster. This project leverages Docker for containerization, ensuring a consistent and scalable environment for deployment.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Using Docker](#using-docker)
- [Configuration](#configuration)
  - [Strategy Configuration](#strategy-configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Containerized Environment:** Utilize Docker to ensure a consistent setup across different environments.
- **Dagster Integration:** Manage and orchestrate data pipelines efficiently with Dagster.
- **Dynamic Configuration:** Easily configure strategies and scripts through JSON configuration files.
- **Asynchronous Execution:** Execute scripts asynchronously with countdown functionality for better performance.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Docker:** Make sure Docker is installed on your machine. You can download it from [here](https://www.docker.com/get-started).
- **Docker Compose (optional):** If you plan to use Docker Compose for multi-container setups.
- **Git:** For cloning the repository.

## Installation

### Using Docker

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/autost.git
   cd autost
   ```

2. **Build the Docker Image**

   Build the Docker image using the provided `Dockerfile`.

   ```bash
   docker build -t autost:latest .
   ```

3. **Run the Docker Container**

   Run the Docker container from the built image.

   ```bash
   docker run -d -p 3000:3000 --name autost_container autost:latest
   ```

   - The application will be accessible at `http://localhost:3000`.

## Configuration

Autost uses JSON configuration files to manage strategies and scripts.

### Strategy Configuration

Located at `autost/dagster/config.json`, this file defines various strategies with their scheduling and execution details.
