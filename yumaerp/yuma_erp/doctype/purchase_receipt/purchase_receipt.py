import frappe

def validation(self, method):
    if not self.custom_supplier_invoice_no:
        return

    # Get current fiscal year based on the posting date (or today if not set)
    fiscal_year = frappe.db.get_value(
        "Fiscal Year",
        {"year_start_date": ["<=", self.posting_date or frappe.utils.today()],
         "year_end_date": [">=", self.posting_date or frappe.utils.today()]},
        "name"
    )

    if not fiscal_year:
        frappe.throw("Could not determine the current Fiscal Year.")

    # Get fiscal year start and end dates
    fy_start, fy_end = frappe.db.get_value(
        "Fiscal Year", fiscal_year, ["year_start_date", "year_end_date"]
    )

    # Check for duplicates in the same fiscal year (excluding current document)
    exists = frappe.db.exists(
        "Purchase Receipt",
        {
            "custom_supplier_invoice_no": self.custom_supplier_invoice_no,
            "posting_date": ["between", [fy_start, fy_end]],
            "name": ["!=", self.name],  # ignore current document
        },
    )

    if exists:
        link = f"/app/purchase-receipt/{exists}"
        frappe.throw(
            f"Purchase Receipt with supplier invoice number "
            f"'<b>{self.custom_supplier_invoice_no}</b>' already exists "
            f"in fiscal year <b>{fiscal_year}</b>: "
            f"<a href='{link}' target='_blank'>{exists}</a>"
        )
