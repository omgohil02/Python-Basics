#Currency Note Counter in python 

try:
    amount = int(input("Enter amount in rupees: "))
    
    # Validation: Positive integer and multiple of 10
    if amount <= 0 or amount % 10 != 0:
        print("Error: Amount must be a positive multiple of 10.")
    else:
        denominations = [2000, 500, 200, 100, 50, 20, 10]
        notes_breakdown = []
        total_notes = 0
        
        remaining_amount = amount
        for denom in denominations:
            count = remaining_amount // denom
            remaining_amount %= denom
            notes_breakdown.append((denom, count))
            total_notes += count
            
        print("Breakdown:")
        for denom, count in notes_breakdown:
            print(f"{denom} x {count}")
            
        print(f"Total number of notes: {total_notes}")

except ValueError:
    print("Error: Please enter a valid integer amount.")