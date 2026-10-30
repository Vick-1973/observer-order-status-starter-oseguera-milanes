from .observer import Observer
class OrderStatus:
    def __init__(self, order_id: str, *observers: Observer):
        self.order_id = order_id
        self.status = "NEW"
        self._observers: list[Observer] = []

        for observer in observers:
            self.attach(observer)

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def set_status(self, status: str) -> None:
        self.status = status
        self.notify()

    def notify(self) -> None:
        for observer in tuple(self._observers):
            observer.update(self.order_id, self.status)
