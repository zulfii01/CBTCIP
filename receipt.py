from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def create_receipt(customer_name, items, tot_amount, receipt_number):
    file_name = f"recept_{receipt_number}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    #company details
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2, height-50, "Cipher Byte")
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, height-70, "Kolkata")
    c.drawCentredString(width/2, height-85, "Mail: cipherbytetechnologies@gmail.com")

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height-125, "PAYMENT RECEIPT")

    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, height - 140, f"Receipt number: {receipt_number}")
    c.drawCentredString(width/2, height - 155, f"Date: {datetime.now().strftime('%Y, %m, %d  %H:%M:%S')}" )
    c.drawCentredString(width/2, height - 170, f"Customer Name: {customer_name}")

    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - 210, "ITEMS")
    c.setFont("Helvetica", 12)
    item_y = height - 225
    for item, price in items.items():
        c.drawCentredString(width/2, item_y, f"{item}: Rs.{price:.2f}/-")
        item_y -= 15

    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, item_y - 20, f"Total Amount: Rs.{tot_amount:.2f}/-")

    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(width/2, height - 350, "Thankyou for your purchase! :)")

    #saving the pdf
    c.save()
    print(f"Receipt saved as {file_name}")


# example usage
customer_name = "MOHD ZULFEKAR"
items = {
    "Driving gloves": 200,
    "Soda": 30.5,
    "Ice-cream": 69.5
}
tot_amount = sum(items.values())
receipt_no = 1001

create_receipt(customer_name, items, tot_amount, receipt_no)