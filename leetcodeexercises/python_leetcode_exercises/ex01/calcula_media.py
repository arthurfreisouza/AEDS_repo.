def media(lst):
    media_value = 0
    for i in range(len(lst)):
        media_value = media_value + lst[i]

    media_value = media_value / len(lst)
    print(" The type is : {}".format(type(media_value)))
    return media_value