# Dialogflow Chatbot Project

## Overview
This project is a chatbot built using [Dialogflow](https://dialogflow.cloud.google.com/), designed to handle simple conversational flows. It integrates with a webhook for currency conversion functionalities, with two webhook versions available:
1. **Version 1 (Hardcoded Conversion Rates)**: Uses hardcoded currency conversion rates for simplicity and offline use.
2. **Version 2 (Real-Time API Integration)**: Integrates with the [Currency Conversion API](https://www.currencyconverterapi.com/) to fetch real-time exchange rates.

The project uses Flask as the web framework to host the webhook and supports testing through the [ngrok](https://ngrok.com/) tunneling service.

## Features
- **Dialogflow Integration**: Handles intents and entities for natural language processing.
- **Currency Conversion**: Converts between currencies dynamically based on the version of the webhook you choose.
- **Flask Webhook**: Webhook is implemented in Python using Flask.
- **Real-Time API**: Option to integrate real-time currency data via an external API.
- **Local Webhook Testing**: Use ngrok to expose the locally running server to the internet for testing with Dialogflow.

## Project Structure

dialogflow-chatbot/

├── app.py                # Webhook version with hardcoded conversion rates

├── app_realtimeAPI.py    # Webhook version using Currency Conversion API for real-time data

├── requirements.txt      # Python dependencies

├── .gitignore            # Files to exclude from version control

├── ngrok.exe             # ngrok executable for local tunneling (Windows)

├── README.md             # Documentation

└── LICENSE               # License file (if applicable)


## Prerequisites
To set up and run this project, you will need:
- A Google account to access Dialogflow.
- Python 3.8+.
- [ngrok](https://ngrok.com/) or a similar tunneling service to expose your local Flask server to the internet.
- An API key for [Currency Conversion API](https://www.currencyconverterapi.com/) (for Version 2).

## Setup and Installation

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/username/dialogflow-chatbot.git
cd dialogflow-chatbot
```

### 2.Install Python Dependencies
Install the required Python libraries by running the following command:

```bash
pip install -r requirements.txt
```

### 3. Set Up Webhook (Flask Example)
You have two options for setting up the webhook. Choose the version you need:

- Option 1: Hardcoded Conversion Rates
Open the app.py file.

Install required dependencies:
```bash
pip install -r requirements.txt
```

Start the Flask server:
```bash
python app.py
```

Use ngrok to expose your local server to the internet. Open a new terminal window and run:
```bash
ngrok http 5000
```

This will provide you with a public URL, such as http://<ngrok_id>.ngrok.io.
Copy the public URL and set it as the webhook URL in Dialogflow:

Go to Dialogflow Console → Fulfillment → Webhook → Enable and paste the URL.

- Option 2: Real-Time API Integration
Open the app_realtimeAPI.py file.
Add your Currency Conversion API key to the designated section in the file:
```python
API_KEY = "your_api_key_here"
```

Install required dependencies:
```bash
pip install -r requirements.txt
```

Start the Flask server:
```bash
python app_realtimeAPI.py
```

Use ngrok to expose your local server to the internet. Open a new terminal window and run:
```bash
ngrok http 5000
```

This will provide you with a public URL, such as http://<ngrok_id>.ngrok.io.
Copy the public URL and set it as the webhook URL in Dialogflow:
Go to Dialogflow Console → Fulfillment → Webhook → Enable and paste the URL.

### 4. Test the Chatbot
Open the Dialogflow Console and interact with the chatbot using the Dialogflow Simulator.
You can also test the chatbot using the embedded web interface (if implemented) or integrate the chatbot into your website.

### 5. Using ngrok
If you're using Windows, you'll be using the ngrok.exe file provided. Make sure it's located in the same folder as your Flask server or provide the full path when running ngrok.

Run ngrok in a terminal like this:

```bash
ngrok http 5000
```
This will generate a public URL that can be used in Dialogflow as the webhook.


License
This project is licensed under the MIT License. See the LICENSE file for details.
