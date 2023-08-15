from py5paisa import FivePaisaClient

totp = 598950
cred={
    "APP_NAME":"5P50495514",
    "APP_SOURCE":"17013",
    "USER_ID":"YvqxEvcd7Gd",
    "PASSWORD":"WGhBHMIhnB7",
    "USER_KEY":"PhkOlB5SX3WkBEk4e5an6AVcQA7hnHbj",
    "ENCRYPTION_KEY":"cASkwbFwlI0v8rOr6j1li7em0HIVEKt8"
    }


######### get request token 
client = FivePaisaClient(cred=cred)
request_token = client.get_totp_session('9046232854',str(totp),'336699')

#print(request_token.RequestToken )


######### get access token 

#access_token = client.get_access_token(str(request_token) ) 
#print(access_token)

#Now Can directly call client.place_order()
