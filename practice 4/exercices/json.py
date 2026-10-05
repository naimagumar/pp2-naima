import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("DN                                                 Description           Speed    MTU")
print("-" * 80)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]

    print(
        f"{attr['dn']:50} "
        f"{attr['descr']:20} "
        f"{attr['speed']:8} "
        f"{attr['mtu']}"
    )







   