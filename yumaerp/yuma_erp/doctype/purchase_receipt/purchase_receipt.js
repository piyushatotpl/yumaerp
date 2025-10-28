frappe.ui.form.on("Purchase Receipt", {
    refresh: function (frm) {
        frm.add_custom_button(
            __("Advance Shipping Note"),
            function () {
                const me = this;

                erpnext.utils.map_current_doc({
                    method: "yumaerp.api.make_asn_to_purchase_invoice",
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
                    postprocess: function (mapped_item, source_doc, target_doc) {
                        // Set custom field to store the ASN name in each child row
						console.log(source_doc)
                        mapped_item.custom_advance_shipping_note = source_doc.name;
						mapped_item.purchase_order = source_doc.purchase_order;
                    }
                });
            },
            __("Get Items From")
        );
    },
});
