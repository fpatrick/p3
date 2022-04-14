class Validate:
    """
    Get menu choice from user and validate
    :param option: The menu choice, can be a number 1-6
    """
    def __init__(self):
        self.choice = 0
        self.number = 0

    def ask_choice(self):
        """
        Convert choice to int, raise exception if wrong option or can't be converted
        :return: True if passes, False if except
        """
        while True:
            try:
                self.choice = int(input("1-2: "))
                if int(self.choice) > 6:
                    raise ValueError(
                        f"Please choose a number between 0 and 6! You provided {self.choice}"
                    )
                return False
            except ValueError as e:
                print(f"Please choose a number between 0 and 6! You provided invalid data: {e}\n")

    def ask_price(self):
        while True:
            try:
                self.number = int(input("Please enter desired price: \n"))
                return False
            except ValueError as e:
                print(f"Invalid data! Please enter only numbers and try again. \n")



class User:
    def __init__(self):
        self.amazon_url = ""
        self.amazon_price = 0
        self.argos_url = ""
        self.argos_price = 0
        self.currys_url = ""
        self.currys_price = 0

