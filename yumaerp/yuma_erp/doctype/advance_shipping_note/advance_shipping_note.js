// Copyright (c) 2025, otpl and contributors
// For license information, please see license.txt

frappe.ui.form.on("Advance Shipping Note", {
    refresh(frm) {
        set_purchase_order_query(frm);
    },

    supplier(frm) {
        // Reset purchase_order when supplier changes
        frm.set_value("purchase_order", null);
        frm.refresh_field("purchase_order");

        set_purchase_order_query(frm);
    },

    purchase_order(frm) {
        if (!frm.doc.purchase_order) return;

        const table_fieldname = "asn_items"; // Update if your child table fieldname is different
        frm.clear_table(table_fieldname);

        frappe.call({
            method: "frappe.client.get",
            args: {
                doctype: "Purchase Order",
                name: frm.doc.purchase_order,
            },
            callback: function (r) {
                if (r.message) {
                    r.message.items.forEach(function (po_item) {
                        let row = frm.add_child(table_fieldname);
                        row.item_code = po_item.item_code;
                        row.item_name = po_item.item_name;
                        row.description = po_item.description;
                        row.qty = po_item.qty - po_item.received_qty;
                        row.uom = po_item.uom;
                        row.rate = po_item.rate;
						row.amount = po_item.amount;
                    });
                    frm.refresh_field(table_fieldname);
                }
            },
        });
    },
});

// Helper function to set Purchase Order query
function set_purchase_order_query(frm) {
    frm.set_query("purchase_order", function () {
        if (frm.doc.supplier) {
            return {
                filters: {
                    supplier: frm.doc.supplier,
                    docstatus: 1
                },
            };
        } else {
            return {};
        }
    });
}
