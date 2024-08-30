import pytest
import Task_2


@pytest.fixture
def watering_system():
    return Task_2.WateringSystem()


def test_initial_soil_moisture(watering_system):
    watering_system.add_area("Garden", 30)
    assert watering_system.areas["Garden"]["soil_moisture"] == 30


def test_add_water(watering_system):
    watering_system.add_water(500)
    assert watering_system.water_level == 2500


def test_add_existing_area(watering_system):
    watering_system.add_area("Garden", 30)
    watering_system.add_area("Garden", 50)
    assert watering_system.areas["Garden"]["soil_moisture"] == 30


def test_add_new_area(watering_system):
    assert len(watering_system.areas) == 0
    watering_system.add_area("Lawn", 40)
    assert len(watering_system.areas) == 1


def test_water_spray_supply(watering_system):
    watering_system.add_area("Garden", 30)
    watering_system.water_spray_supply("Garden", 15)
    assert watering_system.areas["Garden"]["spray_water"] == 15


def test_water_area(watering_system):
    watering_system.add_area("Garden", 30)
    watering_system.water_area("Garden", 15)
    watering_system.water_spray_supply("Garden", 10)
    assert watering_system.areas["Garden"]["soil_moisture"] == 100


def test_water_area_not_enough_water(watering_system):
    watering_system.water_level = 0
    watering_system.add_area("Garden", 30)
    assert watering_system.water_area("Garden", 15) is None


def test_max_soil_moisture(watering_system):
    first_water_level_check = watering_system.water_level
    watering_system.add_area("Garden", 100)

    # Атрибут spray_water участвует в уравнении "water_needed = (duration * self.areas[area]["spray_water"])"
    # Без него, даже если первоначально soil_moisture будет 10 расхода water_level не будет
    watering_system.water_spray_supply("Garden", 10)

    watering_system.water_area("Garden", 30)
    second_water_level_check = watering_system.water_level

    assert first_water_level_check == second_water_level_check


def test_soil_moisture_after_long_watering(watering_system):
    watering_system.add_area("Garden", 30)
    watering_system.water_area("Garden", 60)

    assert watering_system.areas["Garden"]["soil_moisture"] == 100


def test_soil_moisture_after_watering(watering_system):
    watering_system.add_area("Garden", 30)
    watering_system.water_area("Garden", 60)
    assert watering_system.areas["Garden"]["soil_moisture"] == 100
