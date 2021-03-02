import json


def find_most_popular(d):
    kleidia = []
    for k in find_all_kleidia(d):
        kleidia.append(k)
    counter = 0
    most_frequent = kleidia[0]
    for i in keys:
        curr_frequency = kleidiacount(i)
        if curr_frequency > counter:
            counter = curr_frequency
            most_frequent = i
    return most_frequent


def find_all_kleidia(d):
    if isinstance(d, dict):
        for kleidia, value in d.items():
            if type(value) is dict or type(value) is list:
                yield kleidia
                yield from find_all_keys(value)
            else:
                yield kleidia
    elif isinstance(d, list):
        for v in d:
            yield from find_all_keys(v)


if __name__ == '__main__':
    filename = str(input("Please insert the name of the file you want to analyze: "))
    f = open(f"{filename}.txt", "r")
    example_text = f.read()
    example = json.loads(example_text)
    print(f"The most popular key in the following dictionary which was extracted from {filename}.txt : {example_text} is: {find_most_popular(example)}")
