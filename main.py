import re

def generate_simulated_ai_summary(original_text):
    """
    Simulates an AI summary, intentionally introducing a factual error
    and an omission to demonstrate potential unreliability.
    """
    # Extract some correct information from the original text
    company = re.search(r"(Acme Corp)", original_text).group(1)
    product = re.search(r"'(SuperWidget \d+)'", original_text).group(1)
    launch_date = re.search(r"on (October \d+, \d{4})", original_text).group(1)
    price = re.search(r"priced competitively at (\$\d{3,})", original_text).group(1)
    battery_life = re.search(r"battery life of (\d+ hours)", original_text).group(1)

    # Construct a summary, but intentionally introduce a factual error (RAM size)
    # and omit key details (pre-order/shipping info) to simulate AI 'hallucinations' or omissions.
    simulated_summary = (
        f"{company} announced its new {product} on {launch_date}. "
        f"It features a revolutionary quantum processor, 64GB of RAM, " # Intentional factual error: Original is 128GB
        f"and a battery life of {battery_life}. It is priced at {price}. "
        f"This is a significant upgrade from the previous model." # Omission: No mention of pre-order/shipping
    )
    return simulated_summary

def verify_summary(original_text, ai_summary):
    """
    Demonstrates a basic verification process by checking key facts
    from the AI summary against the original text.
    This highlights the need for critical thinking when using AI summaries.
    """
    print("\n--- Verification Process ---")
    print("Original Text:")
    print(original_text)
    print("\nAI Summary:")
    print(ai_summary)
    print("\n--- Discrepancies Found ---")

    found_errors = False

    # Check for RAM size consistency
    original_ram_match = re.search(r"(\d+GB of RAM)", original_text)
    summary_ram_match = re.search(r"(\d+GB of RAM)", ai_summary)
    if original_ram_match and summary_ram_match:
        original_ram = original_ram_match.group(1)
        summary_ram = summary_ram_match.group(1)
        if original_ram != summary_ram:
            # This demonstrates a factual error (hallucination) in the AI summary.
            print(f"- Factual Error: RAM size. Original: '{original_ram}', Summary: '{summary_ram}'")
            found_errors = True
        else:
            print(f"- RAM size: '{original_ram}' (Matches original)")
    elif original_ram_match and not summary_ram_match:
        print(f"- Omission: RAM size '{original_ram}' mentioned in original but not in summary.")
        found_errors = True

    # Check for pre-order/shipping details (omission)
    original_shipping_match = re.search(r"(Pre-orders start next week, on November 1st, with shipping expected in mid-December)", original_text)
    summary_shipping_match = re.search(r"(Pre-orders start|shipping expected)", ai_summary) # Check for any mention
    if original_shipping_match and not summary_shipping_match:
        # This demonstrates an omission of critical information in the AI summary.
        print(f"- Omission: Key detail about '{original_shipping_match.group(1)}' is missing from summary.")
        found_errors = True
    elif not original_shipping_match and summary_shipping_match:
        print(f"- Hallucination: Summary mentions shipping details not present in original.")
        found_errors = True
    else:
        print("- Shipping details: Present in both (requires manual comparison for full accuracy)." if original_shipping_match else "- Shipping details: Not a primary focus of this check.")

    # Check for battery life consistency
    original_battery_match = re.search(r"battery life of (\d+ hours)", original_text)
    summary_battery_match = re.search(r"battery life of (\d+ hours)", ai_summary)
    if original_battery_match and summary_battery_match:
        if original_battery_match.group(1) != summary_battery_match.group(1):
            print(f"- Factual Error: Battery life. Original: '{original_battery_match.group(1)}', Summary: '{summary_battery_match.group(1)}'")
            found_errors = True
        else:
            print(f"- Battery life: '{original_battery_match.group(1)}' (Matches original)")

    if not found_errors:
        print("No obvious factual errors or significant omissions detected by this simple check.")
        print("However, a human review is always recommended for critical information.")
    else:
        print("\n--- Action Required ---")
        print("The AI summary contains inaccuracies or omissions. Refer to the original text for correct information.")

# Main execution
if __name__ == "__main__":
    article_text = """
    Acme Corp announced its new 'SuperWidget 3000' on October 26, 2023, during its annual innovation summit.
    The SuperWidget 3000 features a revolutionary quantum processor, 128GB of RAM, and a battery life of 48 hours under heavy usage.
    It is designed for professional users requiring high performance and long endurance.
    The device is priced competitively at $999. Pre-orders start next week, on November 1st, with shipping expected in mid-December.
    The previous model, SuperWidget 2000, had only 64GB of RAM and a 24-hour battery life, making the 3000 a substantial upgrade.
    """

    # Simulate AI generating a summary
    # This function is designed to introduce a known error and omission, mirroring the article's premise.
    ai_generated_summary = generate_simulated_ai_summary(article_text)

    # Demonstrate the verification process, which is the core recommendation of the article.
    verify_summary(article_text, ai_generated_summary)
