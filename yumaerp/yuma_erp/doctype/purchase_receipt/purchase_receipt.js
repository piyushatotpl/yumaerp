frappe.ui.form.on("Purchase Receipt", {
	refresh: function (frm) {
		frm.add_custom_button(
			__("Advance Shipping Note"),
			function () {
				const me = this;

				erpnext.utils.map_current_doc({
					method: "pinnacleprod.api.make_asn_to_purchase_invoice",
					source_doctype: "Advance Shipping Note",
					target: frm,
					setters: {
						supplier: frm.doc.supplier || undefined,
						company: frm.doc.company || undefined,
					},
					get_query_filters: {
						docstatus: 1,
					},
					allow_child_item_selection: true,
					child_fieldname: "asn_items",
					child_columns: [
						"item_code",
						"item_name",
						"description",
						"qty",
						"uom",
						"schedule_date",
						"warehouse",
						"batch_no",
						"serial_no",
						"package_no",
						"weight",
						"remarks",
					],
				});
			},
			__("Get Items From")
		);
	},
});
