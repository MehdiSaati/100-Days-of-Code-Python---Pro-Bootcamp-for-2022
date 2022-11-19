# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berline"
}
print(capitals)
travel_log = {
    "France":["Paris", "Lille", "Dijon"],
    "Germany":["Berline", "Hamburg", "Stutgart"]
}
print(travel_log)
# nesting Dictionary in a Dictionary
travel_log = {
    "France":{"cities_visited":["Paris", "Lille", "Dijon"], "total_visites": 12},
    "Germany":{"cities_visited":["Berline", "Hamburg", "Stutgart"],"total_visits": 5}
}
# nesting Dictionary in a List
travel_log = [
    {
        "country": "France", 
        "total_visites": 12,
        "cities_visited":["Paris", "Lille", "Dijon"]
        
    },
    {
        "country":"Germany",
        "total_visits": 5,
        "cities_visited":["Berline", "Hamburg", "Stutgart"]
        
    }
]
print(travel_log)
# add new country
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["total_visites"] = times_visited
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow","Saint"])
print(travel_log)
