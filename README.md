# Unpaid-Developers

# Course Data Extraction and Processing Project

This project automates the extraction of course-related information (such as subject codes, credit points, and subject names) from the course handbook PDF files, processes the data, and stores it in an Excel file. It also interacts with a MySQL database to store the extracted data. The main objective is to facilitate course comparison and subject-level analysis.

## Features
- Downloads PDF files of subjects from the course handbook.
- Extracts key course information such as subject codes, credit points, and subject names.
- Compares and stores the extracted data in a MySQL database.
- Generates detailed subject information, including links and descriptions.
- Saves the extracted and processed data into Excel files.
  
## Directory Structure

```
/project_directory
│
├── Main.py                  # Main script to control data extraction and processing
├── Extract_subject_list.py  # Handles extraction of subject list from PDF files
├── Subject_instances.py     # Manages extraction of subject-specific instances and details
├── comparision.py           # Contains comparison functions for course details
├── database.py              # Manages database connections and queries
├── pdf_download.py          # Downloads the subject PDFs from the course handbook
├── silo.py                  # Extracts subject intended learning outcomes
├── write_silo.py            # Writes the subject learning outcomes into files
└── subject_instances.txt    # Text file for storing subject instance data
```

## Installation

### Prerequisites
This project requires Python 3.x and the following libraries:

- `pdfplumber` – for extracting text from PDF files.
- `pandas` – for data manipulation and storage.
- `pymysql` – for interacting with a MySQL database.
- `selenium` – for web scraping and PDF downloading.

To install the required libraries, you can create a virtual environment and install the dependencies using the following:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can install them manually:

```bash
pip install pdfplumber pandas pymysql selenium
```

### Web Driver
You will also need the Chrome WebDriver to run Selenium. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/). Ensure that it is installed and added to your system's PATH.

## How to Run the Project

### Step 1: Clone the repository
Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/course-data-extraction.git
cd course-data-extraction
```

### Step 2: Set Up the Database
Create a MySQL database and configure the connection settings in `database.py`:

- `host`: Database host IP or URL.
- `user`: MySQL username.
- `password`: MySQL password.
- `database`: Name of the database where data will be stored.

Make sure that the database exists, or you can modify the script to create it automatically.

### Step 3: Set Up the Subject List
In the `Main.py` file, update the `courses` list with the course codes you want to extract data for:

```python
courses = ['SBCS', 'SBIT', 'SBCY']
```

Each course code corresponds to a PDF URL in the La Trobe University handbook.

### Step 4: Run the Script

Run the `Main.py` script to start the extraction process:

```bash
python Main.py
```

The script will:
1. Download the PDF for each course.
2. Extract the subject list, credit points, and subject names from the PDFs.
3. Store the extracted data in an Excel file and a MySQL database.
4. Generate links and details for each subject, and save them to text files.

### Step 5: Check Output

The extracted data will be saved in the following location:
```
/project_directory/[course_code]/[course_code].xlsx
```

Additionally, logs and detailed subject information will be saved in `.txt` files located in the respective course directories.

## Script Breakdown

### `Main.py`
- Manages the overall workflow, including:
  - Creating directories for course data.
  - Downloading PDFs if not already available.
  - Extracting course details from the PDFs.
  - Writing the results to Excel and database tables.

### `Extract_subject_list.py`
- Extracts subject codes, credit points, and subject names from the course PDFs.
- Calls external functions for comparison or further processing.

### `Subject_instances.py`
- Scrapes additional subject instance information from the La Trobe University website using Selenium.
- Writes subject-specific details such as the availability of the subject to a text file.

### `comparision.py`
- Extracts comparative details such as career opportunities, course duration, and exchange program availability from the course data.
- Stores this data in the database for further analysis.

### `database.py`
- Manages MySQL database connections and handles the storage of course and comparison data into tables.

### `pdf_download.py`
- Downloads the PDF files for course subjects using Selenium's web scraping capabilities.

### `silo.py`
- Extracts and processes the "Subject Intended Learning Outcomes" section from subject PDFs.

### `write_silo.py`
- Writes the extracted learning outcomes to text files and stores subject instances in a separate file.

## Example Output

When the `Main.py` script is executed, the following will occur:

1. A directory will be created for each course code.
2. PDFs for the course subjects will be downloaded.
3. The subject list will be extracted and saved to an Excel file (`.xlsx`).
4. The subject instance data, including career outcomes and other details, will be saved to text files.
5. The comparison data will be inserted into the MySQL database.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request. Please ensure your changes are well-documented, and follow best practices for Python coding.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Additional Notes:

1. **Database**: Ensure you have the correct permissions for accessing and modifying the MySQL database.
2. **Web Scraping**: Since the project uses Selenium for web scraping, make sure to comply with the website's terms of service regarding automated scraping.
3. **Error Handling**: You might need to handle various edge cases depending on the actual structure of the PDFs or if there are network issues during PDF downloads.

Let me know if you need further customization!
