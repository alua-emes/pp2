#create output that resembles the following by parsing the included JSON file.
import json
with open("data.json", "r") as read_file:
    data = json.load(read_file)
    print(data)
    print("Interface Status")
    print("==============================================================================")
    print("DN                                             Description          Speed                      MTU ")
    for i, k in data["imdata"][0]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k, end="                          ")
        if i == "speed":
            print(k, end="                                         ")
        if i == "mtu":
            print(k, end="                   ")