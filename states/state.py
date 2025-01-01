from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    name = State()
    phone = State()

class Feedback(StatesGroup):
    feedback = State()
    
    
class NameChange(StatesGroup):
    name = State()
    

class PhoneChange(StatesGroup):
    phone = State()
    
    
class Collobration(StatesGroup):
    name = State()
    phone = State()
    location = State()
    networks = State()
    info = State()
    