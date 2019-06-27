import math

VALID_SKUS = ["A", "B", "C", "D", "E"]

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
    sku_data = dict(A=0, B=0, C=0, D=0, E=0)
    for sku in sku_list:
        sku_data[sku] += 1

    total = 0
    total += sku_data["C"] * 20
    total += sku_data["D"] * 15
    total += sku_data["E"] * 40

    if sku_data["A"] / 5 >= 1:
        a_bundles = math.floor(sku_data["A"]/5)
        total += a_bundles * 200
        if sku_data["A"] % 5 >= 3:
            mod = sku_data["A"] % 5
            import pdb;pdb.set_trace()
            total += 130
            total += 50 * (mod - 3)
        else:
            total += (sku_data["A"] % 5) * 50
    elif sku_data["A"] / 3 >= 1:
        a_bundles = math.floor(sku_data["A"]/3)
        total += a_bundles * 130
        total += (sku_data["A"] % 3) * 50
    else:
        total += sku_data["A"] * 50

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

    return total





    

    

    
