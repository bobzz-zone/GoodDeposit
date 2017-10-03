// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Customer Good Deposit Balance Detail"] = {
	"filters": [
		{
			"fieldname":"customer",
			"label": __("Customer"),
			"fieldtype": "Link",
			"options": "Customer",
			"reqd":1
		}
	]
}
