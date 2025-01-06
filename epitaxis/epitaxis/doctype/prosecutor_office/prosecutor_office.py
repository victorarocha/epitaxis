# Copyright (c) 2025, Victor Arocha and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ProsecutorOffice(Document):
	def before_save(self):
		self.office_name = f"{self.name}"
