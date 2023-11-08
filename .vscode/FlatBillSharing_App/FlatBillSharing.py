import webbrowser
from fpdf import FPDF

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
    
    def pays(self, bill, flatmate2):
        weight = (self.days_in_flat / (self.days_in_flat + flatmate2.days_in_flat))
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Generates a PDF file that contains data about the flatmates, such as
    their names and respective calculated bill for that period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image("/Users/mattgola/Desktop/GitHub/Python Course/files-master/App-2-Flatmates-Bill/files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period and Month labels and values
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=175, h=40, txt=bill.period, border=0, ln=1)


        # Insert name and due amount for the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=175, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount for the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=175, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open('file://' + (self.filename))


bill = Bill(amount = 120, period = "November 2023")
matt = Flatmates(name="Matt", days_in_flat=20)
syd = Flatmates(name='Syd', days_in_flat=25)

print("Matt pays: ", matt.pays(bill=bill, flatmate2=syd))
print("Syd pays: ", syd.pays(bill, flatmate2=matt))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=matt, flatmate2=syd, bill=bill)