import pandas as pd

def calculate_compound_interest(principal, outstanding_amount, interest_rate_per_month, months_pending, monthly_installment):
    """Calculates compound interest, considering monthly installments.

    Args:
        principal: The initial principal amount.
        outstanding_amount: The current outstanding amount.
        interest_rate_per_month: The monthly interest rate (as a decimal).
        months_pending: The number of months for which interest is calculated.
        monthly_installment: The fixed monthly installment amount.

    Returns:
        A dictionary containing the original principal, outstanding amount, total interest, and final amount.
    """

    final_amount = outstanding_amount  # Start with the outstanding amount
    total_interest = 0

    for _ in range(months_pending):
        interest_for_month = final_amount * interest_rate_per_month
        total_interest += interest_for_month
        final_amount -= monthly_installment  # Add interest, subtract installment

        if final_amount < 0:  # Ensure it doesn't go negative (loan paid off)
            final_amount = 0
            break

    return {
        "principal": principal,
        "outstanding_amount": outstanding_amount,
        "total_interest": total_interest,
        "final_amount": final_amount
    }

def process_customer_data(input_excel_file, output_excel_file):
    """Processes customer data from an input Excel file and saves results to an output Excel file.

    Args:
        input_excel_file: Path to the input Excel file.
        output_excel_file: Path to the output Excel file.
    """
    try:
        df = pd.read_excel(input_excel_file)

        results = []
        for index, row in df.iterrows():
            principal = row['Principal']
            outstanding_amount = row['OutstandingAmount']
            months_pending = row['MonthsPending']
            monthly_installment = row['MonthlyInstallment']  # Get monthly installment from Excel
            interest_rate_per_month = 0.14  # 14% annual interest, converted to monthly

            interest_data = calculate_compound_interest(principal, outstanding_amount, interest_rate_per_month, months_pending, monthly_installment)
            results.append({
                'CustomerID': row['CustomerID'],
                'Principal': principal,
                'OutstandingAmount': outstanding_amount,
                'MonthsPending': months_pending,
                'MonthlyInstallment': monthly_installment,
                'TotalInterest': interest_data['total_interest'],
                'FinalAmount': interest_data['final_amount']
            })

        results_df = pd.DataFrame(results)
        results_df.to_excel(output_excel_file, index=False)
        print(f"Successfully processed data and saved to {output_excel_file}")

    except FileNotFoundError:
        raise Exception(f"Input file '{input_excel_file}' not found.")
    except KeyError as e:
        raise Exception(f"Column '{e}' not found in the Excel file. Check column names.")
    except TypeError as e:
        raise Exception(f"Data Type mismatch: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")