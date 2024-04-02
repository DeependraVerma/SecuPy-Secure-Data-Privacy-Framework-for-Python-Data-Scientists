class Auditing:
    def __init__(self):
        self.logs = []

    def log_event(self, event):
        self.logs.append(event)

    def get_logs(self):
        return self.logs
