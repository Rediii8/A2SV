class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.events:
           
            if startTime < e and endTime > s:
                return False
        
        self.events.append((startTime, endTime))
        return True