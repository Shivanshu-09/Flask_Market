from market import app

# Check if the run.py file has run directly and not imported
if __name__ == '__main__':
    app.run(debug=True)