// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Good Withdraw', {
	refresh: function(frm) {
		if (this.frm.doc.docstatus===0) {
				cur_frm.add_custom_button(__('Sales Order'),
					function() {
						erpnext.utils.map_current_doc({
							method: "erpnext.selling.doctype.sales_order.sales_order.make_delivery_note",
							source_doctype: "Sales Order",
							get_query_filters: {
								docstatus: 1,
								status: ["!=", "Closed"],
								per_delivered: ["<", 99.99],
								project: cur_frm.doc.project || undefined,
								customer: cur_frm.doc.customer || undefined,
								company: cur_frm.doc.company
							}
						})
					}, __("Get items from"));
			}
	}
});
