# Order Status Observers — Observer Design Pattern

**Team conformed by:** Braulio Milanés Loza and Oswaldo Oseguera Sandoval

## Overview

This project demonstrates the Observer Design Pattern
using Python and object-oriented programming.

The goal is to allow an OrderStatus object to notify
multiple independent observers whenever its state changes.

The implementation follows the Observer pattern presented
in the "Decorator & Observer" class material.

## Design Pattern: Observer

The Observer pattern defines a one-to-many dependency
between objects.

When the Subject changes its state, all subscribed
observers are automatically notified.

The Subject does not need to know the concrete classes
of its observers.

## Components

### Observer

An abstract class that defines the update() method.

All concrete observers implement this contract.

### OrderStatus

The Subject that manages the current state of an order.

Responsibilities:
- Store the order ID and current status.
- Subscribe observers using attach().
- Unsubscribe observers using detach().
- Notify subscribed observers when the status changes.

### CustomerNotifier

A concrete Observer responsible for recording customer
notifications whenever an order status changes.

### AuditObserver

A concrete Observer responsible for recording order
status changes for auditing purposes.

### AnalyticsObserver

A new concrete Observer that counts status change events.

It was added without modifying the OrderStatus
notification logic.

## Project Structure

    src/
      order_status/
        __init__.py
        observer.py
        order_status.py
        customer_notifier.py
        audit_observer.py
        analytics_observer.py
      demo.py

    tests/
      test_observer_subscriptions.py
      (existing starter tests)

    README.md
    requirements.txt
    pyproject.toml

## Requirements

- Python 3.9 or newer
- pytest

## Installation

Clone your repository:

    git clone <YOUR_REPOSITORY_URL>

Navigate to your project folder.

Create a virtual environment (Windows):

    py -m venv .venv

Activate the environment:

    .venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install --upgrade pip
    pip install -r requirements.txt

## Running the Application

Run:

    python src/demo.py

Expected output:

    Current status: SHIPPED
    Customer messages: ['ORD-101:PAID', 'ORD-101:SHIPPED']
    Audit entries: [('ORD-101', 'PAID')]
    Analytics counts: {'PAID': 1, 'SHIPPED': 1}

## Running Tests

Execute all tests:

    python -m pytest -q

Execute the new focused test:

    python -m pytest tests/test_observer_subscriptions.py -v

The test verifies:
1. Observers receive state change notifications.
2. Duplicate subscriptions are ignored.
3. Unsubscribed observers stop receiving notifications.
4. Remaining observers continue receiving updates.
5. AnalyticsObserver records status counts correctly.

## How Does Observer Work?

First, an OrderStatus object is created.

Then, CustomerNotifier, AuditObserver and AnalyticsObserver
are subscribed to the Subject.

When set_status() changes the order status,
OrderStatus calls notify().

The notify() method invokes update() on all
subscribed observers.

Each observer handles the event independently.

## Why Was the Observer Contract Introduced?

The original OrderStatus implementation depended directly
on CustomerNotifier and AuditObserver.

This created tight coupling between the Subject
and concrete receiver classes.

The Observer contract removes those direct dependencies.

OrderStatus now depends only on the Observer abstraction.

## How Was AnalyticsObserver Added?

AnalyticsObserver was implemented as a new class
that inherits from Observer.

It implements update() to count status change events.

The new observer is registered using attach().

No changes to OrderStatus notification logic were required
to support AnalyticsObserver.

## What Do Attach and Detach Mean?

attach() subscribes an observer to the Subject.

detach() removes an observer from the subscription list.

After detaching, the observer no longer receives
notifications from future status changes.

This allows subscriptions to change at runtime.

## What Is the Subject?

OrderStatus is the Subject.

It owns the order state and notifies subscribed
observers when that state changes.

## What Is the Observer Contract?

Observer is an abstract class containing the update()
method.

Each concrete observer must implement this method.

This allows the Subject to communicate through
one stable interface.

## Who Owns the Reaction?

Each concrete observer owns its own reaction.

CustomerNotifier records notifications.

AuditObserver records audit entries.

AnalyticsObserver counts status change events.

OrderStatus does not implement these responsibilities.

## What Lifecycle or Coupling Cost Does Observer Introduce?

One lifecycle cost is managing subscriptions correctly.

Observers must be unsubscribed when they are no longer
needed.

Otherwise, the Subject may continue holding references
to unnecessary objects and sending unwanted notifications.

The pattern also introduces indirect communication,
which can make debugging notification flows harder.

## Design Decisions

- Observer is an abstract base class.
- OrderStatus acts as the Subject.
- Observers implement the same update() contract.
- Subscriptions use attach() and detach().
- Notifications use notify().
- Duplicate subscriptions are prevented.
- Each observer has one responsibility.
- One main class is implemented per source file.
- Existing notification and audit formats are preserved.
- New observers can be introduced without modifying
  OrderStatus notification logic.

## Conclusion

The Observer Design Pattern successfully separates
order state management from notification responsibilities.

OrderStatus now communicates with observers through
a stable interface instead of depending on concrete
receiver classes.

CustomerNotifier, AuditObserver and AnalyticsObserver
can subscribe and unsubscribe independently.

This implementation demonstrates loose coupling,
separation of responsibilities and extensibility.
