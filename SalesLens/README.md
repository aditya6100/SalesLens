
# SalesLens: Retail Sales Data Analysis

A comprehensive data analysis project to analyze retail sales data, identify trends, and gain actionable insights into business performance. This project is designed to be a portfolio-ready showcase for data analysis skills.

<p align="center">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Project Status" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License" />
</p>

---

## 🚀 Features

- **Data Generation**: Creates a realistic, synthetic sales dataset.
- **Data Cleaning**: Handles missing values and removes duplicates to ensure data quality.
- **Feature Engineering**: Derives new features like `total_amount`, `month`, and `year` for deeper analysis.
- **Exploratory Data Analysis (EDA)**: Answers key business questions through data exploration.
- **Interactive Visualizations**: Generates plots for monthly revenue, top cities, best-selling products, and category-wise sales.

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy" />
  <img src="https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter" />
</p>

---

## 📂 Folder Structure

```
└───SalesLens/
    ├───generate_data.py
    ├───README.md
    ├───sales_data.csv
    └───SalesLens.ipynb
```

---

## 📸 Screenshots

Here are some example visualizations from the analysis:

| Monthly Revenue Trend | Top 5 Cities by Revenue |
| :---: | :---: |
| ![Monthly Revenue Trend](/screenshots/monthly_revenue.png) | ![Top Cities](/screenshots/top_cities.png) |

| Category-wise Sales Distribution |
| :---: |
| ![Category-wise Sales Distribution](/screenshots/category_sales.png) |

---

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/aditya6100/SalesLens.git
    cd SalesLens
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install pandas numpy matplotlib seaborn jupyter
    ```

---

## 🚀 How to Run the Project

1.  **Generate the dataset:**
    Run the script to create the `sales_data.csv` file.
    ```bash
    python generate_data.py
    ```

2.  **Launch Jupyter Notebook:**
    Start the Jupyter server from your terminal.
    ```bash
    jupyter notebook
    ```

3.  **Run the analysis:**
    Open the `SalesLens.ipynb` notebook in the Jupyter interface and execute the cells sequentially to see the full analysis.

---

## 🌊 Data Flow (Architecture)

The project follows a simple, linear data flow:

```mermaid
graph TD;
    A[Data Generation <br> `generate_data.py`] --> B[Raw Data <br> `sales_data.csv`];
    B --> C[Jupyter Notebook <br> `SalesLens.ipynb`];
    C --> D{Data Cleaning & <br> Preprocessing};
    D --> E{Feature Engineering};
    E --> F{Exploratory Data Analysis};
    F --> G[Data Visualizations <br> (Charts & Plots)];
    G --> H[Actionable Insights];
```

---

## 💡 Use Cases

This project can be adapted for various analytical purposes:
- **Business Performance Reporting**: Create automated sales reports for stakeholders.
- **Inventory Management**: Identify which products to stock based on sales data.
- **Marketing Strategy**: Target high-value cities and customer segments.
- **Financial Forecasting**: Use historical trends to predict future sales.

---

## 🔮 Future Enhancements

- **Interactive Dashboard**: Build an interactive dashboard using Plotly or Dash.
- **Advanced Analytics**: Implement time-series forecasting to predict future sales.
- **Cloud Deployment**: Deploy the analysis pipeline on a cloud platform like AWS or Azure.
- **Database Integration**: Store and query data from a SQL database like PostgreSQL.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/aditya6100/SalesLens/issues).

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
