employee_name = str(input("Enter employee's name: "))
hours_worked = float(input("Enter number of hours worked in a week: "))
month_worked = input("Enter month worked: ")
hourly_payrate = float(input("Enter hourly pay rate: "))
federaltax_withholdingrate = float(input("Enter Federal tax withholding rate: "))
statetax_withholdingrate = float(input("Enter state tax withholding: "))

gross_pay = hours_worked * hourly_payrate
federalwithholding_percentage = (federaltax_withholdingrate / 100) * gross_pay
statewithholding_percentage = (statetax_withholdingrate / 100) * gross_pay
total_deduction = federalwithholding_percentage + statewithholding_percentage
net_pay = gross_pay - total_deduction
print( )
print(f"""===============================================================================================
=   Super Mart Payroll statement for the month of {month_worked}                     =
===============================================================================================
=                                                                                             =
= Employee name: {employee_name:<70}                             =
= Hours worked: {hours_worked:<74}                                =
= Pay rate: ${hourly_payrate:<71}                                =
= Gross pay: ${gross_pay:<71}                                  =
= Deductions:                                                                                =
=   Federal withholding {federalwithholding_percentage}%: ${federal_withholding:.2f}         =
=   State withholding {statewithholding_percentage}%: ${state_withholding:.2f}             =
=   Total Deduction: ${total_deduction:<65}                      =
= Net pay: ${net_pay:<75}                                     =
===============================================================================================""")




