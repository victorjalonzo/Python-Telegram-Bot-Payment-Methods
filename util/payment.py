from dotenv import load_dotenv
import os
load_dotenv()

class PaymentManager:
    @staticmethod
    def getAvailableMethods():
        methods = {
            "CASHAPP": os.getenv("CASHAPP"),
            "PAYPAL": os.getenv("PAYPAL"),
            "ZELLE": os.getenv("ZELLE"),
            "GOOGLEPAY": os.getenv("GOOGLEPAY"),
            "APPLEPAY": os.getenv("APPLEPAY"),
            "CHIME": os.getenv("CHIME"),
            "VENMO": os.getenv("VENMO"),
            "BITCOIN": os.getenv("BITCOIN"),
            "ETHEREUM": os.getenv("ETHEREUM")
        }

        available_methods = {key:value for (key,value) in methods.items() if len(value) > 0}
        return available_methods