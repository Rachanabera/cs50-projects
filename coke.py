def main():
    # Initialize the amount due and the total inserted
    amount_due = 50
    total_inserted = 0

    # Loop until the user has inserted enough coins
    while total_inserted < amount_due:
        # Prompt the user to insert a coin
        coin = int(input("Insert Coin: "))

        # Check if the coin is valid (25, 10, or 5 cents)
        if coin == 25 or coin == 10 or coin == 5:
            total_inserted += coin
        else:
            # If the coin is invalid, continue to the next loop without modifying total_inserted
            print(f"Amount Due: {amount_due - total_inserted}")
            continue  # Skip the current iteration and prompt for another coin

        # Output the remaining amount due if it's still less than 50
        if total_inserted < amount_due:
            print(f"Amount Due: {amount_due - total_inserted}")

    # Calculate the change owed
    change_owed = total_inserted - amount_due
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
