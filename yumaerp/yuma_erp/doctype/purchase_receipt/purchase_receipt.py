import frappe

def validation(self, method):
    if not self.custom_supplier_invoice_no:
        return

    posting_date = self.posting_date or frappe.utils.today()

    # Get current fiscal year based on posting date
    fiscal_year = frappe.db.get_value(
        "Fiscal Year",
        {
            "year_start_date": ["<=", posting_date],
            "year_end_date": [">=", posting_date],
        },
        "name"
    )

    if not fiscal_year:
        frappe.throw("Could not determine the current Fiscal Year.")

    # Get fiscal year start and end dates
    fy_start, fy_end = frappe.db.get_value(
        "Fiscal Year", fiscal_year, ["year_start_date", "year_end_date"]
    )

    # Check for duplicate for same GSTIN and Supplier Invoice No in the same fiscal year
    exists = frappe.db.exists(
        "Purchase Receipt",
        {
            "custom_supplier_invoice_no": self.custom_supplier_invoice_no,
            "supplier": self.supplier,
            "posting_date": ["between", [fy_start, fy_end]],
            "name": ["!=", self.name],  # exclude current doc
        },
    )

    if exists:
        link = f"/app/purchase-receipt/{exists}"
        frappe.throw(
            f"Purchase Receipt with Supplier Invoice No "
            f"'<b>{self.custom_supplier_invoice_no}</b>' for supplier "
            f"'<b>{self.supplier}</b>' already exists "
            f"in Fiscal Year <b>{fiscal_year}</b>: "
            f"<a href='{link}' target='_blank'>{exists}</a>"
        )