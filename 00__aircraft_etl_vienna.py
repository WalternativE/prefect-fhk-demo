import aircraftlib as aclib


def main():
    # Get the live aircraft vector data around Dulles airport
    vienna_airport_position = aclib.Position(lat=48.1126, long=16.5755)
    area_surrounding_vienna = aclib.bounding_box(
        position=vienna_airport_position, radius_km=200
    )

    print("fetching reference data...")
    ref_data = aclib.fetch_reference_data()

    print("fetching live aircraft data...")
    raw_aircraft_data = aclib.fetch_live_aircraft_data(area=area_surrounding_vienna)

    print("cleaning & transform aircraft data...")
    live_aircraft_data = []
    for raw_vector in raw_aircraft_data:
        vector = aclib.clean_vector(raw_vector)
        if vector:
            aclib.add_airline_info(vector, ref_data.airlines)
            live_aircraft_data.append(vector)

    print("saving live aircraft data...")
    db = aclib.Database()
    db.add_live_aircraft_data(live_aircraft_data)

    print("saving reference data...")
    db.update_reference_data(ref_data)

    print("complete!")


if __name__ == "__main__":
    main()
