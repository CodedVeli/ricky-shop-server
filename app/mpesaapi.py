import requests
from .extensions import mpesa_bp
from requests.auth import HTTPBasicAuth
from flask import  request
from datetime import datetime
import json
import base64


consumer_key = "fFhbLAxOBMus8upS0uNUUrRpT6qya9SUrXOwdrjYzeXe4CS0"
consumer_secret = "UQlZ0Vysmk0A1vHoP524QGkQL1N7PUygYTlsSyDPQGOjK2hP3H22mj0fBTszGFdk"
base_url = "http:102.217.157.198/5000"

api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

@mpesa_bp.route('/access_token', methods=['GET'])
def access_token():
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return validated_mpesa_access_token   


@mpesa_bp.route('/register_url', methods=['POST'])
def register_url():
    token = access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % token}
    request = {
        "ShortCode": "600383",
        "ResponseType": "Completed",
        "ConfirmationURL": base_url + "",
        "ValidationURL": ""
    }
    response = requests.post(api_url, json=request, headers=headers)    

    return response.json()

# confirm
# @mpesa_bp.route('/c2b/confirm' , methods=['POST'])
# def confirm():
#     data = request.get_json()
#     # write to file
#     file = open('confirm.json', 'a') 
#     file.write(json.dumps(data))
#     file.close()
#     return {
#         "ResultCode": 0,
#         "ResultDesc": "Accepted"
#     }

# # validate
# @mpesa_bp.route('/c2b/validate' , methods=['POST'])
# def validate():
#     data = request.get_json()
#     # write to file
#     file = open('validate.json', 'a') 
#     file.write(json.dumps(data))
#     file.close()
#     return {
#         "ResultCode": 0,
#         "ThirdPartyTransID": "1234567890",
#         "ResultDesc": "Accepted"
#     }

# # simulate
# @mpesa_bp.route('/simulate', methods=['POST'])
# def simulate():         

    # token = access_token()
    # api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    # headers = {"Authorization": "Bearer %s" % token}
    # request = {
    #     "ShortCode": "600383",
    #     "CommandID": "CustomerPayBillOnline",
    #     "Amount": "100",
    #     "Msisdn": "254700272040",
    #     "BillRefNumber": "TestAPI"
    # }
    # response = requests.post(api_url, json=request, headers=headers)
    # return response.json()


# generate mpesa password

MPESA_PASSKEY = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
MPESA_SHORTCODE = "174379"
# phone_number = "254700272040"
# amount = 1
def generate_mpesa_password():
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    business_short_code = MPESA_SHORTCODE
    passkey = MPESA_PASSKEY
    data_to_encode = business_short_code + passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decoded_password = online_password.decode('utf-8')
    return decoded_password

@mpesa_bp.route('/lipa_na_mpesa', methods=["POST"])
def initiate_stk_push():
    data = request.get_json()
    phone_number = data['phone_number']
    amount = data['amount']
    ac_token = "KGuDFImjWA6pB6XdBPSQVDW44HKu"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {
        'Authorization': 'Bearer %s' % ac_token,
        'Content-Type': 'application/json'
    }

    request_payload = {
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwNDAzMDEwOTMx",
    "Timestamp": "20240403010931",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": amount,
    "PartyA": '254' + str(phone_number),
    "PartyB": 174379,
    "PhoneNumber": '254' + str(phone_number),
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "Ricky's Shop",
    "TransactionDesc": "Payment of items" 
  }

    response = requests.request("POST", api_url, headers=headers, json=request_payload)
    return response.text.encode('utf8')