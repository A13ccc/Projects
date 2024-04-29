# Write code below 💖

import math
from random import choice as ch


planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]


def formula(rad):
  area = 4 * math.pi * rad ** 2
  return area


rnd_planet = ch(planets)


if rnd_planet == 'Mercury':
  rad = 2440
  print('The radius of', rnd_planet, 'is', rad, 'and the surface area is', "{:,.2f}".format(round(formula(rad), 3)))
elif rnd_planet == 'Venus':
  rad = 6052
  print('The radius of', rnd_planet, 'is', rad, 'and the surface area is', "{:,.2f}".format(round(formula(rad), 3)))
elif rnd_planet == 'Earth':
  rad = 6371
  print('The radius of', rnd_planet, 'is', rad, 'and the surface area is', "{:,.2f}".format(round(formula(rad), 3)))
elif rnd_planet == 'Mars':
  rad = 3390
  print('The radius of', rnd_planet, 'is', rad, 'and the surface area is', "{:,.2f}".format(round(formula(rad), 3)))
elif rnd_planet == 'Saturn':
  rad = 58232
  print('The radius of', rnd_planet, 'is', rad, 'and the surface area is', "{:,.2f}".format(round(formula(rad), 3)))
else:
  print("Oops! An error occured.")
