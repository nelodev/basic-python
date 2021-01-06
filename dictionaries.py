def run():
    # my_dict = {
    #     'key1': 1,
    #     'key2': 2,
    #     'key3': 3,
    # }
    # print(my_dict) # {'key1': 1, 'key2': 2, 'key3': 3}
    # print(my_dict['key_1']) # 1
    # print(my_dict['key_2']) # 2

    countries_population = {
        'Spain': 123123123,
        'Andorra': 123123,
        'Portugal': 984958
    }

    # print(countries_population['Norway']) # KeyError

    # for country in countries_population.keys():
    #     print(country)

    # for population in countries_population.values():
    #     print(population)

    for country, population in countries_population.items():
        print(country + " has " + str(population) + " people")

if __name__ == "__main__":
    run()