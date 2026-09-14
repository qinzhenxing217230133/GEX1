######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################

airport_info = ("OUL", 1, "14-09-2026")
allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}
restricted_destinations = {"Moscow", "Pyongyang"}

flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": [
            "Alice Wong",
            "David Kim",
            "Fatima Ali"
        ]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": [
            "Chen Wei",
            "George Smith"
        ]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": [
            "Hana Lee",
            "Maria Garcia",
            "Noah Wilson"
        ]
    }
}


def find_flight(flights, flight_number):
    input_clean = flight_number.strip().lower()
    for real_key in flights:
        if real_key.lower() == input_clean:
            return real_key
    return None


def passenger_exists(passengers, passenger_name):
    name_clean = passenger_name.strip().lower()
    for p in passengers:
        if p.lower() == name_clean:
            return True
    return False


def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    real_flight_key = find_flight(flights, flight_number)
    if real_flight_key is None:
        return "FLIGHT_NOT_FOUND"

    name_stripped = passenger_name.strip()
    if len(name_stripped) == 0:
        return "EMPTY_NAME"

    flight = flights[real_flight_key]

    if flight["destination"] in restricted_destinations:
        return "RESTRICTED"

    if passenger_exists(flight["passengers"], name_stripped):
        return "DUPLICATE"

    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"

    flight["passengers"].append(name_stripped.title())
    return "OK"


def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    real_flight_key = find_flight(flights, flight_number)
    if real_flight_key is None:
        return "FLIGHT_NOT_FOUND"

    flight = flights[real_flight_key]
    target_clean = passenger_name.strip().lower()

    for idx, p_name in enumerate(flight["passengers"]):
        if p_name.lower() == target_clean:
            del flight["passengers"][idx]
            return "OK"
    return "PASSENGER_NOT_FOUND"


def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    real_flight_key = find_flight(flights, flight_number)
    if real_flight_key is None:
        return "FLIGHT_NOT_FOUND"

    new_gate_clean = new_gate.strip().upper()
    allowed_upper = {g.upper() for g in allowed_gates}
    if new_gate_clean not in allowed_upper:
        return "INVALID_GATE"

    actual_gate = None
    for g in allowed_gates:
        if g.upper() == new_gate_clean:
            actual_gate = g
            break
    flight = flights[real_flight_key]
    flight["gate"] = actual_gate
    return "OK"


def flight_status(flight):
    cap = flight["capacity"]
    count = len(flight["passengers"])
    percent = count / cap * 100
    if percent >= 100:
        return "FULL"
    elif percent >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


def sorted_manifest(
    flights,
    flight_number
):
    real_flight_key = find_flight(flights, flight_number)
    if real_flight_key is None:
        return None
    flight = flights[real_flight_key]
    return sorted(flight["passengers"])


def total_passengers(flights):
    total = 0
    for f in flights.values():
        total += len(f["passengers"])
    return total


def any_full_flight(flights):
    for f in flights.values():
        if len(f["passengers"]) >= f["capacity"]:
            return True
    return False


def all_flights_have_passengers(flights):
    for f in flights.values():
        if len(f["passengers"]) == 0:
            return False
    return True
