print('Welcome to Rotational speed units converter!')
print('Note that you can only convert between the same unit types (for example: rad/* to rad/*)', end="\n\n")

print('Supported units for revolutions: "rpm","rph","rpd","rpw","rps"')
print('Supported units for radians: "rad/m", "rad/h", "rad/d", "rad/w", "rad/s"')
print('Supported units for degrees: "deg/m", "deg/h", "deg/d", "deg/w", "deg/s"')
print()

si = {"rpm": 1, "rph": 0.016666666666, "rpd": 0.00069444444, "rpw": 0.00009920635, "rps": 60,
      "rad/m": 1, "rad/h": 0.016666666666, "rad/d": 0.00069444444, "rad/w": 0.00009920635, "rad/s": 60,
      "deg/m": 1, "deg/h": 0.016666666666, "deg/d": 0.00069444444, "deg/w": 0.00009920635, "deg/s": 60}


def convert(val, un_from, un_to):
    result = val * si[un_from] / si[un_to]
    return round(result, ndigits=4)


value = float(input('Enter a value: '))
unit_from = input('Enter unit you want to convert from: ')
unit_to = input('Enter unit you want to convert to: ')

template = '\n{} {} is equal to {} {}'

if (unit_from in si) and (unit_to in si):
    print(template.format(value, unit_from, convert(value, unit_from, unit_to), unit_to))
else:
    print('\nUnknown units! Please check if the units are correct!')
