import os
import argparse
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("--directory")
parser.add_argument("--app-name")
parser.add_argument("--image-tag")

# replace image with specified tag
def replace_deployment(directory, app_name, image_tag):
    filename = os.path.join(directory, app_name, "deployment.yaml")

    with open(filename, 'r') as file:
        deployment = yaml.safe_load(file)

    containers = deployment["spec"]["template"]["spec"]["containers"]

    l = [container for container in containers if container["name"] == app_name][0]
    l["image"] = image_tag

    print("Deployment: ", deployment)

    with open(filename, 'w') as file:
        yaml.dump(deployment, file)

if __name__ == "__main__":
    args = parser.parse_args()
    replace_deployment(args.filename, args.app_name, args.image_tag)
