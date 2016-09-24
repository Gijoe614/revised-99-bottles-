def beers_left(num_beers):
   while num_beers > 0:
       str_beer = str(num_beers)
       print (str_beer + " bottles of beer on the wall")
       print (str_beer + " bottles of beer")
       print ("if one of these bottles should happen to fall")
       num_beers -= 1
       str_beer = str(num_beers)
       print (str_beer + " bottles of beer on the wall \n\n")

my_beers = raw_input("How many beers are we starting with? ")
beers_left(int(my_beers))
