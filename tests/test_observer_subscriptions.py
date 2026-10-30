from order_status.order_status import OrderStatus
from order_status.customer_notifier import CustomerNotifier
from order_status.audit_observer import AuditObserver
from order_status.analytics_observer import AnalyticsObserver


def test_observers_receive_updates_and_detach_stops_notifications():
    order = OrderStatus("ORD-101")
    customer = CustomerNotifier()
    audit = AuditObserver()
    analytics = AnalyticsObserver()

    # Subscribe observers
    order.attach(customer)
    order.attach(audit)
    order.attach(analytics)

    # A duplicate subscription should be ignored
    order.attach(customer)

    # First status update
    order.set_status("PAID")

    assert customer.messages == ["ORD-101:PAID"]
    assert audit.entries == [("ORD-101", "PAID")]
    assert analytics.status_counts == {"PAID": 1}

    # Unsubscribe audit
    order.detach(audit)

    # Second status update
    order.set_status("SHIPPED")

    assert order.status == "SHIPPED"

    assert customer.messages == [
        "ORD-101:PAID",
        "ORD-101:SHIPPED"
    ]

    assert audit.entries == [
        ("ORD-101", "PAID")
    ]

    assert analytics.status_counts == {
        "PAID": 1,
        "SHIPPED": 1
    }
