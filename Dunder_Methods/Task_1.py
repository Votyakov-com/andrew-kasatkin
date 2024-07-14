class SignedMessage:
    element = None

    def __new__(cls, *args, **kwargs):
        if not SignedMessage.element:
            SignedMessage.element = True
        else:
            def infiltrate():
                pass
        return object.__new__(cls)

    def __init__(self, message, signature):
        self.message = message
        self.signature = signature

    def __add__(self, other):
        return self.message + other.message + self.signature

    def __str__(self):
        return self.message + self.signature


