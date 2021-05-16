import os
import requests
import mailslurp_client

#url = "https://api.mailslurp.com/newEmailAddress?allowTeamAccess=false&useDomainPool=false&apikey=4b63d85a1afef87bd2bdfb6d73342376608aa9f24a21cfa5c9d3d9b5f0ea00c5"


def create_email_and_inbox_Rest_Api():
    url = "https://api.mailslurp.com/newEmailAddress?allowTeamAccess=false&useDomainPool=false"
    headers = {"accept": "application/json","x-api-key":"4b63d85a1afef87bd2bdfb6d73342376608aa9f24a21cfa5c9d3d9b5f0ea00c5"}
    data = {}
    r = requests.post(url,headers,data)
    if (r.status_code == 201):
        emailaddress = r["emailAddress"]
        print(r.status_code, r.reason,+emailaddress)

    else:
        url = "https://api.mailslurp.com/newEmailAddress?allowTeamAccess=false&useDomainPool=false&apikey=4b63d85a1afef87bd2bdfb6d73342376608aa9f24a21cfa5c9d3d9b5f0ea00c5"
        headers = {"accept": "application/json"}
        data = {}
        r = requests.post(url,headers,data)
        if (r.status_code == 201):
            emailaddress = r["emailAddress"]
            print(r.status_code, r.reason,+emailaddress)

create_email_and_inbox_Rest_Api()