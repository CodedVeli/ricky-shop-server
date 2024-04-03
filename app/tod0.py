# from validate_email_address import validate_email


# from email_validator import validate_email, EmailNotValidError

# def check(email):
# 	try:
# 	# validate and get info
# 		v = validate_email(email) 
# 		# replace with normalized form
# 		email = v["email"] 
# 		print("True")
# 	except EmailNotValidError as e:
# 		# email is not valid, exception message is human-readable
# 		print(str(e))

# check("ericgithaiga007@gmail.com")

# check("ankitrai326.com")



# def is_valid_email(email):
#     is_valid = validate_email(email, verify=True)
#     return is_valid

# print(is_valid_email("ericgithaiga007@gmail.com"))

# Full docs on GitHub - https://github.com/kickboxio/kickbox-python
# import kickbox

# def is_email_address_valid(email, api_key):
# 	# Initialize Kickbox client with your API key.
# 	client = kickbox.Client(api_key)
# 	kbx = client.kickbox()

# 	# Send the email for verification.
# 	response = kbx.verify(email)

# 	# check the response code if you like
# 	# assert response.code == 200, "kickbox api bad response code"
# 	# We can exclude emails that are undeliverable
# 	return response.body['result'] != "undeliverable"


from email_validator import validate_email, EmailNotValidError

email = "ericgithaiga007@gmail.com"

try:

  # Check that the email address is valid. Turn on check_deliverability
  # for first-time validations like on account creation pages (but not
  # login pages).
  emailinfo = validate_email(email, check_deliverability=False)

  # After this point, use only the normalized form of the email address,
  # especially before going to a database query.
  email = emailinfo.normalized

except EmailNotValidError as e:

  # The exception message is human-readable explanation of why it's
  # not a valid (or deliverable) email address.
  print(str(e))
