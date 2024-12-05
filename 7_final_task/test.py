import requests
import ipinfo

access_token = '0b0603455815e7'

handler = ipinfo.getHandler(access_token)
ip_address = '79.174.184.253'
details = handler.getDetails(ip_address)

print(details.loc)


# print(requests.get("http://ip-api.com/json/").json())

