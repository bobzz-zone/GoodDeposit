# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class GoodWithdraw(Document):
	def on_submit(self):
		deposit=""
		for item in self.items:
			if item.deposit_item == "":
				frappe.throw("Goods Withdrawal should be from Good Deposit")
			else:
				data = frappe.db.sql("""select qty-withdrawed from `tabGood Deposit Item` where name="{}" """.format(item.deposit_item),as_list=1)
				qty=0
				for x in data:
					qty=x[0]
				if qty<item.qty:
					frappe.throw("Items {} is deposited only {} so cant be withdrawed {}".format(item.item_code,qty,item.qty))
			if item.deposit not in deposit:
				if deposit=="":
					deposit = """ "{}" """.format(item.deposit)
				else:
					deposit = """{},"{}" """.format(deposit,item.deposit)
		for item in self.items:
			frappe.db.sql("""update `tabGood Deposit Item` set withdrawed=withdrawed+{} where name="{}" """.format(item.qty,item.deposit_item),as_list=1)
		lists=frappe.db.sql("""select parent from `tabGood Deposit Item` where parent in ({}) and qty=withdrawed """.format(deposit),as_list=1)
		deposit=""
		for dep in lists:
			if dep[0] not in deposit:
				if deposit=="":
					deposit = """ "{}" """.format(dep[0])
				else:
					deposit = """{},"{}" """.format(deposit,dep[0])
		frappe.db.sql("""update `tabGood Deposit` set status="Withdrawed" where name IN ({}) """.format(deposit),as_list=1)
	def on_cancel(self):
		deposit=""
		for item in self.items:
			if item.deposit not in deposit:
				if deposit=="":
					deposit = """ "{}" """.format(item.deposit)
				else:
					deposit = """{},"{}" """.format(deposit,item.deposit)
		for item in self.items:
			frappe.db.sql("""update `tabGood Deposit Item` set withdrawed=withdrawed-{} where name="{}" """.format(item.qty,item.deposit_item),as_list=1)
		frappe.db.sql("""update `tabGood Deposit` set status="Deposited" where name IN ({}) """.format(deposit),as_list=1)
