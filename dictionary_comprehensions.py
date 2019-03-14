#import pdb
from pprint import pprint as pp

country_to_capital = {'United Kingdom': 'London',
                      'Brazil': 'Brazilia',
                      'Morocco': 'Rabat',
                      'Sweden': 'Stockholm'}
#pdb.set_trace()
capital_to_country = {capital: country for country, capital in country_to_capital.items()}

#for lists
#[ expr(item) for item in iterable ]

def main():
    pp(country_to_capital)
    pp(capital_to_country)

if __name__ == "__main__":
    main()