def beers_left(num_beers):
    str_beer= str(num_beers)
    print (str_beer + " bottles of beer on the wall")
    print (str_beer + " bottles of beer")
    print ("if one of these bottles should happen to fall")
    while num_beers != 1:
    str_beer = str(num_beers)
    print (str_beer + " bottles of beer on the wall \n\n")
    if num_beers > 0:
        beers_left(num_beers)


my_beers = raw_input("How many beers are we starting with? ")
beers_left(int(my_beers))
