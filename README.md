# data_cleaning_project

# 🧹 Transaction Data Cleaning Script

## Overview

This project is a **Python-based data cleaning pipeline** for transactional datasets. It processes raw Excel transaction records and prepares them for analysis by:

* Standardizing product names
* Fixing invalid or missing data
* Converting negative numeric values to positive
* Validating dates and transaction states

The script ensures the dataset is **accurate, consistent, and ready for downstream analysis**.

---

## Features

1. **Load Data**

   * Reads Excel files using **Pandas**
   * Converts `Price` and `Quantity` columns to numeric types, handling errors

2. **Handle Missing Values**

   * Drops rows where critical columns (`Transaction_ID`, `Customer_ID`, `Quantity`, `Price`, `Transaction_Status`) are missing

3. **Validate Dates**

   * Converts `Transaction_Date` to `datetime` objects
   * Invalid dates are replaced with `NaT`

4. **Clean Product Names**

   * Standardizes product names to lowercase
   * Uses **fuzzy string matching** (via `SequenceMatcher`) to identify typos
   * Corrects incomplete or inconsistent names

5. **Fix Numeric Values**

   * Converts negative `Price` or `Quantity` values to positive numbers

6. **Transaction Status Cleaning**

   * Replaces `"Failed"` or `"failed"` transaction statuses with `None`

7. **Deduplication**

   * Removes duplicate rows from the dataset

---

## Usage

1. Place your Excel transaction file in a known location (update the path in `load_data()`).
2. Run the script:

```bash
python main.py
```

3. The cleaned dataset is printed to the console. You can modify the script to save it to a new Excel or CSV file:

```python
original_data.to_csv("cleaned_transactions.csv", index=False)
```

---

## Example Workflow

```python
original_data = load_data()
original_data = droping_nan(original_data, "Transaction_ID")
original_data = validate_dates(original_data)
original_data = clean_product_names(original_data)
original_data = neg_to_pos(original_data)
original_data = transaction_states_cleaning(original_data)
```

This ensures that all critical columns are cleaned, product names are standardized, and all numeric values are positive.

---

## Dependencies

* Python 3.x
* pandas
* openpyxl (for reading Excel files)
* difflib (for string similarity)
* collections (for counting most common strings)

Install dependencies via pip:

```bash
pip install pandas openpyxl
```

---

## Why This Matters

Raw transactional datasets often contain:

* Typos in product names
* Missing or invalid data
* Negative values where they shouldn't exist

This script **automates the cleaning process**, saving time and ensuring **high-quality data for analysis, reporting, or machine learning projects**.

