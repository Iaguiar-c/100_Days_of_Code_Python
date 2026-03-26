# nested list in dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"]
# }

# print lille
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    }
}

print(travel_log["France"]["cities_visited"][2])