def to_meters(feet, inches):
    feet_to_meters = feet * 0.3048
    inches_to_meters = inches * 0.0254
    return feet_to_meters + inches_to_meters


if __name__ == '__main__':
    print(to_meters(3, 4))