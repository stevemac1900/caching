import csv
import itertools
from brewerydb_queries import BreweryDBQueries

# These 2 mark the from/to lines from the csv file that will be queried in the for loop. just change them manually
# so tomorrow start at line 380 and end at line 760.
start_line = 1
end_line = 380

reader = csv.reader(open('personal_account.csv', 'r'), delimiter=',')
writer = csv.writer(open('style_cache.csv', 'a'), delimiter=',')

rows_i_to_j = itertools.islice(reader, start_line, end_line)

for row in rows_i_to_j:
    beer_name = row[0]
    beer_name = beer_name.title()
    query = BreweryDBQueries()
    writer.writerow([beer_name+","+query.get_beer_style(beer_name)])
