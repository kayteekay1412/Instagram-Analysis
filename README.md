# Instagram Analysis

## Description
This is a simple Python script for analyzing an Instagram profile's posts, specifically extracting and visualizing data related to captions, likes, and comments. The script uses the Instaloader library to scrape data from a given Instagram profile and then generates histograms for likes and comments.

## Usage

1. Install the required packages using pip:

```bash
pip install instaloader pandas matplotlib
```

2. Clone this repository:

```bash
git clone https://github.com/kayteekay1412/Instagram-Analysis.git
```

3. Navigate to the project directory:

```bash
cd Instagram-Analysis
```

4. Run the script `insta-analysis.py` by providing the Instagram username of the profile you want to analyze. Replace `then0t0ri0usvip` with the desired username.

```bash
python insta-analysis.py
```

## Script Details

### Code File
- Code Name: `insta-analysis.py`

### Required Libraries
- [Instaloader](https://instaloader.github.io/): A Python library for downloading and analyzing Instagram content.
- [Pandas](https://pandas.pydata.org/): A powerful data manipulation and analysis library.
- [Matplotlib](https://matplotlib.org/): A popular plotting library for creating visualizations.

### Code Explanation
- The script takes an Instagram username as input and scrapes data from the user's posts.
- It collects captions, likes, and comments for each post and stores them in separate lists.
- The data is then structured in a Pandas DataFrame for easy analysis.
- Two histograms are generated and displayed using Matplotlib to visualize the distribution of likes and comments.

### Output
- The scraped data is saved to a CSV file named `<username>_instagram_data.csv`.
- Two histograms are displayed, showing the distribution of likes and comments.
- A message is printed indicating where the data has been saved.

## Example
```python
python insta-analysis.py
```

Feel free to contribute to this project or use the code for your own Instagram analysis needs. If you encounter any issues or have suggestions for improvements, please create an issue or pull request. Enjoy analyzing Instagram data with this simple script!
