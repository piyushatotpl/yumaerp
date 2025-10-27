app_name = "yumaerp"
app_title = "Yuma ERP"
app_publisher = "otpl"
app_description = "app to customize erpnext for yuma"
app_email = "support@otpl.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "yumaerp",
# 		"logo": "/assets/yumaerp/logo.png",
# 		"title": "Yuma ERP",
# 		"route": "/yumaerp",
# 		"has_permission": "yumaerp.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/yumaerp/css/yumaerp.css"
# app_include_js = "/assets/yumaerp/js/yumaerp.js"

# include js, css files in header of web template
# web_include_css = "/assets/yumaerp/css/yumaerp.css"
# web_include_js = "/assets/yumaerp/js/yumaerp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "yumaerp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Purchase Receipt": "yumaerp/doctype/purchase_receipt/purchase_receipt.js",
    "Supplier Quotation": "pinnacle_production/doctype/supplier_quotation/supplier_quotation.js",
}
doctype_list_js = {
    "Supplier Quotation": "yumaerp/doctype/supplier_quotation/supplier_quotation_listview.js"
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "yumaerp/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "yumaerp.utils.jinja_methods",
# 	"filters": "yumaerp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "yumaerp.install.before_install"
# after_install = "yumaerp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "yumaerp.uninstall.before_uninstall"
# after_uninstall = "yumaerp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "yumaerp.utils.before_app_install"
# after_app_install = "yumaerp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "yumaerp.utils.before_app_uninstall"
# after_app_uninstall = "yumaerp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "yumaerp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    # "*": {
    # 	"on_update": "method",
    # 	"on_cancel": "method",
    # 	"on_trash": "method"
    # }
    "Purchase Receipt": {
        "validate": "yumaerp.yuma_erp.doctype.purchase_receipt.purchase_receipt.validation"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"yumaerp.tasks.all"
# 	],
# 	"daily": [
# 		"yumaerp.tasks.daily"
# 	],
# 	"hourly": [
# 		"yumaerp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"yumaerp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"yumaerp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "yumaerp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "yumaerp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "yumaerp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["yumaerp.utils.before_request"]
# after_request = ["yumaerp.utils.after_request"]

# Job Events
# ----------
# before_job = ["yumaerp.utils.before_job"]
# after_job = ["yumaerp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"yumaerp.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
