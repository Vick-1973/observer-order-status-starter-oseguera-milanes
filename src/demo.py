from order_status.order_status import OrderStatus
from order_status.customer_notifier import CustomerNotifier
from order_status.audit_observer import AuditObserver
from order_status.analytics_observer import AnalyticsObserver


# Create the observers
customer = CustomerNotifier()
audit = AuditObserver()
analytics = AnalyticsObserver()

# Create an order
order = OrderStatus("ORD-101")

# Subscribe observers
order.attach(customer)
order.attach(audit)
order.attach(analytics)

# First status change
order.set_status("PAID")

# Unsubscribe AuditObserver
order.detach(audit)

# Second status change
order.set_status("SHIPPED")

# Display results
print("Current status:", order.status)
print("Customer messages:", customer.messages)
print("Audit entries:", audit.entries)
print("Analytics counts:", analytics.status_counts)
