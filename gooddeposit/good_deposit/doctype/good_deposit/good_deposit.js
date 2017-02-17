// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Good Deposit', {
	refresh: function(frm) {
		if(frm.doc.docstatus==1) {
			cur_frm.add_custom_button(__('Withdraw'), this.make_withdrawal, __("Make"));
		}
		if (frm.doc.docstatus===0) {
				cur_frm.add_custom_button(__('Delivery Note'),
					function() {
						erpnext.utils.map_current_doc({
							method: "gooddeposit.gooddeposit.doctype.gooddeposit.gooddeposit.make_deposit",
							source_doctype: "Delivery Note",
							get_query_filters: {
								docstatus: 1,
								company: cur_frm.doc.company
							}
						})
					}, __("Get items from"));
			}
	},
	make_withdrawal: function() {
		frappe.model.open_mapped_doc({
			method: "gooddeposit.gooddeposit.doctype.gooddeposit.gooddeposit.make_withdrawal",
			frm: cur_frm
		})
	}
});
