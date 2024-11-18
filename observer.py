class LibraryObserver:
    def update(self, message):
        pass


class UserObserver(LibraryObserver):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Notification for {self.name}: {message}")


class LibraryNotifier:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def notify(self, message):
        for observer in self.subscribers:
            observer.update(message)
