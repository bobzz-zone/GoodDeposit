from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Item Code::200","Item Name::200","Description::200","Qty:Float:100"], []
	data = frappe.db.sql("""select d.item_code,d.item_name,d.description,sum(d.qty-d.withdrawed) as "total" 
		from `tabGood Deposit Item` d join `tabGood Deposit` p on d.parent=p.name
		where d.qty>d.withdrawed and p.customer == "{}" group by d.item_code""".format(filters.get("customer")),as_list=1)
	return columns, data