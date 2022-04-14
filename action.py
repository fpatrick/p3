import scraper


class Validate(scraper.Scrapping):
    """
    Get menu choice from user and validate
    :param option: The menu choice, can be a number 1-6
    """
    def __init__(self):
        scraper.Scrapping.__init__(self)
        self.choice = 99
        self.price = 99
        self.url = ""

    def ask_choice(self, limit):
        """
        Convert choice to int, raise exception if wrong option or can't be converted
        :return: True if passes, False if except
        """
        while True:
            try:
                self.choice = int(input(f"1-{limit}: "))
                if self.choice > limit:
                    raise ValueError(
                        f"Please choose a number between 0 and {limit}! You provided {self.choice}"
                    )
                return False
            except ValueError as e:
                print(f"Please choose a number between 0 and {limit}! You provided invalid data: {e}\n")

    def ask_price(self):
        while True:
            try:
                self.price = int(input("Please enter desired price: \n"))
                return False
            except ValueError as e:
                print(f"Invalid data! Please enter only numbers and try again. \n")

    def ask_page(self):
        self.url = input("Please enter the URL: \n")
        try:
            return self.make_soup(self.url)
        except:
            print(f"URL Couldn't be reached! Please verify and try again. \n")
            return False


class User:
    def __init__(self):
        self.amazon_url = ""
        self.amazon_price = 0
        self.argos_url = ""
        self.argos_price = 0
        self.currys_url = ""
        self.currys_price = 0


