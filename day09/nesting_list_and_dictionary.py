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
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visites": 12
    },
    {
        "country":"Germany",
        "cities_visited":["Berline", "Hamburg", "Stutgart"],
        "total_visits": 5
    }
]
print(travel_log)
