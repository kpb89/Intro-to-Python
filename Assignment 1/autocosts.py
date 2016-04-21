loan_payment = float(input('Please enter the amount you pay for loan in the form xx.yy: '))
loan_per_year = int(input('Please enter how many times per year you pay: '))
loan_total = loan_payment * loan_per_year
loan_total_str = '{:,.2f}'.format(loan_total)
print('$',loan_total_str,sep ='')

insurance_payment = float(input('Please enter the amount you pay for insurance in the form xx.yy: '))
insurance_per_year = int(input('Please enter how many times per year you pay: '))
insurance_total = insurance_payment * insurance_per_year
insurance_total_str = '{:,.2f}'.format(insurance_total)
print('$',insurance_total_str,sep ='')

gas_payment = float(input('Please enter the amount you pay for gas in the form xx.yy: '))
gas_per_year = int(input('Please enter how many times per year you pay: '))
gas_total = gas_payment * gas_per_year
gas_total_str = '{:,.2f}'.format(gas_total)
print('$',gas_total_str,sep='')

oil_payment = float(input('Please enter the amount you pay for oil in the form xx.yy: '))
oil_per_year = int(input('Please enter how many times per year you pay: '))
oil_total = oil_payment * oil_per_year
oil_total_str = '{:,.2f}'.format(oil_total)
print('$',oil_total_str,sep='')

maintenance_payment = float(input('Please enter the amount you pay for maintenance in the form xx.yy: '))
maintenance_per_year = int(input('Please enter how many times per year you pay: '))
maintenance_total = maintenance_payment * maintenance_per_year
maintenance_total_str = '{:,.2f}'.format(maintenance_total)
print('$',maintenance_total_str,sep='')


total_cost = loan_total + insurance_total + gas_total + oil_total + maintenance_total
total_cost_str = '{:,.2f}'.format(total_cost)
print('The total yearly cost is $',total_cost_str,sep='')


monthly_cost = total_cost / 12
monthly_cost_str = '{:,.2f}'.format(monthly_cost)
print('The total monthly cost is $',monthly_cost_str,sep='')
