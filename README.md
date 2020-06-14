# ShopBot

![](amazon-web-scraping-data-extraction.png)
* A script to generate a .csv file containing details about the bestselling product of a given type from Amazon.com.
* This script uses Selenium which is one of the most widely used framework for testing web applications. It scrapes the Amazon.com website and fetches the best selling product of the given category and adds the deail to a .csv file.
* It then sends a mail to the user after updating the spreadsheet.
## Installation
1. Clone this repo

```
git clone https://github.com/syedsharjil/ShopBot.git

```
2. Installing dependencie/libraries
* Geckodriver for Firefox- The geckodriver can be downloaded from [here](https://github.com/mozilla/geckodriver/releases).

* BeautifulSoup- It is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing   Pythonic idioms for iterating, searching, and modifying the parse tree. It can be installed in the following way.

```
$ pip install beautifulsoup4
```

## Running the script
After installing all the libraries and dependencies. The product_price.py can be run directly in any IDE of your choice or through the shell.

```
$ python3 product_price.py 
```
