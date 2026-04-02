# Task 1 — The Lie Detector 🔍
# Write a function that takes two dicts — one of "claims" and one of "facts" — and returns which claims are lies, which are true, and which cannot be verified.
pythonclaims = {"sky": "green", "water": "wet", "fire": "cold"}
facts  = {"sky": "blue",  "water": "wet"}

# expected output:
# VERIFIED TRUE:  ['water']
# LIES:           ['sky']
# UNVERIFIABLE:   ['fire']
groups ={
    'VERIFIED':[],
    "LIES":[],
    "UNVERIFIABLE":[]
}

# def verdict(claims, facts):
#     for key in claims | facts.keys():
#         if key in claims and key in facts:
#             if claims[key] == facts[key]:
#                 groups["VERIFIED"].append(key)
#             elif claims[key] != facts[key]:
#                 groups["LIES"].append(key)
#         else:
#             groups["UNVERIFIABLE"].append(key)
#     print(groups)


def verdict(claims, facts):
    for key in claims | facts.keys():
        if key in claims and key in facts:
            if claims[key] == facts[key]:
                groups["VERIFIED"].append(key)
            elif claims[key] != facts[key]:
                groups["LIES"].append(key)
        else:
            groups["UNVERIFIABLE"].append(key)


    print(groups)


verdict(pythonclaims, facts= facts)