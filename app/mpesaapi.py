import requests
import os
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth
from flask import request, jsonify
from .extensions import mpesa_bp
# from models.model import OrderPayments


class MpesaClient:
    def __init__(self):
        self.consumer_key = os.getenv('MPESA_CONSUMER_KEY')
        self.consumer_secret = os.getenv('MPESA_CONSUMER_SECRET')
        self.shortcode = os.getenv('MPESA_SHORTCODE')
        self.passkey = os.getenv('MPESA_PASSKEY')
        self.party_a = os.getenv('MPESA_PARTY_A')

    def get_access_token(self):
        api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        try:
            response = requests.get(api_url, auth=HTTPBasicAuth(
                self.consumer_key, self.consumer_secret))
            response.raise_for_status()
            return response.json()['access_token']
        except requests.exceptions.RequestException as e:
            print(f"Error getting access token: {e}")
            return None

    def generate_password(self):
        lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
        data_to_encode = self.shortcode + self.passkey + lipa_time
        return base64.b64encode(data_to_encode.encode()).decode('utf-8')

    def validate_phone_number(self, phone_number: str) -> str:
        # so that one can input 07593911XX or +2547593911XX
        # and it will be converted to 2547593911XX
        # This ensures that the phone number is in the format 254XXXXXXXXX
        # But the 254 becomes a problem if you have users from different countries
        # like +256
        if phone_number is None:
            return None

        if phone_number.startswith("+"):
            phone_number = phone_number[1:]
        if phone_number.startswith("0"):
            phone_number = "254" + phone_number[1:]
        return phone_number

    def validate_amount(self, amount: float) -> float:
        return max(amount, 0)

    def initiate_stk_push(self, phone_number, amount):
        phone_number = self.validate_phone_number(phone_number)
        amount = self.validate_amount(amount)

        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        access_token = self.get_access_token()

        if not access_token:
            return "Failed to get access token."

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        request_payload = {
            "BusinessShortCode": self.shortcode,
            "Password": self.generate_password(),
            "Timestamp": datetime.now().strftime('%Y%m%d%H%M%S'),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": self.party_a,
            "PartyB": self.shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": "https://ricky-shop-server-3.onrender.com/mpesa/callback",  # change the live URL
            "AccountReference": "12345678",
            "TransactionDesc": "Pay For goods in rick shop"
        }

        response = requests.post(
            api_url, json=request_payload, headers=headers)

        if response.status_code == 200:
            print(response.json())
            return True
        else:
            print(response.json())
            raise Exception(response.json())


@mpesa_bp.route('/lipa_na_mpesa', methods=['POST'])
def initiate_stk_push():
    data = request.get_json()
    print(f"Data: {data}")
    if not data:
        return jsonify({"error": "No data provided"}), 400

    phone_number = data.get('phone_number')
    amount = data.get('amount')

    if not phone_number or not amount:
        return jsonify({"error": "Phone number or amount missing"}), 400

    mpesa_client = MpesaClient()

    phone_number = mpesa_client.validate_phone_number(phone_number)
    amount = mpesa_client.validate_amount(amount)

    if phone_number is None or amount is None:
        return jsonify({"error": "Invalid phone number or amount"}), 400

    try:
        mpesa_client.initiate_stk_push(phone_number, amount)
        return jsonify({"message": "STK push initiated"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@mpesa_bp.route('/callback', methods=['POST'])
def handle_callback():
    callback_data = request.json

    # Check the result code
    result_code = callback_data['Body']['stkCallback']['ResultCode']
    if result_code != 0:
        # If the result code is not 0, there was an error
        error_message = callback_data['Body']['stkCallback']['ResultDesc']
        response_data = {'ResultCode': result_code, 'ResultDesc': error_message}
        return jsonify(response_data)

    # If the result code is 0, the transaction was completed
    callback_metadata = callback_data['Body']['stkCallback']['CallbackMetadata']
    amount = None
    phone_number = None
    for item in callback_metadata['Item']:
        if item['Name'] == 'Amount':
            amount = item['Value']
        elif item['Name'] == 'PhoneNumber':
            phone_number = item['Value']

    # Save the variables to a file or database, etc.
    # ...

    # Return a success response to the M-Pesa server
    response_data = {'ResultCode': result_code, 'ResultDesc': 'Success'}
    print(response_data)
    return jsonify(response_data)