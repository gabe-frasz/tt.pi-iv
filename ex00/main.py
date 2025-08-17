from convert import convert
import utils

print("--- Conversor de Medidas ---")

input_unit = utils.get_unit_choice("Digite o número da medida que quer converter:")
input_value = utils.get_float_value("Digite o valor a ser convertido: ")
output_unit = utils.get_unit_choice("Digite o número da medida para a qual quer converter:")

result = convert(input_value, input_unit, output_unit)

print("\n--- Resultado ---")
print(f"{input_value:.4f} {str(input_unit)} = {result:.4f} {str(output_unit)}")
print("-----------------")

