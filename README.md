# Clothing Size Matcher

## Overview
The Clothing Size Matcher is a web application that allows users to input their dimensions and search for clothing items that match their size and description. The project is structured with a frontend built using HTML, CSS, and JavaScript, and a backend developed in Python.

## Project Structure
```
clothing-size-matcher
├── src
│   ├── frontend
│   │   ├── index.html       # Main HTML document for the website
│   │   ├── styles.css       # CSS styles for the website
│   │   └── script.js        # JavaScript for handling user interactions
│   └── backend
│       ├── app.py           # Main entry point for the backend application
│       ├── search.py        # Functions for processing user input and searching for clothing
│       ├── crawler.py       # Future integration for web crawling
│       └── requirements.txt  # Python dependencies for the backend
├── .gitignore               # Files and directories to ignore in version control
└── README.md                # Documentation for the project
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd clothing-size-matcher
   ```

2. **Set up the backend**:
   - Navigate to the `src/backend` directory.
   - Create a virtual environment:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```
       source venv/bin/activate
       ```
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```

3. **Run the backend server**:
   ```
   python app.py
   ```

4. **Open the frontend**:
   - Open `src/frontend/index.html` in a web browser to access the application.

## Usage Guidelines
- Enter your dimensions in the provided input fields.
- Click the search button to find clothing items that match your size and description.
- The application will communicate with the backend to process your request and return results.

## Future Plans
- Integrate a web crawler in `crawler.py` to scrape clothing data from various websites based on user input.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.