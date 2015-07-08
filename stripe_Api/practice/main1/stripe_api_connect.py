import requests


api_endpoint='https://api.stripe.com'
api_secret_key='sk_test_xxxxxxxxxxx' #enter your details here
api_pub_key='pk_test_xxxxxxxxxxxxxxxxxxxxxxxxx' #enter your details here

def create_customer():
	endpoint="/v1/customers"
	user=api_secret_key
	description="some description for customer"
	email="abhijit.bangera@gmail.com"
	final_api_endpoint=api_endpoint+endpoint
	rmethod="post"
	# print(user, description,final_api_endpoint)
	auth=(user, "")
	params={
		"email":email
	}
	r=requests.post(final_api_endpoint,auth=auth,params=params)
	# print(r.status_code)
	# print(r.text)
	# print(r.json())
	return r.json
new_customer=create_customer()

def update_customer_description(cust_id,description):
	new_endpoint=api_endpoint+"/v1/customers/"+cust_id
	auth={user,""}
	params={
		"description":description
	}
	r=requests.post(new_endpoint,auth=auth,params=params)
	return r.json()
updated_c=update_customer_description(new_customer["id"],"here is a new desc")
