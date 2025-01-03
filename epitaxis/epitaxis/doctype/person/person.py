# Copyright (c) 2024, Victor Arocha and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Person(Document):
	def before_save(self):
		self.full_name = f"{self.first_name} {self.father_lastname} {self.mother_lastname}"
		
