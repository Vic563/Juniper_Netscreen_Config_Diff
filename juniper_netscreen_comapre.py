def parse_juniper_config(file):
    # open the config file and read its contents
    with open(file, 'r') as f:
        config = f.read()

    # create a Device object
    dev = Device()

    # load the config into the Device object
    dev.load_config(config)
    
    # access the configuration elements
    for elem in dev.rpc.get_config():
        print(elem.tag)

# get the file name from the user
file = input("Enter the path of the config file: ")

# parse the config
parse_juniper_config(file)
