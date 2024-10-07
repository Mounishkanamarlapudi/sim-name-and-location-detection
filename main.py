import phonenumbers
from test import number  
# Import a phone number (in E.164 format) from the 'test' module

from phonenumbers import geocoder
# Geocoder: Find the geographic location (country/region) for the phone number
ch_number = phonenumbers.parse(number, "CH")  
# Parse the number with a region code
print(geocoder.description_for_number(ch_number, "en"))  
# Display the location in English

from phonenumbers import carrier
# Carrier: Find the carrier (SIM provider) for the phone number
service_number = phonenumbers.parse(number, "RO")  
# Parse the number for carrier lookup
print(carrier.name_for_number(service_number, "en"))  
# Display the carrier name in English
