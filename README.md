# stock-news
A Python app that monitors daily stock price changes, fetches related news for significant moves, and sends WhatsApp alerts through Twilio.

## Installation

Activate your virtual environment, then install the project dependencies from the repository root:
```powershell
python -m pip install -r requirements.txt
```

## Configuration

1. Copy the example environment file and add your API credentials:
```powershell
powershell
Copy-Item .env_example .env
notepad .env
```

2. Replace the placeholder values in `.env` with your Alpha Vantage, NewsAPI, and Twilio credentials. Keep `.env` private—do not commit it to Git.

3. To send WhatsApp messages, configure the Twilio WhatsApp Sandbox in your Twilio Console. Set `TWILIO_WHATSAPP_FROM` to the sandbox sender and `TWILIO_WHATSAPP_TO` to your WhatsApp number, using the `whatsapp:+...` format. Join the sandbox from your recipient number by following Twilio’s instructions.

The app loads credentials from `.env` when it runs. Make sure your API keys and Twilio settings are valid before starting it.