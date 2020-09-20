class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean(number)
        self.area_code = self.parse_area_code(self.number)
        self.exchange = self.parse_exchange(self.number)
        self.subscriber_number = self.number[-4:]

    def clean(self, number):
        num_string = ''.join([d for d in number if d.isnumeric()])
        if len(num_string) < 10 or len(num_string) > 11:
            raise ValueError("invalid phone number")
        elif len(num_string) == 10:
            return num_string
        elif len(num_string) == 11 and num_string[0] != '1':
            raise ValueError("invalid phone number")
        else:
            return num_string[1:]

    def parse_area_code(self, number):
        first_digit = number[0] if len(number) == 10 else number[1]
        if first_digit == '0' or first_digit == '1':
            raise ValueError("invalid area code")
        else:
            return number[:3]

    def parse_exchange(self, number):
        exchange = number[3:6] if len(number) == 10 else number[4:7]
        if exchange[0] == '0' or exchange[0] == '1':
            raise ValueError("invalid exchange")
        else:
            return exchange

    def pretty(self):
        return f"({self.area_code}) {self.exchange}-{self.subscriber_number}"
