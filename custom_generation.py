from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import lightgrey, black
from reportlab.pdfgen import canvas


customer = {
    "company_name": "customer AB",
    "street_address": "street 11",
    "postal_address": "26868 Röstånga",
    "customer_reference": "John doe",
    "recipient_email": "some@gmail.com",
    "customer_number": "10"
}

# setting monthly variables for invoice printing
createDate = "2023-10-23"
dueDate = "2023-11-15"
OCRBase = createDate.replace("-", "")


costs = [
    {'description': 'Kostnad för arbete', 'value': 3740},
    # ... you can add more items
]

VAT = int(costs[0]['value']*0.25)
totalIncVAT = int(costs[0]['value']+VAT)

# Calculate the total
total_cost = sum(item['value'] for item in costs)


# Set the OCR
OCR = OCRBase+customer["customer_number"]

# Create PDF
c = canvas.Canvas(f"Faktura_{customer['company_name']}_{OCR}.pdf", pagesize=letter)
width, height = letter

# Set PDF title
c.setTitle(f"Faktura {OCR} till {customer['company_name']}")


# Set fill color to light grey
c.setFillColor(lightgrey)

# Draw a rectangle. Parameters are: x, y, width, height
c.rect(270, height-115, 270, 100, fill=1)
c.setFillColor(black)  # change fill color to black for text


currentHeight=40
c.setFont("Helvetica-Bold", 14)
c.drawString(300, height-currentHeight, "FAKTURA")
currentHeight+=15
c.setFont("Helvetica-Bold", 12)
c.drawString(300, height-currentHeight, "Förfallodatum:")
c.drawString(450, height-currentHeight, dueDate)
currentHeight+=15
c.drawString(300, height-currentHeight, "Summa att betala:")
c.drawString(450, height-currentHeight, str(totalIncVAT)+" kr")
currentHeight+=15
c.drawString(300, height-currentHeight, "OCR-nummer:")
c.drawString(450, height-currentHeight, OCR)
currentHeight+=15
c.drawString(300, height-currentHeight, "Bankgiro:")
c.drawString(450, height-currentHeight, "5517-9477")




#Add logo - Note: Replace 'your_logo.jpg' with your actual logo file
c.drawInlineImage("./shiitakelogo.jpg", 40, height-100, width=100, height=60)

currentHeight+=80
# Add customer info
c.setFont("Helvetica-Bold", 12)
c.drawString(50, height-currentHeight, "Growhub Ekonomisk Förening:")
c.setFont("Helvetica", 12)
c.drawString(350, height-currentHeight, "Faktura till:")

currentHeight+=15
c.drawString(50, height-currentHeight, "Viktor Zaunders")
c.drawString(350, height-currentHeight, customer['company_name'])

currentHeight+=15
c.drawString(50, height-currentHeight, "viktor@mycogreens.se")
c.drawString(350, height-currentHeight, customer['street_address'])

currentHeight+=15
c.drawString(50, height-currentHeight, "0733-907011")
c.drawString(350, height-currentHeight, customer['postal_address'])


currentHeight+=30
# Draw a line
c.line(50, height-currentHeight, width-50, height-currentHeight)

currentHeight+=30
c.drawString(50, height-currentHeight, "Fakturanummer/OCR: "+OCR)
c.drawString(350, height-currentHeight, "Fakturadatum: "+createDate)

currentHeight+=15
c.drawString(50, height-currentHeight, "Kundreferens: "+customer['customer_reference'])
c.drawString(350, height-currentHeight, "Förfallodatum: "+dueDate)

currentHeight+=15
c.drawString(50, height-currentHeight, "Mottagare epost: "+customer['recipient_email'])
c.drawString(350, height-currentHeight, "Dröjesmålsränta: 15%")

currentHeight+=15


currentHeight+=60
# Add cost item description
c.setFont("Helvetica-Bold", 12)
c.drawString(50, height-currentHeight, "Beskrivning")
c.drawString(350, height-currentHeight, "Kostnad")
currentHeight+=10
# Draw a line
c.line(50, height-currentHeight, width-50, height-currentHeight)

currentHeight+=15
# Add item description and cost
c.setFont("Helvetica", 12)
c.drawString(50, height-currentHeight, costs[0]['description'])
c.drawString(350, height-currentHeight, str(costs[0]['value'])+" kr")

currentHeight+=15
c.drawString(50, height-currentHeight, "Moms (25%)")
c.drawString(350, height-currentHeight, str(VAT)+" kr")

currentHeight+=10
# Draw a line
c.line(50, height-currentHeight, width-50, height-currentHeight)

currentHeight+=15
c.setFont("Helvetica-Bold", 12)
c.drawString(50, height-currentHeight, "Totalt:")
c.drawString(350, height-currentHeight, str(totalIncVAT)+" kr")

c.setFont("Helvetica", 12)
    # Draw a line
c.line(50, height-680, width-50, height-680)
c.drawString(50, height-695, "Growhub Ekonomisk Förening")
c.setFont("Helvetica-Bold", 12)
c.drawString(350, height-695, "OCR-nummer: "+OCR)
c.setFont("Helvetica", 12)

c.drawString(50, height-710, "Per Gummessons väg 5")
c.setFont("Helvetica-Bold", 12)
c.drawString(350, height-710, "Bankgiro: 5517-9477")
c.setFont("Helvetica", 12)

c.drawString(50, height-725, "268 68 Röstånga")
c.drawString(350, height-725, "Godkänd för F-skatt")

c.drawString(50, height-740, "Org.nr 7696388193")
c.drawString(350, height-740, "VAT-nr SE769638819301")

print("Faktura: "+customer['company_name']+" skapad! med OCR "+OCR)

# Save PDF
c.save()

