import pytest
from parking_lot import ParkingLot
from Vehicle import Car


@pytest.fixture
def parking_lot():
    lot = ParkingLot()
    lot.create_parking_lot(5)
    return lot


def test_create_parking_lot(parking_lot):
    assert parking_lot.capacity == 5
    assert len(parking_lot.slots) == 5
    assert parking_lot.slots == [-1] * 5


def test_park(parking_lot):
    slot_id = parking_lot.park("KA-01-HH-1234", "White")
    assert slot_id == 1
    assert isinstance(parking_lot.slots[0], Car)
    assert parking_lot.slots[0].regno == "KA-01-HH-1234"
    assert parking_lot.slots[0].color == "White"


def test_leave_slot(parking_lot):
    parking_lot.park("KA-01-HH-1234", "White")
    result = parking_lot.leave_slot(1)
    assert result is True
    assert parking_lot.slots[0] == -1


def test_check_status(parking_lot):
    parking_lot.park("KA-01-HH-1234", "White")
    parking_lot.park("KA-01-HH-5678", "Black")
    status = []
    parking_lot.check_status = lambda: status.append("\n".join([
        "Slot No \tRegistration No \tColor",
        "1\tKA-01-HH-1234\tWhite",
        "2\tKA-01-HH-5678\tBlack"
    ]))
    parking_lot.check_status()
    expected_status = "Slot No \tRegistration No \tColor\n1\tKA-01-HH-1234\tWhite\n2\tKA-01-HH-5678\tBlack"
    assert status[0] == expected_status


def test_get_regno_from_color(parking_lot):
    parking_lot.park("KA-01-HH-1234", "White")
    parking_lot.park("KA-01-HH-5678", "White")
    regnos = parking_lot.get_regno_from_color("White")
    assert regnos == ["KA-01-HH-1234", "KA-01-HH-5678"]


def test_get_slotno_from_regno(parking_lot):
    parking_lot.park("KA-01-HH-1234", "White")
    slotno = parking_lot.get_slotno_from_regno("KA-01-HH-1234")
    assert slotno == 1


def test_get_slotno_from_color(parking_lot):
    parking_lot.park("KA-01-HH-1234", "White")
    parking_lot.park("KA-01-HH-5678", "White")
    slotnos = parking_lot.get_slotno_from_color("White")
    assert slotnos == ["1", "2"]


def test_show_data_park(parking_lot, capsys):
    parking_lot.show_data("park KA-01-HH-1234 White")
    captured = capsys.readouterr()
    assert "Allocated slot number: 1" in captured.out


def test_show_data_leave(parking_lot, capsys):
    parking_lot.park("KA-01-HH-1234", "White")
    parking_lot.show_data("leave_slot 1")
    captured = capsys.readouterr()
    assert "slot number 1 is free" in captured.out


def test_show_data_status(parking_lot, capsys):
    parking_lot.park("KA-01-HH-1234", "White")
    parking_lot.show_data("status")
    captured = capsys.readouterr()
    assert "1\tKA-01-HH-1234\tWhite" in captured.out


def test_show_data_regno_for_cars_with_colour(parking_lot, capsys):
    parking_lot.park("KA-01-HH-1234", "White")
    parking_lot.park("KA-01-HH-5678", "White")
    parking_lot.show_data("regno_for_cars_with_colour White")
    captured = capsys.readouterr()
    assert "KA-01-HH-1234, KA-01-HH-5678" in captured.out


def test_show_data_slotno_for_cars_with_colour(parking_lot, capsys):
    parking_lot.park("KA-01-HH-1234", "White")
    parking_lot.park("KA-01-HH-5678", "White")
    parking_lot.show_data("slotno_for_cars_with_colour White")
    captured = capsys.readouterr()
    assert "1, 2" in captured.out


def test_show_data_slot_number_for_regno(parking_lot, capsys):
    parking_lot.park("KA-01-HH-1234", "White")
    parking_lot.show_data("slot_number_for_regno KA-01-HH-1234")
    captured = capsys.readouterr()
    assert "1" in captured.out


def test_show_data_exit(parking_lot, capsys):
    with pytest.raises(SystemExit):
        parking_lot.show_data("exit")
