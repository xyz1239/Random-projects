from typing import Optional

def get_valid_input(prompt:str, min_val:float=0, max_val:Optional[float]=None) ->float :
    while True:
        try:
            value = float(input(prompt))
            if value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def payrollcalc() -> None:
    #inputs 
    name = input("Enter employee's name: ").strip()
    hours_worked = get_valid_input("Enter number of hours worked in a week: ",0,7*24)
    pay = get_valid_input("Enter hourly pay rate: ")
    tax_rate = get_valid_input("Enter ATO tax withholding rate: ")
    medicare_rate = get_valid_input("Enter Medicare Levy rate: ")

    #calculations 
    gross_pay = round(hours_worked * pay,2)
    ato_tax = round(gross_pay * tax_rate, 2)
    medicare = round(gross_pay * medicare_rate, 2)
    total_deduction = ato_tax + medicare
    net_pay = gross_pay - total_deduction

    #outputs
    last_name = name.split()[-1]  
    print(f"\nEmployee Name: {last_name}")
    print(f"Hours Worked: {hours_worked:.1f}")
    print(f"Pay Rate: ${pay:.2f}")
    print(f"gross pay: ${gross_pay:.2f}")
    print("Deductions: ")
    print(f"ATO tax ({tax_rate * 100:.1f}%):  ${ato_tax:.2f} ")
    print(f"Medicare Levy ({medicare_rate*100:.1f}%):  ${medicare:.2f}")
    print(f"Total Deduction12: ${total_deduction:.1f}")
    print(f"Net Pay: ${net_pay:.2f}")

#runs program
payrollcalc()


