from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Customer::200","Item Code::200","Item Name::200","Description::200","Qty:Float:100"], []
	where = ""
	if filters.get("customer"):
		where = """ and p.customer = "{}" """.format(filters.get("customer"))
	data = frappe.db.sql("""select p.customer,d.item_code,d.item_name,d.description,sum(d.qty-d.withdrawed) as "total" 
		from `tabGood Deposit Item` d join `tabGood Deposit` p on d.parent=p.name
		where d.qty>d.withdrawed {} group by d.item_code""".format(where),as_list=1)
	return columns, data