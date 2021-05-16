import os
import requests
import mailslurp_client

url = "https://api.mailslurp.com/newEmailAddress?allowTeamAccess=false&useDomainPool=false&apikey=4b63d85a1afef87bd2bdfb6d73342376608aa9f24a21cfa5c9d3d9b5f0ea00c5"




def create_inbox_example_Rest_Api():
    headers = {"accept": "application/json"}
    data = {}
    r = requests.post(url,headers,data)
    print (r)
    print(r.status_code, r.reason)



def create_inbox_example_sdk_client():
    configuration = mailslurp_client.Configuration()
    configuration.api_key['x-api-key'] = "4b63d85a1afef87bd2bdfb6d73342376608aa9f24a21cfa5c9d3d9b5f0ea00c5"
    with mailslurp_client.ApiClient(configuration) as api_client:
        # create an inbox using the inbox controller
        api_instance = mailslurp_client.InboxControllerApi(api_client)
        #inbox = api_instance.create_inbox()
        // create an inbox with options
        const inbox = await inboxController.createInbox({
            emailAddress: 'anything@my-verified-domain.com',
        })
        print(inbox)

        # check the id and email_address of the inbox
        assert len(inbox.id) > 0
        assert "mailslurp.com" in inbox.email_address


create_inbox_example_sdk_client()
create_inbox_example_Rest_Api()