VALID_SKUS = ["A", "B", "C", "D"]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """Assuming skus is a continuous string, not comma separated"""
    if not isinstance(skus, str):
        return -1

    # sort the skus, convert to list
    sku_list = sorted(skus)
    
    # remove any blank entries
    sku_list = [i for i in sku_list if i.strip() != ""]

    # validate skus
    sku_list = [i.upper() for i in sku_list if i.upper() in VALID_SKUS]

    # count skus
    sku_data = dict(A=0, B=0, C=0, D=0)
    for sku in sku_list:
        sku_data[sku] += 1

    total = 0
    total += sku_data["C"] * 20
    total += sku_data["D"] * 15

    




    

    

    


