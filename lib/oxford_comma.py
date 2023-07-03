def oxford_comma(items):
    if ( len(items) == 1 ):
        return (items[0])
    if ( len(items) == 2 ):
        return (f"{items[0]} and {items[1]}")
    items_formatted = ''
    for i in range (len(items)):
        if ( i == len(items) - 1):
            items_formatted += (f"and {items[i]}")
        else:
            items_formatted += (f"{items[i]}, ")
    return items_formatted
