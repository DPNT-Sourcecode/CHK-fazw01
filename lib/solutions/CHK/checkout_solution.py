import math

VALID_SKUS = ["A", "B", "C", "D", "E", "F"]

OFFERS = {
    "A": [50, [(5, 200), (3, 130)]],
    "C": [20, None],
    "D": [15, None]
}

def calculate_sku(sku_data, key):
    total = 0
    offer = OFFERS[key]
    if offer[1] is None:
        return sku_data[key] * offer[0]

    offer1 = offer[1][0]
    offer2 = offer[1][1]
    if sku_data[key] / offer1[0] >= 1:
        a_bundles = math.floor(sku_data[key]/offer1[0])
        total += a_bundles * offer1[1]
        if sku_data[key] % offer1[0] >= offer2[0]:
            mod = sku_data[key] % offer1[0]
            total += offer2[1]
            total += offer[0] * (mod - offer2[0])
        else:
            total += (sku_data[key] % offer1[0]) * offer[0]
    elif sku_data[key] / offer2[0] >= 1:
        a_bundles = math.floor(sku_data[key]/offer2[0])
        total += a_bundles * offer2[1]
        total += (sku_data[key] % offer2[0]) * offer[0]
    else:
        total += sku_data[key] * offer[0]

    return total

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """Assuming skus is a continuous string, not comma separated"""
    if not isinstance(skus, str):
        return -1

    # sort the skus, convert to list
    sku_list = sorted(skus)

    # reject any lower case chars
    for i in sku_list:
        if i not in VALID_SKUS:
            return -1

    # count skus
    sku_data = dict(A=0, B=0, C=0, D=0, E=0, F=0)
    for sku in sku_list:
        sku_data[sku] += 1

    total = 0
    total += calculate_sku(sku_data, "C")
    total += calculate_sku(sku_data, "D")
    total += sku_data["E"] * 40

    #if sku_data["A"] / 5 >= 1:
    #    a_bundles = math.floor(sku_data["A"]/5)
    #    total += a_bundles * 200
    #    if sku_data["A"] % 5 >= 3:
    #        mod = sku_data["A"] % 5
    #        total += 130
    #        total += 50 * (mod - 3)
    #    else:
    #        total += (sku_data["A"] % 5) * 50
    #elif sku_data["A"] / 3 >= 1:
    #    a_bundles = math.floor(sku_data["A"]/3)
    #    total += a_bundles * 130
    #    total += (sku_data["A"] % 3) * 50
    #else:
    #    total += sku_data["A"] * 50
    total += calculate_sku(sku_data, "A")
    free_b = 0

    if sku_data["E"] / 2 >= 1:
        # for every 2 E we get a free B
        # how many free B are we eligible for
        free_b = math.floor(sku_data["E"]/2)

    if sku_data["B"] / 2 >= 1:
        # calculate which deal is best, 2 for 45, or a free B
        a_bundles = math.floor(sku_data["B"]/2)
        bundle_total = 0
        bundle_total += a_bundles * 45
        bundle_total += (sku_data["B"] % 2) * 30
        bundle_mod = sku_data["B"] % 2
        if free_b > bundle_mod:
            bundle_total -= 30 * bundle_mod
        else:
            bundle_total -= 30 * free_b

        paid_for_b = sku_data["B"] - free_b
        if paid_for_b < 0:
            paid_for_b = 0
        free_total = paid_for_b * 30

        if bundle_total < free_total:
            total += bundle_total
        else:
            total += free_total
    else:
        total += sku_data["B"] * 30
        if free_b > 0 and sku_data["B"] >= free_b:
            total -= (free_b * 30)

    if sku_data["F"] / 3 >= 1:
        f_bundles = math.floor(sku_data["F"]/3)
        total += f_bundles * 20
        total += (sku_data["F"] % 3) * 10
    else:
        total += sku_data["F"] * 10

    return total





    

    

    





