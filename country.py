class Country:
    def __init__(self, name):
        self.name = name
        self.states = []
        self.union_territories = []

    def add_state(self, state):
        self.states.append(state)

    def add_union_territory(self, ut):
        self.union_territories.append(ut)

    def __str__(self):
        return f"Country: {self.name}, States: {len(self.states)}, Union Territories: {len(self.union_territories)}"


class State:
    def __init__(self, name):
        self.name = name
        self.districts = []

    def add_district(self, district):
        self.districts.append(district)

    def __str__(self):
        return f"State: {self.name}, Districts: {len(self.districts)}"


class District:
    def __init__(self, name):
        self.name = name
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

    def __str__(self):
        return f"District: {self.name}, Cities: {len(self.cities)}"


class City:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"City: {self.name}"


class UnionTerritory:
    def __init__(self, name):
        self.name = name
        self.districts = []

    def add_district(self, district):
        self.districts.append(district)

    def __str__(self):
        return f"Union Territory: {self.name}, Districts: {len(self.districts)}"


# Example usage:
if __name__ == "__main__":
    # Country creation
    india = Country("India")

    # States creation
    karnataka = State("Karnataka")
    maharashtra = State("Maharashtra")

    # Districts creation
    bangalore_district = District("Bangalore")
    mumbai_district = District("Mumbai")

    # Cities creation
    bangalore_city = City("Bangalore")
    mumbai_city = City("Mumbai")

    # Adding cities to districts
    bangalore_district.add_city(bangalore_city)
    mumbai_district.add_city(mumbai_city)

    # Adding districts to states
    karnataka.add_district(bangalore_district)
    maharashtra.add_district(mumbai_district)

    # Adding states to country
    india.add_state(karnataka)
    india.add_state(maharashtra)

    # Creating a Union Territory and adding districts to it
    delhi_ut = UnionTerritory("Delhi")
    delhi_ut.add_district(District("New Delhi"))

    # Adding Union Territory to country
    india.add_union_territory(delhi_ut)

    print(india)
    for state in india.states:
        print(state)
        for district in state.districts:
            print(f"  {district}")
            for city in district.cities:
                print(f"    {city}")

    for ut in india.union_territories:
        print(ut)
        for district in ut.districts:
            print(f"  {district}")
            for city in district.cities:
                print(f"    {city}")
