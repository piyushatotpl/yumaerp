// Copyright (c) 2025, otpl and contributors
// For license information, please see license.txt

frappe.ui.form.on("Advance Shipping Note", {
	refresh(frm) {
		frm.set_query("purchase_order", function () {
			return {
				filters: {
					supplier: frm.doc.supplier || "",
				},
			};
		});
	},
});
