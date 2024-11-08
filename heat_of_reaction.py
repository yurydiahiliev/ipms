import argparse
import json

def calculate_heat_of_reaction(enthalpies, coefficients_reactants, coefficients_products):
    reactants_heat = sum(
        coefficients_reactants[reactant] * enthalpies.get(reactant, 0) for reactant in coefficients_reactants)

    products_heat = sum(
        coefficients_products[product] * enthalpies.get(product, 0) for product in coefficients_products)

    heat_of_reaction = products_heat - reactants_heat
    return heat_of_reaction

def main():
    parser = argparse.ArgumentParser(description="Calculate heat of reaction for a given chemical reaction.")
    parser.add_argument('--enthalpies', type=str, required=True,
                        help="JSON string for enthalpies of elements (e.g. '{\"KNO3\": -494.6, \"S\": 0, \"C\": 0, \"N2\": 0, \"CO2\": -393.5, \"K2S\": -248.5}')")
    parser.add_argument('--reactants', type=str, required=True,
                        help="JSON string for reactant coefficients (e.g. '{\"KNO3\": 2, \"S\": 1, \"C\": 3}')")
    parser.add_argument('--products', type=str, required=True,
                        help="JSON string for product coefficients (e.g. '{\"N2\": 1, \"CO2\": 3, \"K2S\": 1}')")
    args = parser.parse_args()

    enthalpies = json.loads(args.enthalpies)
    coefficients_reactants = json.loads(args.reactants)
    coefficients_products = json.loads(args.products)

    heat = calculate_heat_of_reaction(enthalpies, coefficients_reactants, coefficients_products)
    print(f"Тепловий ефект реакції: {heat:.2f} кДж/моль")

if __name__ == "__main__":
    main()