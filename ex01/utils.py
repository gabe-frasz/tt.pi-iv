from convert import NAME_TO_PT, Unit

def get_unit_choice(prompt_message: str) -> Unit:
  units_list = list(Unit)

  options_str = "\n".join([
      f"{i} - {NAME_TO_PT.get(unit.name)} ({str(unit)})"
      for i, unit in enumerate(units_list, start=1)
  ])
  full_prompt = f"{prompt_message}\n{options_str}\n"

  while True:
    choice = int(input(full_prompt))

    if 1 <= choice <= len(units_list):
      return units_list[choice - 1]


def get_float_value(prompt_message: str) -> float:
  escapedInputValue = input(prompt_message).replace(",", ".")
  return float(escapedInputValue)

