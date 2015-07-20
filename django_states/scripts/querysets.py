#!/usr/bin/env python

import csv
import os
import sys

sys.path.append("..")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_states.settings')

from django.db.models import Q
from main.models import State, StateCapital, City

#states = State.objects.all().values('name', 'abbreviation')
#
#states2 = State.objects.all().order_by('population').reverse().exclude(name__startswith="M")
#
#for state in states2:
#    print "%s, %s \n" % (state.name, state.population)
#    print "-------"

#he_dict = {1: 'val1'. 2: 'val2'}

#he_dict[(1, "a")] = "tuple"

#or x in the_dict.keys():
#   print x, " : ", the_dict[x]

#states = State.objects.all()

#or state in states:
#   print "-------%s-------" % state.name
#   for city in state.city_set.all():
#       print city

#cities = City.objects.all()

#print cities

states = State.objects.filter(city__name="Houston")

for state in states:
    cities = state.city_set.filter(name="Houston")
    for city in cities:
        print "%s | %s | %s" % (state, city.name, city.zip_code)

states_with_atown = State.objects.filter(city__name__startswith="A")

for state in states_with_atown:
    cities = state.city_set.filter(name__startswith="A")
    for city in cities:
        print "%s | %s | %s" % (state, city.name, city.zip_code)
