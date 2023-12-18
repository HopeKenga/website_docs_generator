# Website Documentation Generator

This project is an AI tool that sifts through a website and produces thorough documentation of what it does, how it does it, and what can be improved. It is implemented in Python using Django, BeautifulSoup, and Celery.

## Description

The tool consists of three main components:

1. **Web Scraper**: This component uses BeautifulSoup and requests to scrape the website and extract the HTML content.

2. **Documentation Generator**: This component parses the HTML content to identify different elements and their attributes and generates documentation based on this information.

3. **Improvement Suggester**: This component checks for common issues like missing alt tags on images, lack of meta tags for SEO, etc., and suggests improvements.

## Installation

1. Clone the repository: `git clone <repo_url>`
2. Navigate to the project directory: `cd documentation_gen`
3. Install the dependencies: `pip install -r requirements.txt`

## Usage

To run the project, use the command: `python manage.py runserver`

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)