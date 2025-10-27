frappe.ui.form.on("Supplier Quotation", {
	refresh(frm) {
		// Only allow Purchase Manager to take action
		const has_permission = frappe.user_roles.includes("Purchase Manager");

		// Add buttons only for draft documents & correct role
		if (
			!frm.is_new() &&
			frm.doc.docstatus === 0 &&
			has_permission &&
			!frm.custom_buttons_added
		) {
			frm.custom_buttons_added = true; // prevent duplicates

			// --- Accept Button ---
			frm.add_custom_button(
				__("Accept"),
				() => {
					frappe.confirm(__("Are you sure you want to Accept this quotation?"), () => {
						frm.set_value("custom_approval_status", "Accepted");
						frm.set_value("custom_is_submittable", 1);
						frm.save("Submit");
					});
				},
				__("Actions")
			);

			// --- Reject Button ---
			frm.add_custom_button(
				__("Reject"),
				() => {
					frappe.confirm(__("Are you sure you want to Reject this quotation?"), () => {
						frm.set_value("custom_approval_status", "Rejected");
						frm.set_value("custom_is_submittable", 0);
						frm.save();
					});
				},
				__("Actions")
			);
		}

		// --- Visual Status Indicator ---
		if (frm.doc.custom_approval_status) {
			let color = "blue";
			if (frm.doc.custom_approval_status === "Accepted") color = "green";
			else if (frm.doc.custom_approval_status === "Rejected") color = "red";

			frm.page.set_indicator(__(frm.doc.custom_approval_status), color);
			frm.set_intro(__("Current Status: {0}", [frm.doc.custom_approval_status]), color);
		}

		// --- Hide action buttons for non-managers ---
		if (!has_permission) {
			frm.page.clear_actions_menu();
		}
	},

	// --- Validation before submit ---
	before_submit(frm) {
		if (!frm.doc.custom_is_submittable) {
			frappe.throw(
				__("You cannot submit this quotation until it is accepted by a Purchase Manager.")
			);
		}
	},
});
