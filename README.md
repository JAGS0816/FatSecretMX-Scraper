# Fat Secret Scrapy Crawler

This project uses Scrapy in Python to extract nutritional information from foods on the Fatsecret Mexico website.

## Project Description

The crawler is designed to retrieve data on calories, carbohydrates, fats, proteins, and sodium from specific foods on the Fatsecret Mexico website.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/YOUR_USERNAME/your-repository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repository
   ```

3. Install dependencies using pip and the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Scrapy spider to obtain nutritional data. Make sure Scrapy is installed.

```bash
scrapy runspider Fat_secret_scrapper.py -o Fat_secret_nut_values.csv
```

## Project Structure

- `Fat_secret_scrapper.py`: Contains the source code of the spider and extraction logic.
- `requirements.txt`: List of project dependencies.
- `README.md`: This file, providing information about the project.

## Spider Configuration

- `name`: "Fat_Secret"
- `custom_settings`: Custom settings such as export encoding and user agent.
- `download_delay`: Delay in requests to avoid scraping detection.
- `allowed_domains`: Allowed domains for the spider.
- `start_urls`: Initial URL to start the extraction.

## Additional Notes

- The code uses a custom processor to clean numbers.
- Ensure compliance with the website's policies when performing scraping.

## Contributions

Contributions are welcome! If you find improvements or issues, please create an issue or send a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
