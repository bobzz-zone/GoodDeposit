# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import frappe.utils
from frappe.utils import  flt
from frappe.model.mapper import get_mapped_doc
class GoodDeposit(Document):
	pass
	def on_cancel(self):
		for item in self.items:
			if item.withdrawed>0:
				frappe.throw("Item Already Withdrawed so it cant be cancelled")
@frappe.whitelist()
def make_withdrawal(source_name, target_doc=None):
	def set_missing_values(source, target):
		pass

	def update_item(source, target, source_parent):
		target.qty = flt(source.qty) - flt(source.withdrawed)

	target_doc = get_mapped_doc("Good Deposit", source_name, {
		"Good Deposit": {
			"doctype": "Good Withdraw",
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"field_map": {
			"name": "gd"
		},
		"Good Deposit Item": {
			"doctype": "Good Withdraw Item",
			"field_map": {
				"name": "good_deposit_item",
				"parent": "good_deposit"
			},
			"postprocess": update_item,
			"condition": lambda doc: abs(doc.withdrawed) < abs(doc.qty)
		}
	}, target_doc, set_missing_values)

	return target_doc
@frappe.whitelist()
def make_deposit(source_name, target_doc=None):
	def set_missing_values(source, target):
		pass

	def update_item(source, target, source_parent):
		pass
	
	target_doc = get_mapped_doc("Delivery Note", source_name, {
		"Delivery Note": {
			"doctype": "Good Deposit",
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"field_map":{
			"delivery_note":"name"
		},
		"Delivery Note Item": {
			"doctype": "Good Deposit Item"
		}
	}, target_doc, set_missing_values)

	return target_doc
