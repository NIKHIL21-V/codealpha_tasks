import re
import os


def extract_emails(input_file, output_file):
    try:
        # Check whether the input file exists
        if not os.path.exists(input_file):
            print(f"Error: '{input_file}' was not found.")
            return

        # Read the input text file
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Extract email addresses using a regular expression
        emails = re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            text
        )

        # Remove duplicate email addresses
        unique_emails = sorted(set(emails), key=str.lower)

        # Save the extracted email addresses
        with open(output_file, "w", encoding="utf-8") as file:
            for email in unique_emails:
                file.write(email + "\n")

        print("\n========== EMAIL EXTRACTION REPORT ==========")
        print(f"Email addresses found: {len(emails)}")
        print(f"Unique email addresses: {len(unique_emails)}")
        print(f"Results saved to: {output_file}")
        print("==============================================")

        if not unique_emails:
            print("No email addresses were found in the input file.")

    except OSError as error:
        print(f"File error: {error}")


def main():
    print("===================================")
    print("     PYTHON EMAIL EXTRACTOR")
    print("       CodeAlpha Task 3")
    print("===================================")

    input_file = input("Enter the input text filename (default: input.txt): ").strip()

    if not input_file:
        input_file = "input.txt"

    output_file = input(
        "Enter the output filename (default: extracted_emails.txt): "
    ).strip()

    if not output_file:
        output_file = "extracted_emails.txt"

    extract_emails(input_file, output_file)


if __name__ == "__main__":
    main()