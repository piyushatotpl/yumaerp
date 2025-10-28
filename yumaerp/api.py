import frappe
from frappe import _
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist(allow_guest=True)
def register_supplier(supplier_data, address_data, contact_data=None):
    """
    supplier_data: JSON string with Supplier fields
    address_data: JSON string with Address fields
    contact_data: optional JSON string with Contact fields
    """

    import json

    supplier_data = json.loads(supplier_data)
    address_data = json.loads(address_data)
    contact_data = json.loads(contact_data) if contact_data else {}

    try:
        # Check if supplier already exists by GSTIN or Name
        existing_supplier = frappe.db.exists(
            "Supplier", {"gstin": supplier_data.get("gstin")}
        )
        if existing_supplier:
            supplier = frappe.get_doc("Supplier", existing_supplier)
            frappe.msgprint(_("Supplier already exists. Updating existing record."))
            supplier.update(supplier_data)
            supplier.save(ignore_permissions=True)
        else:
            supplier = frappe.get_doc({"doctype": "Supplier", **supplier_data}).insert(
                ignore_permissions=True
            )

        # Create Address
        address = frappe.get_doc(
            {
                "doctype": "Address",
                **address_data,
                "links": [{"link_doctype": "Supplier", "link_name": supplier.name}],
            }
        ).insert(ignore_permissions=True)

        # Set this address as Supplier's primary address
        supplier_address_field = (
            "supplier_primary_address"
            if "supplier_primary_address" in supplier.meta.fields
            else "address"
        )
        supplier.db_set("supplier_primary_address", address.name)

        # Create Contact
        if contact_data:
            contact = frappe.get_doc(
                {
                    "doctype": "Contact",
                    **contact_data,
                    "links": [{"link_doctype": "Supplier", "link_name": supplier.name}],
                }
            ).insert(ignore_permissions=True)

            # Set primary contact
            supplier.db_set("supplier_primary_contact", contact.name)
        else:
            contact = None

        frappe.db.commit()

        return {
            "supplier": supplier.name,
            "address": address.name,
            "contact": contact.name if contact else None,
        }

    except Exception as e:
        frappe.log_error(message=str(e), title="Supplier Registration Error")
        frappe.throw(
            _("Error creating Supplier, Address or Contact: {0}").format(str(e))
        )


@frappe.whitelist()
def make_asn_to_purchase_invoice(source_name, target_doc=None, args=None):
    """Map Advance Shipping Note → Purchase Receipt"""

    def update_item(source, target, source_parent):
        # Copy quantity
        target.qty = source.qty
        # Set ASN reference in target child
        if hasattr(target, "custom_advance_shipping_note"):
            target.custom_advance_shipping_note = source_parent.name
        # Set purchase order if field exists
        if hasattr(target, "purchase_order"):
            target.purchase_order = source_parent.purchase_order

    doc = get_mapped_doc(
        "Advance Shipping Note",
        source_name,
        {
            "Advance Shipping Note": {
                "doctype": "Purchase Receipt",  # Target DocType
                "field_map": {
                    "supplier": "supplier",
                    "company": "company",
                    "posting_date": "posting_date",
                },
            },
            "ASN Items": {
                "doctype": "Purchase Receipt Item",  # Target Child Table
                "field_map": {
                    "item_code": "item_code",
                    "item_name": "item_name",
                    "description": "description",
                    "qty": "qty",
                    "uom": "uom",
                    "warehouse": "warehouse",
                    "batch_no": "batch_no",
                    "serial_no": "serial_no",
                    "package_no": "package_no",
                    "weight": "weight",
                    "remarks": "remarks",
                },
                "postprocess": update_item,
            },
        },
        target_doc,
    )

    return doc

