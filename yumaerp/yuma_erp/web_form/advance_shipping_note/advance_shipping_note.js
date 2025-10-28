frappe.ready(function () {
	frappe.call({
		method: "yumaerp.api.get_supplier_for_user",
		args: { user: frappe.session.user },
		callback: function (r) {
			if (r.message) {
				frappe.web_form.set_value("supplier", r.message);

				// Filter Purchase Orders by supplier
				frappe.web_form.set_df_property("purchase_order", "get_query", () => {
					return { filters: { supplier: r.message } };
				});
			} else {
				frappe.msgprint("No Supplier record linked with your user account.");
			}
		},
	});
});
