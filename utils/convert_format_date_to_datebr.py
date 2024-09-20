from datetime import datetime

def convert_format_date_to_datebr(date_string):
    # Convert the string to a datetime object
    date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

    formatted_date = date_object.strftime('%d/%m/%Y')

    return formatted_date
