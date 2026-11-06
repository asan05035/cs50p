distances = {
    "Voyager 1" : "171",
    "Voyager 2" : "143",
    "Pioneer 11" : "119 AU",
    "New Horizon" : "65 AU"
}

def main():             # Orchestrator func - sfx
    spacecraft = input("Enter a spacecraft: ")
    distance = get_distance(spacecraft)     # manifesting abstraction
    print(distance)


def get_distance(spacecraft):   # Action func - hand you back some value
    try:
        distance = float(distances[spacecraft])
        return f"spacecraft is {distance * 149597870} km away from earth "
    except KeyError:
        return f"That spacecraft not availabe in the dictionary"
    except ValueError:
        return f"Value is in string cannot be converted"

if __name__ == '__main__':      # Convention - boilerplate -
    main()
    
    