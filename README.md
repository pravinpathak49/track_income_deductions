# Salary Tracker

A modern web application to track your salary income and deductions with a beautiful, intuitive interface.

## Features

- 📊 **Dashboard Overview**: View total income, deductions, and net in-hand amount at a glance
- 📈 **Trend Visualization**: Interactive chart showing income vs deductions over time
- 💰 **Flexible Deductions**: Add custom deduction categories (tax, insurance, retirement, etc.)
- ✏️ **Easy Management**: Add, edit, and delete salary entries
- 🎨 **Modern UI**: Clean, responsive design with smooth animations

## Screenshots

![Dashboard](screenshots/dashboard.png)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/salary-tracker.git
cd salary-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5001`

## Usage

1. **Add Entry**: Click "Add New Entry" to record a new salary payment
2. **Add Deductions**: Use the "Add Deduction" button to add multiple deduction categories
3. **View Dashboard**: See your financial summary and trends on the main page
4. **Edit/Delete**: Manage existing entries from the table

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Charts**: Chart.js

## Project Structure

```
salary-tracker/
├── app.py              # Flask application
├── database.py         # Database operations
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   └── edit.html
├── static/             # Static assets
│   ├── style.css
│   └── script.js
└── requirements.txt    # Python dependencies
```

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
