import yaml
import pprint


def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        # data = yaml.load(file_descriptor, Loader=yaml.FullLoader)
        data = yaml.full_load(file_descriptor)
    return data


def yaml_dump(filepath, data):
    """Dumps data to a yaml file"""
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)


if __name__ == "__main__":
    file_path = "test.yaml"
    data = yaml_loader(file_path)
    # print(data["weapons"])
    pp = pprint.PrettyPrinter(indent=6, depth=1)
    pp.pprint(data)
    pp = pprint.PrettyPrinter(indent=6, depth=2)
    pp.pprint(data)
    pp = pprint.PrettyPrinter(indent=6, depth=3)
    pp.pprint(data)
