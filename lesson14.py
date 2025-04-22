def places(place, address, **place_info):
    place_info["address"] = address
    place_info["place_name"] = place

    return place_info

profiles = places("Ресторан", "Улица кала", menu="kal", price="dorogo")
print(profiles)

