import math
import string

VALID_SKUS = list(string.ascii_uppercase)
STANDARD_SKUS = sorted(list(set(VALID_SKUS) - set(["B", "M", "Q", "S", "T", "X", "Y", "Z"])))

OFFERS = {
    "A": [50, [(5, 200), (3, 130)]],
    "C": [20, None],
    "D": [15, None],
    "E": [40, None],
    "F": [10, [(2, "F")]],
    "G": [20, None],
    "H": [10, [(10, 80), (5, 45)]],
    "I": [35, None],
    "J": [60, None],
    "K": [70, [(2, 120)]],
    "L": [90, None],
    "N": [40, None],
    "O": [10, None],
    "P": [50, [(5, 200)]],
    "R": [50, None],
    "U": [40, [(3, "U")]],
    "V": [50, [(3, 130), (2, 90)]],
    "W": [20, None]
}

def calculate_sku(sku_data, key):
    if sku_data[key] == 0:
        return 0

    offer = OFFERS[key]
    
    if offer[1] is not None and isinstance(offer[1][0][1], str):
        total = 0
        if sku_data[key] / (offer[1][0][0] + 1) >= 1:
            f_bundles = math.floor(sku_data[key]/(offer[1][0][0]+1))
            total += f_bundles * (offer[0] * offer[1][0][0])
            total += (sku_data[key] % (offer[1][0][0]+1)) * offer[0]
        else:
            total += sku_data[key] * offer[0]
        return total
    elif offer[1] is None:
        return sku_data[key] * offer[0]
    else:
        total = 0
        offer1 = offer[1][0]
        try:
            offer2 = offer[1][1]
        except IndexError:
            offer2 = [10000000]
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

def special_case(sku_data, free_trigger, trigger_amount, free_sku, free_sku_value, free_deal=None):
    """free_deal can be tuple of amount and value"""
    free_items = 0
    total = 0

    if sku_data[free_trigger] / trigger_amount >= 1:
        # for every <trigger_amount> of <free_trigger> we get a free <free_sku>
        # how many free items are we eligible for
        free_items = math.floor(sku_data[free_trigger]/trigger_amount)


    if free_deal and sku_data[free_sku] / free_deal[0] >= 1:
        deal_amount = free_deal[0]
        deal_value = free_deal[1]
        # calculate which deal is best
        a_bundles = math.floor(sku_data[free_sku]/deal_amount)
        bundle_total = 0
        bundle_total += a_bundles * deal_value
        bundle_total += (sku_data[free_sku] % deal_amount) * free_sku_value
        bundle_mod = sku_data[free_sku] % deal_amount
        if free_items > bundle_mod:
            bundle_total -= free_sku_value * bundle_mod
        else:
            bundle_total -= free_sku_value * free_items

        paid_for_items = sku_data[free_sku] - free_items
        if paid_for_items < 0:
            paid_for_items = 0
        free_total = paid_for_items * free_sku_value

        if bundle_total < free_total:
            total += bundle_total
        else:
            total += free_total
    else:
        total += sku_data[free_sku] * free_sku_value
        if free_items > 0 and sku_data[free_sku] >= free_items:
            total -= (free_items * free_sku_value)

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
    sku_data = {sku: 0 for sku in VALID_SKUS}
    for sku in sku_list:
        sku_data[sku] += 1

    total = 0
    for sku in STANDARD_SKUS:
        total += calculate_sku(sku_data, sku)

    total += special_case(sku_data, "E", 2, "B", 30, (2, 45))
    total += special_case(sku_data, "N", 3, "M", 15, None)
    total += special_case(sku_data, "R", 3, "Q", 30, (3, 80))

    return total





    

    

    

