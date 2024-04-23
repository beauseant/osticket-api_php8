import requests

url="https://192.168.151.254/osticket/ost_wbs/"
key = "FB0D35801DC2CC92FFD788E667CA7B3B"
verifyCert = False

#auth header:
headers = {"apikey":key}




ticketDataCreate={
    "query":"ticket",
    "condition":"add",
    "parameters":{
    "title":"No funciona nada",
    "subject":"furioso con el mundo",
    "user_id": 2,
    "priority_id":2,
    "status_id":1,
    "dept_id":1,
    "sla_id":1,
    "topic_id":1
    }
}



def createTicket ():

    r = requests.post(url=url,json=ticketDataCreate,headers=headers, verify = verifyCert)

    print('INFO :: Request Status Code: ', r.status_code)

    if (r.status_code < 200 or r.status_code >= 300):
        return False

    print('INFO :: Ticket Number: ', r.json())
    return r.json()['data']


def getTicket (id):


    dataget = {
    "query":"ticket",
    "condition":"specific",
    "parameters":{
        "id":id
        }
    }

    r = requests.get(url=url,json=dataget,headers=headers,  verify=verifyCert)
    response = r
    print('INFO :: Request Status Code: ', r.status_code)

    print (response)
    if (r.status_code < 200 or r.status_code >= 300):
        print (r)
        return False

    print('INFO :: Ticket info: ', r.json())
    return True
	
	
ticketId = createTicket()

getTicket( ticketId )

