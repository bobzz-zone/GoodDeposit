// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Good Deposit', {
	refresh: function(frm) {
		if(doc.docstatus==1) {
			cur_frm.add_custom_button(__('Withdraw'), this.make_withdrawal, __("Make"));
		}
	},
	make_withdrawal: function() {
		frappe.model.open_mapped_doc({
			method: "gooddeposit.gooddeposit.doctype.gooddeposit.gooddeposit.make_withdrawal",
			frm: cur_frm
		})
	}
});
