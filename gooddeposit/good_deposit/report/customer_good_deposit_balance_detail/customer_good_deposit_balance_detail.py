# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Good Deposit:Link/Good Deposit:200","Customer::200","Sales:Data:100","Item Code::200","Item Name::200","Qty:Float:100","Rate:Currency:200","Amount:Currency:200","Delivery Date:Link/Delivery Note:100","Delivery Note:Link/Delivery Note:100","Description::200"], []
	where = ""
	if filters.get("customer"):
		where = """ and p.customer = "{}" """.format(filters.get("customer"))
	data = frappe.db.sql("""select p.name,p.customer,p.sales,d.item_code,d.item_name,(d.qty-d.withdrawed) as "sisa",d.rate,((d.qty-d.withdrawed)*d.rate) as "amount" ,dn.posting_date,p.delivery_note,d.description
		from `tabGood Deposit Item` d join `tabGood Deposit` p on d.parent=p.name
		left join `tabDelivery Note` dn on dn.name=p.delivery_note
		where d.qty>d.withdrawed {} """.format(where),as_list=1)
	return columns, data
