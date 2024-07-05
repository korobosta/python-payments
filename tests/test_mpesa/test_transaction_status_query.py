import unittest
from mpesa.transaction_query import TransactionQuery
import json
import os

class TestTransactionQuery(unittest.TestCase):
	transaction_status_query=TransactionQuery()

	def setUp(self):
		self.test_dir = os.path.dirname(__file__)
		self.transaction_query_response_test_data = os.path.join(self.test_dir, 'transaction_query_response_test_data.json')

	def test_transaction_status_query(self):
		response_code = None
		transaction_code = "SDM4XOS3YW"
		response=self.transaction_status_query.transaction_query(transaction_code)
		if 'ResponseCode' in response:
			response_code = response["ResponseCode"]
		self.assertEqual(response_code, '0')

	def test_extraction_of_response(self):
		# Ensure the file path is correct
		self.assertTrue(os.path.isfile(self.transaction_query_response_test_data))

		with open(self.transaction_query_response_test_data, 'r') as file:
			data = json.load(file)
			file.close()
			feedback=self.transaction_status_query.extract_response_details(data)
			print(feedback)

if __name__ == '__main__':
	unittest.main()