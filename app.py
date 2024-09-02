from flask import Flask, render_template, request, redirect, url_for, flash
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.csv'):
            # Process the file here
            filename = file.filename
            # Example: file.save('path/to/save/' + filename)
            flash(f'File {filename} successfully uploaded and processed.', 'success')
            return redirect(url_for('upload'))
        else:
            flash('Please upload a valid CSV file.', 'error')
    return render_template('upload.html')

@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        if start_date and end_date:
            # Handle model training here
            # Example: start_training(start_date, end_date)
            flash('Training successfully executed.', 'success')
            return redirect(url_for('train'))
        else:
            flash('Please select both start and end dates.', 'error')
    return render_template('train.html')

@app.route('/forecast', methods=['GET', 'POST'])
def forecast():
    if request.method == 'POST':
        date = request.form.get('date')
        days = int(request.form.get('days', 0))
        if date and days and 1 <= days <= 7:
            # Perform forecast operation here
            # Example: forecast_results = perform_forecast(date, days)
            forecast_data = [
                {'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'forecast': '100'}
            ]
            csv_filename = 'forecast_results.csv'
            with open(csv_filename, 'w', newline='') as csvfile:
                fieldnames = ['DateTime', 'Forecast']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(forecast_data)

            flash('Forecast completed and results exported to CSV.', 'success')
            return redirect(url_for('results'))
        else:
            flash('Please enter a valid date and ensure days are between 1 and 7.', 'error')
    return render_template('forecast.html')

@app.route('/results')
def results():
    # Render results based on previous operations
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
