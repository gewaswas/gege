# @Kyle.Exotics Reptile Morph Calculator
def reptile_morph_calculator():
    
    print("=== Reptile Morph Calculator ===")
    print("This tool helps you calculate potential offspring morphs from parent reptiles.\n")
    
    
    species = ""
    morph_prices = {}  
    possible_morphs = []  
    
    
    species = input("Enter the reptile species (e.g., Ball Python, Leopard Gecko): ").strip()
    
    
    if "ball python" in species.lower():
        possible_morphs = ["Normal", "Albino", "Piebald", "Pastel", "Spider", "Clown", "Banana"]
        base_price = 5000.0  # float data type
    elif "leopard gecko" in species.lower():
        possible_morphs = ["Normal", "Tangerine", "Hypo", "Super Hypo", "Albino", "Blizzard"]
        base_price = 2000.0
    else:
        possible_morphs = ["Normal", "Albino", "Patternless", "Wild Type"]
        base_price = 1500.0
    
    
    print(f"\nAvailable morphs for {species}:")
    for i, morph in enumerate(possible_morphs, 1):
        print(f"{i}. {morph}")
        
        morph_prices[morph] = base_price * (1 + (i * 0.5))  
    
    
    parent1 = ""
    parent2 = ""
    
    while parent1 not in possible_morphs:
        parent1 = input("\nEnter morph for Parent 1: ").strip().title()
        if parent1 not in possible_morphs:
            print("Invalid morph. Please choose from the list above.")
    
    while parent2 not in possible_morphs:
        parent2 = input("Enter morph for Parent 2: ").strip().title()
        if parent2 not in possible_morphs:
            print("Invalid morph. Please choose from the list above.")
    
   
    print("\nCalculating possible offspring morphs...")
    
    
    offspring_morphs = set()  
    
    
    if parent1 == parent2:
        offspring_morphs.add(parent1)
        if parent1 != "Normal":
            offspring_morphs.add("Normal")  
    else:
        offspring_morphs.add(parent1)
        offspring_morphs.add(parent2)
        offspring_morphs.add("Normal")  
    
    
    if ("Albino" in [parent1, parent2]) and ("Piebald" in [parent1, parent2]) and "Ball Python" in species:
        offspring_morphs.add("Albino Piebald")  # Special combo
    
    # Display results
    print("\n=== Possible Offspring Morphs ===")
    for morph in sorted(offspring_morphs):
        price = morph_prices.get(morph, base_price)
        print(f"- {morph} (Estimated value: ₱{price:.2f})")
    
    # Calculate average value
    if offspring_morphs:
        avg_value = sum(morph_prices.get(m, base_price) for m in offspring_morphs) / len(offspring_morphs)
        print(f"\nAverage offspring value: ₱{avg_value:.2f}")
    

    print("\nCalculation complete! Would you like to save these results?")
    save_choice = input("(YES/NO): ").strip().upper()
    if save_choice == 'YES':
        
        print("Results saved to breeding history!")
    
    print("\nThank you for using the Reptile Morph Calculator!")

# Run the program
if __name__ == "__main__":
    reptile_morph_calculator()