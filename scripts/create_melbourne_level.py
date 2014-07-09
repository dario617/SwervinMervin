#!/usr/bin/env python

import level as l

segments = []
sprites  = []
name     = "melbourne"

segments += l.add_straight(100, 0)
segments += l.add_corner(30, 85, 40, 5, 0, 20)
segments += l.add_straight(100, l.last_y(segments))
segments += l.add_corner(30, 45, 40, 4, l.last_y(segments))
segments += l.add_corner(30, 45, 40, -6, l.last_y(segments))
segments += l.add_corner(30, 45, 40, 6, l.last_y(segments))
segments += l.add_corner(30, 45, 40, -4, l.last_y(segments))
segments += l.add_hill(25, 25, 25, 0, l.last_y(segments))
segments += l.add_straight(150, 0)
segments += l.add_corner(80, 45, 40, 6, l.last_y(segments))
segments += l.add_corner(70, 45, 100, -6, l.last_y(segments))
segments += l.add_hill(25, 25, 25, 25, l.last_y(segments))
segments += l.add_straight(20, l.last_y(segments))
segments += l.add_hill(25, 25, 25, 0, l.last_y(segments))
segments += l.add_corner(140, 220, 140, 5, l.last_y(segments))
segments += l.add_hill(25, 25, 25, 15, l.last_y(segments))
segments += l.add_straight(5, l.last_y(segments))
segments += l.add_hill(25, 25, 25, 5, l.last_y(segments))
segments += l.add_straight(5, l.last_y(segments))
segments += l.add_hill(25, 25, 25, 20, l.last_y(segments))
segments += l.add_straight(5, l.last_y(segments))
segments += l.add_hill(25, 25, 25, 0, l.last_y(segments))
segments += l.add_straight(5, l.last_y(segments))
segments += l.add_hill(25, 25, 25, 25, l.last_y(segments))
segments += l.add_straight(5, l.last_y(segments))
segments += l.add_hill(25, 25, 25, 0, l.last_y(segments))
segments += l.add_straight(40, 0)
segments += l.add_corner(30, 55, 40, 5, 0, 25)
segments += l.add_straight(40, l.last_y(segments))
segments += l.add_corner(30, 55, 40, 5, l.last_y(segments), 0)
segments += l.add_straight(40, l.last_y(segments))
segments += l.add_corner(20, 20, 20, 3, l.last_y(segments))
segments += l.add_corner(20, 20, 20, -3, l.last_y(segments))
segments += l.add_corner(20, 20, 20, 3, l.last_y(segments))
segments += l.add_corner(20, 20, 20, -3, l.last_y(segments))
segments += l.add_straight(100, l.last_y(segments))

l.write("swervin_mervin/levels/{0}.csv".format(name), segments)
