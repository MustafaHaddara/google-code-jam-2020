class Event:
    def __init__(self, pos, start, end):
        self.position = pos
        self.start = start
        self.end = end


def scheduling(events):
    events.sort(key = lambda e: e.start)
    C_free = 0
    J_free = 0

    ordering = [None] * len(events)
    for idx,event in enumerate(events):
        if C_free <= event.start:
            ordering[event.position] = 'C'
            C_free = event.end
        elif J_free <= event.start:
            ordering[event.position] = 'J'
            J_free = event.end
        else:
            return 'IMPOSSIBLE'

    return ''.join(ordering)


def parse_events():
    num_events = int(input())
    events = []
    for i in range(num_events):
        start,end = input().split()
        events.append(Event(i, int(start), int(end)))
    return events

if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        events = parse_events()
        sched = scheduling(events)
        print("Case #{}: {}".format(i+1, sched))