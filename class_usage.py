class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._model = model
        self._registration = registration
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHIJK"[:self._num_seats_per_row])


class Flight:

    def __init__(self, number: str, aircraft: Aircraft):
        """Invariant declared here"""
        if not number[:2].isalpha():
            raise ValueError(f"First two characters must be string {number}")
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

    def number(self) -> str:
        return self._number

    def airline(self):
        return self._number[:2]

    def model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """seat in format - 12C"""

        row, l = self._parse_seat(seat)

        if self._seating[row][l] is not None:
            raise ValueError(f"Seat {seat} is occupied")

        self._seating[row][l] = passenger


    def _parse_seat(self, seat: str) -> (int, str):

        rows, seats = self._aircraft.seating_plan()

        l = seat[-1]
        row = seat[:-1]
        if l not in seats:
            raise ValueError(f"{l} is not value seat number")

        try:
            n_row = int(row)
        except ValueError:
            raise ValueError(f"Invalid row number {row}")

        if n_row not in rows:
            raise ValueError(f"Row number is outside {n_row}")

        return n_row, l

    def relocate_seat(self, passenger:str, from_seat:str, to_seat:str):

        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None and self._seating[from_row][from_letter] != passenger:
            raise ValueError(f'Passenger {passenger} not allocated to {from_seat}')

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f'Passenger {self._seating[to_row][to_letter]} already allocated to {to_seat}')

        self._seating[from_row][from_letter] = None
        self._seating[to_row][to_letter] = passenger

    def no_of_available(self) -> int:
        return sum(
            sum(
                1 for j in i if j is not None
            )
            for i in self._seating if i is not None
        )

    def make_boarding_card(self, card_printer):
        """
        card_printer can be replaced with html_boarding_cards (functional polymorphism)
        :param card_printer:
        :return:
        """
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(self._aircraft, passenger, seat, self._aircraft.model())

    def _passenger_seats(self):
        rows, seats = self._aircraft.seating_plan()
        for row in rows:
            for seat in seats:
                passenger = self._seating[row][seat]
                if passenger is not None:
                    yield passenger, f"{row}{seat}"


def print_boarding_cards(aircraft, passenger, seat, flight_number):
    output = f"|Name - {passenger}" \
        f" Flight : {flight_number}" \
        f" Seat : {seat}" \
        f" Aircraft : {aircraft}"
    banner = "+" + "-" * (len(output)-2) + "+"
    border = "|" + " " * (len(output)-2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)


#
"""
from class_usage import Aircraft, Flight, print_boarding_cards
f = Flight("DB23", Aircraft("D","D",4,5))
f.model()
[None, {'A': None, 'B': None, 'C': None, 'D': None, 'E': None}, {'A': None, 'B': None, 'C': None, 'D': None, 'E': None}, {'A': None, 'B': None, 'C': None, 'D': None, 'E': None}, {'A': None, 'B': None, 'C': None, 'D': None, 'E': None}]
from pprint import pprint as pp
pp(f._seating)

f.allocate_seat('2E','Amit')
f.allocate_seat('2D','Amita')
f.make_boarding_card(print_boarding_cards)
"""

