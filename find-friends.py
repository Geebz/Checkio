def check_connection(network,first,second):
    net = list(network)
    for i in net:
        x = i.split('-')

        if first not in x:
            continue

        if first in x and second in x:
            return True

        net.remove(i)

        if x[0]==first:
            if check_connection(net,x[1],second):
                return True
        else:
            if check_connection(net,x[0],second):
                return True

        return False


if __name__ == '__main__':

    assert check_connection(

        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",

         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),

        "scout2", "scout3") == True, "Scout Brotherhood"

    assert check_connection(

        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",

         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),

        "super", "scout2") == True, "Super Scout"

    assert check_connection(

        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",

         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),

        "dr101", "sscout") == False, "I don't know any scouts."

