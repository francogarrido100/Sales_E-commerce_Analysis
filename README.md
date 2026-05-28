# 📦 E-commerce Sales & Inventory Analysis

End-to-end data analytics project covering cleaning, processing, and analysis of e-commerce sales and inventory data using Python and Pandas — with a Looker Studio dashboard in progress.

---

## 🗂️ Datasets Used

| File | Description |
|------|-------------|
| `Sale_Report.csv` | Main inventory report: SKU, stock levels, category, size, color |
| `Amazon_Sale_Report.csv` | Amazon India orders: status, fulfilment, city, state, revenue (INR) |
| `International_sale_Report.csv` | International B2B orders: customer, SKU, quantity, rate |
| `P__L_March_2021.csv` | Product pricing across platforms: Ajio, Amazon, Flipkart, Myntra |
| `May-2022.csv` | May 2022 pricing snapshot with transfer prices and MRPs |
| `Expense_IIGF.csv` | Operational expense log |

---

## 🛠️ Project Phases

### Phase 1 — Pipeline Automation (`analysis.py`)
Lightweight Python script to ingest raw inventory data, filter key operational columns, and export a clean Excel file ready for reporting.

- Reads `Sale_Report.csv`
- Keeps: `SKU Code`, `Design No.`, `Stock`, `Category`, `Size`, `Color`
- Exports `Sales_Report_Clean.xlsx`

### Phase 2 — Deep Cleaning & EDA (`eda_sales_analysis.ipynb`)
Jupyter Notebook with advanced data quality checks and exploratory analysis across all datasets.

- Removed 62 rows with `#REF!` formula errors in SKU column
- Removed duplicate records
- Standardized categorical variables (color names, casing)
- Imputed missing values with explicit `UNKNOWN` flags
- Stock distribution analysis by category and color
- Revenue analysis by state and fulfilment channel (Amazon dataset)

### Phase 3 — Dashboard (In Progress)
Interactive Looker Studio dashboard connecting the cleaned datasets to track:
- Stock levels by category and size
- Revenue by region and sales channel
- Order status breakdown (Shipped / Cancelled / Returned)

---

## 📁 Repository Structure

```
Sales_E-commerce_Analysis/
│
├── data/                        # Raw source files (not tracked by git)
│   ├── Sale_Report.csv
│   ├── Amazon_Sale_Report.csv
│   └── ...
│
├── analysis.py                  # Phase 1: automation pipeline
├── eda_sales_analysis.ipynb     # Phase 2: cleaning & EDA
├── requirements.txt             # Python dependencies
└── README.md
```

---

## ⚙️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/francogarrido100/Sales_E-commerce_Analysis.git
cd Sales_E-commerce_Analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the pipeline script
python analysis.py

# 4. Open the notebook
jupyter notebook eda_sales_analysis.ipynb
```

---

## 🧰 Tech Stack

- **Python 3.11** — core language
- **Pandas** — data manipulation and cleaning
- **Matplotlib / Seaborn** — visualizations
- **OpenPyXL** — Excel export
- **Jupyter Notebooks** — exploratory analysis
- **Looker Studio** — dashboard (in progress)
- **VS Code** — development environment

---

## 👤 Author

**Franco Garrido**  
Data Analyst · Buenos Aires, Argentina  
[GitHub](https://github.com/francogarrido100)
[LinkedIn] (www.linkedin.com/in/franco-garrido)
