country = {}

country["Egypt"] = ["Sudan", "Libya", "Morocco", "Algeria"]
country["Sudan"] = ["Libya"]
country["Libya"] = ["France", "Italy", "Greece", "Türkiye"]
country["Algeria"] = ["France", "Italy", "Greece", "Türkiye"]
country["Morocco"] = ["Saudi Arabia", "France", "Italy", "Greece", "Türkiye"]
country["Hungary"] = ["Slovenia", "Greece", "Türkiye"]
country["France"] = ["Italy"]
country["Slovenia"] = ["Italy"]
country["Greece"] = ["Slovenia", "France", "Hungary"]
country["Türkiye"] = ["Greece", "Slovenia", "Sweden"]
country["United State"] = ["France", "Greece", "Sweden"]
country["Italy"] = ["France", "Greece", "Slovenia"]


def country_is_target(name):
    if name == "Italy":
        return True


def search(name):
    search_in_queue = []
    search_in_queue += country[name]
    searched = []
    while search_in_queue:
        person = search_in_queue.pop(0)
        if person not in searched:
            if country_is_target(person):
                print(f"Yes, You can travel to {person}")
                return True
            else:
                search_in_queue += country[person]
                searched.append(person)
    print(f"No, You cannot travel to United State Italy")


search("Egypt")
