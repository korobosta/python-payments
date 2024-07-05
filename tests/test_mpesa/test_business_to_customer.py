import unittest
from mpesa.business_to_customer import BusinessToCustomer
import json
import os

class TestBusinessToCustomer(unittest.TestCase):
	def setUp(self):
		self.test_dir = os.path.dirname(__file__)
		self.b2c_response_test_data = os.path.join(self.test_dir, 'b2c_response_test_data.json')
		self.transaction_query_response_test_data = os.path.join(self.test_dir, 'transaction_query_response_test_data.json')

	def initialize_b2c(self):
		business_to_customer_init=BusinessToCustomer()
		return business_to_customer_init

	def test_business_to_customer(self):
		business_to_customer_init = self.initialize_b2c()
		phone_number = "254713887070"
		amount = 1
		remarks = "Send Money to Customer"
		occasion = "OK"
		feedback=business_to_customer_init.business_to_customer(phone_number,amount, remarks,occasion)
		response_code = feedback.get('ResponseCode',"")
		self.assertEqual(response_code,'0')

	def test_extraction_of_response(self):
		# Ensure the file path is correct
		self.assertTrue(os.path.isfile(self.b2c_response_test_data))
		business_to_customer_init = self.initialize_b2c()
		with open(self.b2c_response_test_data, 'r') as file:
			data = json.load(file)
			file.close()
			feedback=business_to_customer_init.extract_response_details(data)
			print(feedback)

if __name__ == '__main__':
    unittest.main()