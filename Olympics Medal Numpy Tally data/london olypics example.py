import numpy as np

country = np.array(["Great Britain","China","Russia","United States","Korea","Japan","Germany"])
country_code = np.array(["GBR","CHN","RUS","US","KOR","JPN","GER"])
gold_medal = np.array([29,38,24,46,13,7,11])
silver_medal = np.array([17,28,25,28,8,14,11])
bronze_medal = np.array([19,22,32,29,7,17,14])

gold_max = gold_medal.argmax()
max_gold_country=country[gold_max]
print("The country that won maximum gold medals is {}".format(max_gold_country))

more_than_20_gold_medals = [gold_medal > 20]
country_with_20plus_goldmedals = country[more_than_20_gold_medals]
print("The countries with more than 20 gold medals include {}".format(country_with_20plus_goldmedals))

medal_tally = np.concatenate([[gold_medal],[silver_medal],[bronze_medal]])
print("The medal tally is \n", medal_tally.transpose())

gold_medal_countries = np.concatenate([[country],[gold_medal]])
print("The countries along with their gold medal include \n", gold_medal_countries.transpose())

for i in range(len(country)):
    country_concat = country[i]
    total_medal = gold_medal[i] + silver_medal[i]+ bronze_medal[i]
    print("{}, total medal {}".format(country_concat, total_medal))


