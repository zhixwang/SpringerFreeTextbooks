# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:47:23 2020

@author: Zhixin
"""

import pandas as pd
import re
import wget
import os

    
books_info = pd.read_excel("Free+English+textbooks.xlsx")

for book_id in range(len(books_info)):
    # Select a book
    book = books_info.iloc[book_id]
    # Get book pdf file link
    book_url = book["DOI URL"]
    
    # Get pdf downloading link
    pdf_detail = re.findall(r'/([a-z-\d.]+)', book_url)
    book_pdf_link = "https://link.springer.com/content/pdf/" + pdf_detail[1] + r"%2F" + pdf_detail[2] + r".pdf"
    
    # Saving info
    book_name = book["Book Title"] + r"_[" + book["Author"] + r"].pdf"          # BookTitle_[BookAuthor].pdf
    
    # Download
    book_category = book[r"English Package Name"]
    if not os.path.exists(book_category):
        os.makedirs(book_category)
    download_file = wget.download(book_pdf_link, out= book_category + r"/" + book_name)
    print(download_file + " Downloaded!")