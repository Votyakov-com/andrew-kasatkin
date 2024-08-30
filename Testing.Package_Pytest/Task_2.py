class WateringSystem:
    def __init__(self):
        self.water_level = 2000  # Начальный уровень воды в системе
        self.is_watering = False  # Флаг, указывающий, идет ли полив в данный момент
        self.areas = {}  # Возможные участки для полива

    @property
    def water_level(self):
        return self._water_level

    @water_level.setter
    def water_level(self, value):
        self._water_level = value

    @property
    def is_watering(self):
        return self._is_watering

    @is_watering.setter
    def is_watering(self, value):
        self._is_watering = value

    def get_water_level(self):
        print(f"Current water level in the system: {self.water_level} ml \n")

    def add_water(self, amount):
        self.water_level += amount

    def add_area(self, area, initial_moisture):
        if area not in self.areas:
            self.areas[area] = {
                "soil_moisture": initial_moisture,  # Уровень влажности почвы на участке
                "spray_water": 0,  # Скорость подачи воды
            }
        else:
            print(f"An area named {area} already exists in the system.")

    def check_soil_moisture(self, area_name=None):
        if area_name is not None:
            if area_name in self.areas:
                moisture = self.areas[area_name]["soil_moisture"]
                print(f"Moisture level for area {area_name}: {moisture}%.")
            else:
                print(f"An area named {area_name} already exists in the system.")
        else:
            for area, data in self.areas.items():
                moisture = data["soil_moisture"]
                print(f"Moisture level for area {area_name}: {moisture}%.")

    def water_area(self, area, duration):
        if area in self.areas:
            if self.is_watering:
                print(
                    "Watering is already in progress. Wait for the current watering to complete."
                )
                return  # Останавливаем выполнение метода
            print(f"Watering of the {area} has been started.")
            self.is_watering = True
            water_needed = (
                duration * self.areas[area]["spray_water"]
            )  # Вычисляем необходимое количество воды
            if self.water_level >= water_needed:
                if self.areas[area]["soil_moisture"] < 100:
                    # Если уровень влажности на участке не достиг 100%
                    self.water_level -= water_needed
                    new_soil_moisture = self.areas[area]["soil_moisture"] + (
                        duration * 5
                    )
                    self.areas[area]["soil_moisture"] = min(
                        new_soil_moisture, 100
                    )  # Ограничиваем влажность до 100%
                else:
                    print(
                        f"Zone {area} already has maximum moisture (100%) and does not require watering."
                    )
            else:
                print(f"Not enough water to spray the area {area}")
            print(f"The watering of the {area} has been completed.")
            self.is_watering = False

    def water_spray_supply(self, area, spray_water):
        if area in self.areas:
            self.areas[area]["spray_water"] = spray_water
        else:
            print(
                f"Area named {area} does not exist in the system. Please add a site using add_area."
            )


if __name__ == "__main__":
    system = WateringSystem()

    system.get_water_level()

    system.add_area("Garden", 30)
    system.check_soil_moisture("Garden")
    system.water_spray_supply("Garden", 10)
    system.water_area("Garden", 30)
    system.check_soil_moisture("Garden")

    system.get_water_level()

    system.add_area("Flowerbed", 25)
    system.check_soil_moisture("Flowerbed")
    system.water_spray_supply("Flowerbed", 8)
    system.water_area("Flowerbed", 20)
    system.check_soil_moisture("Flowerbed")

    system.get_water_level()
