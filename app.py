from flask import Flask, render_template, request, redirect, url_for, jsonify
import database
import json
from datetime import datetime

app = Flask(__name__)

# Initialize database
database.init_db()

@app.route('/')
def index():
    entries = database.get_all_entries()
    
    # Calculate summaries
    total_income = sum(e['income'] for e in entries)
    total_in_hand = sum(e['in_hand'] for e in entries)
    total_deductions = total_income - total_in_hand # Or sum from deductions if we want to be precise, but this is safer for consistency
    
    deduction_percentage = 0
    if total_income > 0:
        deduction_percentage = (total_deductions / total_income) * 100

    return render_template('index.html', entries=entries, 
                           total_income=total_income, 
                           total_in_hand=total_in_hand, 
                           total_deductions=total_deductions,
                           deduction_percentage=deduction_percentage)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date = request.form['date']
        income = float(request.form['income'])
        
        # Process flexible deductions
        deduction_names = request.form.getlist('deduction_name[]')
        deduction_amounts = request.form.getlist('deduction_amount[]')
        
        deductions = []
        total_deductions_amount = 0
        
        for name, amount in zip(deduction_names, deduction_amounts):
            if name and amount:
                amt = float(amount)
                deductions.append({'name': name, 'amount': amt})
                total_deductions_amount += amt
        
        # Calculate in-hand if not provided (or verify it)
        # For this app, let's trust the user's input for in-hand or calculate it?
        # The prompt says "user will submit... total in-hand received".
        # So we take it from input.
        in_hand = float(request.form['in_hand'])
        
        database.add_entry(date, income, deductions, in_hand)
        return redirect(url_for('index'))
    
    return render_template('add.html', today=datetime.now().strftime('%Y-%m-%d'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    entry = database.get_entry(id)
    if not entry:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        date = request.form['date']
        income = float(request.form['income'])
        
        # Process flexible deductions
        deduction_names = request.form.getlist('deduction_name[]')
        deduction_amounts = request.form.getlist('deduction_amount[]')
        
        deductions = []
        total_deductions_amount = 0
        
        for name, amount in zip(deduction_names, deduction_amounts):
            if name and amount:
                amt = float(amount)
                deductions.append({'name': name, 'amount': amt})
                total_deductions_amount += amt
        
        in_hand = float(request.form['in_hand'])
        
        database.update_entry(id, date, income, deductions, in_hand)
        return redirect(url_for('index'))
    
    return render_template('edit.html', entry=entry)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    database.delete_entry(id)
    return redirect(url_for('index'))

@app.route('/api/data')
def api_data():
    entries = database.get_all_entries()
    return jsonify(entries)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
