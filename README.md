# graphreader.py
A very (**VERY**) primitive command-line tool that is able to read data from a photo of a graph.

It's not very smart, so image should not contain anything but dark graph on a bright background (or the other way around with `-i` option), axes invisible (or bright, so program just cuts them off as background) and parallel to image borders.

The value is searched from top to bottom, the first hit is printed as an ansswer (result is saved as `temp.png`, so you can see how exactly search went).
