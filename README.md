# Python-Telegram-Bot-Payment-Methods

This is a Python-based Telegram bot that handles casual payments. The bot allows users to purchase services, view available payment methods, get support, and preview content.

## Features

* Display main menu with options
* Show available payment methods
* Send details of the selected payment method
* Provide support contact
* Send preview video

## Installation

### 1. Clone this repository:

```bash
git clone https://github.com/victorjalonzo/Python-Telegram-Bot-Payment-Methods.git
cd telegram-payment-bot
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Create a .env file in the project's root directory with the following content:

```bash

SESSION_NAME="botsession"

#Replace it with your Telegram application credentials
API_ID="YOUR_API_ID"
API_HASH="YOUR_API_HASH"

#Replace it with your Bot token
BOT_TOKEN="YOUR_BOT_TOKEN"

#Replace it with your Telegram profile link
PROFILE_LINK="YOUR_PROFILE_LINK"

#The price of your service or product
PRICE="YOUR_PRICE YOUR_CURRENCY"

#Replace it with your payment method. If you're not using one of them, remove it. 
PRICE="YOUR_PRICE"
CASHAPP="YOUR_CASHAPP"
PAYPAL="YOUR_PAYPAL"
ZELLE="YOUR_ZELLE"
GOOGLEPAY="YOUR_GOOGLEPAY"
APPLEPAY="YOUR_APPLEPAY"
CHIME="YOUR_CHIME"
VENMO="YOUR_VENMO"
BITCOIN="YOUR_BITCOIN"
ETHEREUM="YOUR_ETHEREUM"
```
Replace the placeholders with your corresponding information.

### 4. Create a folder with the name "preview" and insert a video in the folder with the name "preview.mp4" it should looks like this:
```bash
├── main.py
├── preview
│   └── preview.mp4
```

## Usage

To start the bot, run the following command:
```bash
python main.py
```

## Contributions

Contributions are welcome. If you'd like to contribute, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

