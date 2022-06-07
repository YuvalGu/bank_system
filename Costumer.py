class Costumer:
    def __init__(self, id: str, name: str, pin_code: str):
        """
        :param id: costumer id
        :param name: costumer's name
        :param pin_code: the costumer's password
        """
        self.id = id
        self.name = name
        self.password = pin_code

    def __eq__(self, other):
        return self.id == other.id
