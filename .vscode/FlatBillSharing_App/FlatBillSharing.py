class Bill:
    """
    Object that contains data about a bill, such as total
    amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmates:
    """
    Object that contains data about the flatmates, such as
    the name of roomate, number of days in flat in a month,
    and, how much they pay based on given attributes.
    """  

    def __init__(self, name, days_in_flat):
        self.name = name
        self.days_in_flat = days_in_flat
    
    def pays(self, bill):
        return bill.amount / 2


class PdfReport:
    """
    Generates a PDF file that contains data about the flatmates, such as
    their names and respective calculated bill for that period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


bill = Bill(amount = 120, period = "November 2023")
matt = Flatmates(name="Matt", days_in_flat=20)
syd = Flatmates(name='Syd', days_in_flat=25)

print(matt.pays(bill=bill))