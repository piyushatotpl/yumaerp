frappe.listview_settings['Supplier Quotation'] = {
    get_indicator: function (doc) {
        console.log(doc)
        if (doc.custom_approval_status === "Accepted") {
            return [__("Accepted"), "green", "custom_approval_status,=,Accepted"];
        } else if (doc.custom_action_status === "Rejected") {
            return [__("Rejected"), "red", "custom_approval_status,=,Rejected"];
        } else {
            return [__("Pending"), "orange", "custom_approval_status,not in,Accepted,Rejected"];
        }
    }
};
