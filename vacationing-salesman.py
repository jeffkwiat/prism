import geopy

from geopy.distance import vincenty
from geopy.geocoders import Nominatim

class VacationingSalesman(object):
    """ Show the distances between multiple legs of a vacation. """

    def __init__(self, vacations, use_miles=True):
        self.vacations = vacations
        self.use_miles = use_miles
        self.legs = []

    def run(self):
        """
        Loop through the list of vacation spots and measure
        the distance between them.

        """
        geolocator = Nominatim()
        units = 'miles'
        total_distance = 0

        print('Success! Your vacation itinerary is:')
        for leg in range(1, len(self.vacations)):
            origin = geolocator.geocode(self.vacations[leg - 1])
            destination = geolocator.geocode(self.vacations[leg])
            distance = 0

            if self.use_miles:
                distance = vincenty((origin.latitude, origin.longitude),
                               (destination.latitude, destination.longitude)).miles
            else:
                units = 'kilometers'
                distance = vincenty((origin.latitude, origin.longitude),
                               (destination.latitude, destination.longitude)).kilometers

            total_distance += distance
            print('%s -> %s: %s %s' % (self.vacations[leg - 1],
                                    self.vacations[leg],
                                    '%0.2f' % distance,
                                      units))


        print('Total distance covered in your trip: %0.2f %s' % (total_distance, units))

if __name__ == "__main__":
    vacations = ["Paris, France",
                "New York City, USA",
                "Nuuk, Greenland"]

    salesman = VacationingSalesman(vacations)
    salesman.run()