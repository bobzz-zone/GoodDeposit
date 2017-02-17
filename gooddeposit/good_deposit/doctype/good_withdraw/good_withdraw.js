// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Good Withdraw', {
	refresh: function(frm) {
		if (frm.doc.docstatus===0) {
				cur_frm.add_custom_button(__('Good Deposit'),
					function() {
						erpnext.utils.map_current_doc({
							method: "gooddeposit.gooddeposit.doctype.gooddeposit.gooddeposit.make_withdrawal",
							source_doctype: "Good Deposit",
							get_query_filters: {
								docstatus: 1,
								per_delivered: "Deposited",
								company: cur_frm.doc.company
							}
						})
					}, __("Get items from"));
			}
	}
});
