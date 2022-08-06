#!/usr/bin/env python3

#generate a PDF file to send to the supplier, indicating that the data was correctly processed. To generate PDF reports, you can use the ReportLab library. 


# The content of the report should look like this:

# Processed Update on <Today's date>

# [blank line]

# name: Apple

# weight: 500 lbs

# [blank line]

# name: Avocado

# weight: 200 lbs

# [blank line]

#Using the reportlab Python library, define the method generate_report to build the PDF reports. We have already covered how to generate PDF reports in an earlier lesson; you will want to use similar concepts to create a PDF report named processed.pdf.

import reportlab
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    print(paragraph, "paragraph")
    report_info = Paragraph(title, styles["BodyText"])
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                  ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                  ('ALIGN', (0,0), (-1,-1), 'CENTER')]
    # table_data = [[report_title], paragraph]
    report_table = Table(data=paragraph, style=table_style, hAlign="LEFT")
    
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info, empty_line, report_table])

    # styles = getSampleStyleSheet()
    # report = SimpleDocTemplate(filename)
    # report_title = Paragraph(title, styles["h1"])
    # report_info = Paragraph(additional_info, styles["BodyText"])
    # table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
    #                 ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    #                 ('ALIGN', (0,0), (-1,-1), 'CENTER')]
    # report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    # empty_line = Spacer(1,20)
    # report.build([report_title, empty_line, report_info, empty_line, report_table])
    



# if __name__ == "__main__":
