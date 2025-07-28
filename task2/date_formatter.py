from dateutil import parser
from datetime import datetime

def auto_format_date(date_str: str, output_format: str) -> str:
    try:
        date_obj = parser.parse(date_str)
        return date_obj.strftime(output_format)
    except ValueError as ve:
        return f"Error: Invalid date input - {ve}"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=== Date Formatter ===")
    
    date_str = input("Enter the date (any format): ").strip()
    output_format = input("Enter desired output format (e.g. %m/%d/%Y): ").strip()
    
    # Validate output format by trying to format current date (quick check)
    try:
        datetime.now().strftime(output_format)
    except Exception:
        print("Error: Invalid output date format string.")
        return
    
    result = auto_format_date(date_str, output_format)
    print("Result:", result)

if __name__ == "__main__":
    main()
