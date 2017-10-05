# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Date:Date:150","Customer::200","Good Deposit:Link/Good Deposit:200","Sales:Data:100","Delivery Note:Link/Delivery Note:100","Item Code::200","Item Name::200","Description::200","Qty:Float:100","Rate:Currency:200"], []
	where = ""
	if filters.get("customer"):
		where = """ and p.customer = "{}" """.format(filters.get("customer"))
	data = frappe.db.sql("""select p.customer,p.name,p.sales,p.delivery_note,d.item_code,d.item_name,d.description,(d.qty-d.withdrawed) as "sisa",d.rate 
		from `tabGood Deposit Item` d join `tabGood Deposit` p on d.parent=p.name
		where d.qty>d.withdrawed {} """.format(where),as_list=1)
	return columns, data
