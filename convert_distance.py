def convert_distance(miles):
  km = miles * 1.6
  result = "{} miles equals {:.1f} km".format(miles,km) #{:.1f} is for how many decimal places
  return result

print(convert_distance(14))
