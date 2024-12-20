import importlib

run_days = {
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
    7: False,
    8: False,
    9: False,
    10: False,
    11: False,
    12: False,
    13: False,
    14: False,
    15: False,
    16: False,
    17: False,
    18: False,
    19: True
}

for iday in run_days:
    if not run_days[iday]:
        continue

    print(f"\nDay { iday }")
    importlib.import_module(f"Days.day{iday}")
    print("")

