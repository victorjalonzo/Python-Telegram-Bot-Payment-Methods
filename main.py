from pyrogram import Client, idle, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from util.keyboardMarkup import ReplyKeyboardMarkupManager
from util.Asset import Asset
from util.payment import PaymentManager
from dotenv import load_dotenv
import os

load_dotenv()

SESSION_NAME = os.getenv("SESSION_NAME")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
PRICE = os.getenv("PRICE")
PROFILE_LINK = os.getenv("PROFILE_LINK")
PAYMENT_METHODS = PaymentManager.getAvailableMethods()

asset = Asset('assets/')


class Bot(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.command = {
            "menu": ['menu', '/menu', 'back', '/back'],
            "buy": ['buy', '/buy'],
            "payment": list(PAYMENT_METHODS.keys()),
            "preview": ['preview', '/preview'],
            "support": ['support', '/support']
        }
    
    def start(self):
        super().start()
        self.loop.run_until_complete(self.ready_message())
    
    async def ready_message(self):
        user = await self.get_me()
        print(f"I'm logged as {user.username} ({user.id})")

    async def handle (self, client: Client, message: Message):
        content = message.text.lower()

        if content in self.command["menu"]:
            return await self.show_menu(client, message)

        if content in self.command["buy"]:
            return await self.show_available_payment_methods(client, message)
        
        if content.upper() in self.command["payment"]:
            return await self.send_payment_method(client, message)

        elif content in self.command["preview"]:
            return await self.send_preview(client, message)

        elif content in self.command["support"]:
            return await self.send_support(client, message)
        else:
            return await self.show_menu(client, message)
        
    async def show_menu(self, client: Client, message: Message):
        """Shows the main menu"""

        reply = "Choose an option from the menu."

        options = ["BUY", "PREVIEW", "SUPPORT"]
        reply_markup = ReplyKeyboardMarkupManager.create(options, row_length=1)

        return await client.send_message(chat_id=message.chat.id, text=reply, reply_markup=reply_markup)
    
    async def show_available_payment_methods(self, client: Client, message: Message):
        """Shows the available payment methods"""

        reply = "What payment method do you want to use?"

        methodsList = list(PAYMENT_METHODS.keys())
        reply_keyboard = ReplyKeyboardMarkupManager.create(options=methodsList, row_length=3, addLastRow=["BACK"])

        return await client.send_message(chat_id=message.chat.id, text=reply, reply_markup=reply_keyboard)
    
    async def send_payment_method(self, client: Client, message: Message):
        """Sends a payment method image with button-url to send invoice to support"""

        methodKey = message.text
        methodValue = PAYMENT_METHODS[methodKey]

        caption = ""

        if methodValue.startswith("http"):
            caption = f"{methodKey}: {methodValue}\n"
        else:
            caption = f"{methodKey}: `{methodValue}`\n"
        
        caption += f"PRICE: {PRICE}\n\n"

        caption += "After make the payment, please send the invoice to the support to confirm your payment."

        reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton(text="SEND INVOICE", url=PROFILE_LINK)
        ]])

        image = asset.getByShortName(methodKey.lower())
        return await client.send_photo(chat_id=message.chat.id, photo=image, caption=caption, reply_markup=reply_markup)
    
    async def send_support(self, client: Client, message: Message):
        """Sends an image with button-url to contact support"""

        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="CONTACT SUPPORT", url=PROFILE_LINK)]
        ])
        image = asset.getByShortName('support')
        return await client.send_photo(chat_id=message.chat.id, photo=image, reply_markup=reply_markup)

    async def send_preview(self, client: Client, message: Message):
        """Sends a preview video"""

        reply = "Wait a minute, I;m sending you the preview..."
        await client.send_message(chat_id=message.chat.id, text=reply)

        return await client.send_video(chat_id=message.chat.id, video="preview/preview.mp4")

app = Bot(name=SESSION_NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.text)
async def on_message_arrive_handler(client, message):
    return await app.handle(client=client, message=message)

app.start()
idle()
