#Speed of light in m/s
speed_of_light = 299792458

#One billionth (of a second)
#Converts speed_of_light into m/nanosecond
billionth = 1.0/1000000000

#Nanostick - distance in cm that a photon in a vacuum travels in one nanosecond
nanostick = speed_of_light*billionth*100

#Processor speed (cycles per second - 2.7GHz used as example)
cycles_per_second = 2700000000

CPU_cycle_distance = nanostick/cycles_per_second

print CPU_cycle_distance
