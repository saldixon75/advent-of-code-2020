import numpy;
import sys;
import re;


def is_running(timetable_entry):
    return (not timetable_entry == 'x');

with open("input.txt") as f:
    lines = f.read().splitlines();

earliest_departure = int(lines[0]);
buses = map(int,filter(is_running, lines[1].rsplit(',')));

def get_next_bus(bus_frequency, timestamp):
    # relative to timestamp
    previous_bus = (timestamp ) % bus_frequency ;
    next_bus = bus_frequency - previous_bus ;
    return next_bus;

for bus in buses:
    next_bus = get_next_bus(bus, earliest_departure);
    print("Bus id = " + str(bus) + " leaves in " + str(next_bus) + " minutes");



    












