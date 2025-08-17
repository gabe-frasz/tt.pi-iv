from enum import Enum

NAME_TO_SYMBOL = {
  "METER": "m",
  "FOOT": "ft",
  "YARD": "yd"
}

NAME_TO_PT = {
  "METER": "METRO",
  "FOOT": "PÉ",
  "YARD": "JARDA"
}

class Unit(Enum):
  # each enum value is its equivalent in meters
  METER = 1.0
  FOOT = 0.3048
  YARD = 0.9144

  def __str__(self):
    return NAME_TO_SYMBOL.get(self.name, "?")

def convert(value: float, input_unit: Unit, output_unit: Unit) -> float:
  if input_unit == output_unit:
    return value

  # fist convert to meters
  input_in_meters = value * input_unit.value

  # then convert to the ouput unit
  return input_in_meters / output_unit.value

