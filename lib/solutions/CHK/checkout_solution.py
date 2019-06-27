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
    sku_data = dict(A=0, B=0, C=0, D=0)
    for sku in sku_list:
        sku_data[sku] += 1

    total = 0
    total += sku_data["C"] * 20
    total += sku_data["D"] * 15

    if sku_data["A"] / 3 >= 1:
        a_bundles = math.floor(sku_data["A"]/3)
        total += a_bundles * 130
        total += (sku_data["A"] % 3) * 50
    else:
        total += sku_data["A"] * 50

    if sku_data["B"] / 2 >= 1:
        a_bundles = math.floor(sku_data["B"]/2)
        total += a_bundles * 45
        total += (sku_data["B"] % 2) * 30
    else:
        total += sku_data["B"] * 30

    return total





    

    

    

