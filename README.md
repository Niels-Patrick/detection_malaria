# Malaria Detection Application
Using the malaria Tensorflow dataset, this AI web application takes a cell picture in input and detects
whether the cell is infected or not.

## Setup
1. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
To run the Flask application, execute the following:
```bash
flask run.py
```

## Usage
Once on the web application:
- Click on the "choose a file" button
- Select a cell picture from a local file to upload
- Click on the "upload picture" button
- The result is displayed on the same page
