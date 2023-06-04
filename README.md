# Onboarding API - OpenAI ChatGPT-4 Plugin

This repository contains a **proof-of-concept (PoC)** project demonstrating the potential of OpenAI's ChatGPT-4 plugins in streamlining complex procedures, such as the onboarding of new clients or providers into a company. The Onboarding API plugin provides a conversational interface, aiming to make these processes more user-friendly and efficient.


## Overview
The Onboarding API interacts with key entities such as Software, Client, and Permission. It provides a CRUD REST API, defined using the OpenAPI (Swagger) specification, enabling operators to view and filter software, clients, and permissions.

This PoC was built using Python and the Quart async web framework, adhering to Domain-Driven Design principles to ensure organized and maintainable code. For the purpose of this PoC, we implemented in-memory data structures for storage, making it ideal for demonstration and testing purposes.

<img src="https://user-images.githubusercontent.com/11739105/243170004-0502948a-1f79-4d18-a05b-6ccca60d7001.png" alt="screenshot">

## Note
While this is not a production-ready solution, it serves as a valuable exploration of the capabilities of ChatGPT-4 plugins. The insights gained from this project will undoubtedly contribute to future developments.

## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like "What is on my todo list" and then try adding something to it as well! 

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
