import json

place =[]

while True:
    place = input("Enter a place (or 'q' to quit): ")
    if place.lower() == 'q':
        break
    place.append(place)

places_json = json.dumps(place, indent=4)

print("\nAll places entered: ")
print(places_json)