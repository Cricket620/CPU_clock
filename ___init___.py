#Speed of light in m/s
speed_of_light = 299792458

#One billionth (of a second)
billionth = 1.0/1000000000

#Nanostick - number of centimeters that a photon in a vacuum travels in one second
nanostick = speed_of_light*billionth*100

#Processor speed (cycles per second - 2.7GHz used as example)
cycles_per_second = 2700000000

cycle_distance = nanostick/cycles_per_second

print cycle_distance
