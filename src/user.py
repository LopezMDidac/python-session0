class User:
    name: str
    age: int
    is_avenger: bool

    def __init__(self, name: str, age: int, is_avenger: bool):
        self.name = name
        self.age = age
        self.is_avenger = is_avenger

    def greeting_message(self) -> str:
        message = f"hello {self.name} with {self.age} years old"
        if self.is_avenger:
            message += "Glad to see you again. Welcome to the Stark tower"
        else:
            message += "Please follow to the guest area"

        return message
