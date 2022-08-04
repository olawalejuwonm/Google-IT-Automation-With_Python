#!/usr/bin/env python3

import email
import report
from email import message
import json
import locale
import sys


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
    #json example:
    # {
    #     "id": 47,
    #     "car": {
    #             "car_make": "Lamborghini",
    #             "car_model": "Murciélago",
    #             "car_year": 2002
    #     },
    #     "price": "$13724.05",
    #     "total_sales": 149
    # }
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  max_year = {"car_year": 0}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > max_sales["total_sales"]:
        max_sales = item
    # TODO: also handle most popular car_year
    if item["car"]["car_year"] > max_year["car_year"]:
        max_year = item["car"]
        # save total_sales to max_year
        max_year["total_sales"] = item["total_sales"]

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
  ]
  #appending a formatted string to the summary list in the below format: "The {car model} had the most sales: {total sales}"
  summary.append("The {} had the most sales: {}".format(
        format_car(max_sales["car"]), max_sales["total_sales"]))
  summary.append("The most popular year was {} with {} sales.".format(
        max_year["car_year"], max_year["total_sales"]))
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)
  # TODO: turn this into a PDF report
  #Use the reports.generate() function within the main function
  report.generate("/tmp/cars.pdf", "Sales Report", "This is a report of car sales.", cars_dict_to_table(data)) 

  # TODO: send the PDF report as an email attachment
  #Once the PDF is generated, you need to send the email, using the emails.generate() and emails.send() methods.
  # Use the following details to pass the parameters to emails.generate()
  #Use the following details to pass the parameters to emails.generate():
    # From: automation@example.com
    # To: <user>@example.com
    # Subject line: Sales summary for last month
    # E-mail Body: The same summary from the PDF, but using \n between the lines
    # Attachment: Attach the PDF path i.e. generated in the previous step
  message = email.generate("automation@example.com", "juwon@example.com", "Sales summary for last month", "\n".join(summary), "/tmp/cars.pdf")
  email.send(message)



if __name__ == "__main__":
  main(sys.argv)