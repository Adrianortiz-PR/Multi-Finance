from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personal_finance', methods=['GET', 'POST'])
def personal_finance():
    if request.method == 'POST':
        user_salary = float(request.form['user_salary'])
        budget_method = request.form['budget_method']
        
        if budget_method == '50_30_20':
            necessities = user_salary * 0.5
            wants = user_salary * 0.3
            savings = user_salary * 0.2
            return render_template('personal_finance_section.html', necessities=necessities, wants=wants, savings=savings, budget_method=budget_method)
        elif budget_method == 'rule_of_25':
            rule_of_25 = user_salary * 25
            return render_template('personal_finance_section.html', rule_of_25=rule_of_25, budget_method=budget_method)
        elif budget_method == '70_20_10':
            living_expenses = user_salary * 0.7
            savings_and_investments = user_salary * 0.2
            discretionary_spending = user_salary * 0.1
            return render_template('personal_finance_section.html', living_expenses=living_expenses, savings_and_investments=savings_and_investments, discretionary_spending=discretionary_spending, budget_method=budget_method)
    
    return render_template('personal_finance_section.html')

@app.route('/banking')
def banking():
    return render_template('banking_section.html')

@app.route('/investing')
def investing():
    return render_template('investing_section.html')

if __name__ == '__main__':
    app.run()
