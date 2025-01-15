class Event:
    def __init__(self, payload=None):
        self.payload = payload

    def __str__(self):
        return f"{self.__class__.__name__}: {self.payload}"
    

class ApplicationEvent(Event):
    pass


class ApplicationResultEvent(Event):
    pass


class Applicant:
    def __init__(self, name):
        self.name = name

    def submit_application(self, company, position, queue):
        event = ApplicationEvent({"name": self.name, "position": position})
        queue.append(event)
        company.receive_event(event)

class Company:
    def __init__(self, name):
        self.name = name
        
    def receive_event(self, event):
        print(f"[{self.name}] Received event: {event}")

    def respond_to_application(self, event, accepted, queue):
        result = "Accepted" if accepted else "Rejected"
        response_event = ApplicationResultEvent({"name": event.payload.get("name"), "result": result})
        queue.append(response_event)