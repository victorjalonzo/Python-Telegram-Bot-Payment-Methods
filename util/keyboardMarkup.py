from pyrogram.types import ReplyKeyboardMarkup

class ReplyKeyboardMarkupManager:
    @staticmethod
    def create(
        options: list, 
        row_length: int = 1, 
        is_persistent: bool = None, 
        resize_keyboard: bool = None, 
        one_time_keyboard: bool = None, 
        selective: bool = None, 
        placeholder: str = None,
        addFirstRow: list = None,
        addLastRow: list = None
    ) -> ReplyKeyboardMarkup:
        order = []
        row = []

        for option in options:
            row.append(option.upper())

            if len(row) == row_length:
                order.append(row)
                row = []
                continue
            
            if (option == options[-1]):
                order.append(row)
        
        if addFirstRow is not None:
            order.insert(0, addFirstRow)

        if addLastRow is not None:
            order.append(addLastRow)

        return ReplyKeyboardMarkup(
            keyboard=order, 
            is_persistent=is_persistent, 
            resize_keyboard=resize_keyboard, 
            one_time_keyboard=one_time_keyboard, 
            selective=selective, 
            placeholder=placeholder
        )