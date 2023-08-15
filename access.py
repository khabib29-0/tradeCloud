from py5paisa import FivePaisaClient

req_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjUwNDk1NTE0Iiwicm9sZSI6IlBoa09sQjVTWDNXa0JFazRlNWFuNkFWY1FBN2huSGJqIiwiU3RhdGUiOiIiLCJuYmYiOjE2OTIwMzcxNTIsImV4cCI6MTY5MjAzNzIxMiwiaWF0IjoxNjkyMDM3MTUyfQ.vS5_7R9mQJbgkkDC50Yhewa9yI4pPKTjpwCUunCKdFM'


cred={
    "APP_NAME":"5P50495514",
    "APP_SOURCE":"17013",
    "USER_ID":"YvqxEvcd7Gd",
    "PASSWORD":"WGhBHMIhnB7",
    "USER_KEY":"PhkOlB5SX3WkBEk4e5an6AVcQA7hnHbj",
    "ENCRYPTION_KEY":"cASkwbFwlI0v8rOr6j1li7em0HIVEKt8"
    }


client = FivePaisaClient(cred=cred)
client.get_access_token(req_token)





