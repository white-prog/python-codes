#Define functions that return everything to byte
def toByte(data_size,data_type):
    #we can use dictionary instead then programme become more efficient we don't need to use loop then
    list_of_bytes = [
    ('KB', 1024),
    ('MB', 1048576),
    ('GB', 1073741824),
    ('TB', 1099511627776),
    ('PB', 1125899906842624),
    ('EB', 1152921504606846976),
    ('ZB', 1180591620717411303424),
    ('YB', 1208925819614629174706176)
    ]
    how_much = 0
    for i in list_of_bytes:
        if i[0] == data_type.upper():
            how_much = i[1]
            break

    return str(data_size * how_much) + " bytes"
first = toByte(2,'kb')
print(first)
