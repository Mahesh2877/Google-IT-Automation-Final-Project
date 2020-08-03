#!/usr/bin/env python3

import sys
import os
import requests
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


#Define the generate_report() function which will build and return the report
def generate_report(attachment, title, paragraph, table_data = None):
    styles = getSampleStyleSheet()
#"attachment" points to the pathname where the report will be built
    report = SimpleDocTemplate(attachment)
#We define the title of the report
    report_title = Paragraph(title, styles["h1"])
#We define the text content that will be written in the report
    report_info = Paragraph(paragraph, styles["BodyText"])
#"table_style" is not used here and can be left out.
#However, we left it here as an exmple of how to define a table in a report
#    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black),
#                   ('FONTNAME', (0, 0), (-1, 0), 1, 'Helvetica-Bold'),
#                   ('ALIGN', (0, 0), (-1, -1), 1, 'CENTER')]
    #report_table = Table(data = table_data, style = table_style, hAlign = "LEFT")
#We define an empty line content. We can add this in the build() wherever
#we want an empty line
    empty_line = Spacer(1, 20)

#The actual report itself is built.
#This will create a file at the pathname defined by the "attachment" variable
#As a result, we need not return the report to the calling function
    report.build([report_title, empty_line, report_info, empty_line])
    print("Report generated: {}\n".format(report))
