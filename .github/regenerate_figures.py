import os
import pandas as pd  # Assuming you're using pandas for data manipulation
import matplotlib.pyplot as plt  # Assuming you're using matplotlib for plotting
import seaborn as sns  # Assuming you're using seaborn for visualizations
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D

# Load your data (replace with your actual data loading logic)
df = pd.read_csv("your_data.csv")  # Replace with your data source and format
df_fulfillment = pd.read_csv("your_fulfillment_data.csv")  # Replace if using separate data

def regenerate_figures():

    # Calculate the top 5 products with highest inventory cost
    top_5_products_inventory_cost = df.groupby('Product Name')['Inventory Cost Per Unit'].sum().sort_values(ascending=False).head(5)

    # Extract product names and inventory cost
    product_names = top_5_products_inventory_cost.index.to_list()
    inventory_cost = top_5_products_inventory_cost.values.tolist()

    # Create a bar chart
    plt.figure(figsize=(10, 7))
    plt.bar(product_names, inventory_cost)
    plt.title("Top 5 Products with Highest Inventory Cost")
    plt.xlabel("Product Name")
    plt.ylabel("Inventory Cost")
    plt.savefig('Top 5 products with highest inventory cost.png')

    # Calculate average profit per product department
    avg_profit_by_department = df.groupby('Product Department')['Profit'].mean().sort_values(ascending=False)

    # Extract product department names and average profit
    department_names = avg_profit_by_department.index.to_list()
    avg_profit = avg_profit_by_department.values.tolist()

    # Create a bar chart
    plt.figure(figsize=(10, 7))
    plt.bar(department_names, avg_profit)
    plt.title("Average Profit by Product Department")
    plt.xlabel("Product Department")
    plt.ylabel("Average Profit")
    plt.savefig('Average Profit by Product Dept.png')

    # Calculate the inventory storage cost per product department
    storage_cost_by_department = df.groupby('Product Department')['Storage_Cost'].sum()

    # Extract product department names and storage cost
    department_names = storage_cost_by_department.index.to_list()
    storage_cost = storage_cost_by_department.values.tolist()

    # Create a bar chart
    plt.figure(figsize=(10, 7))
    plt.bar(department_names, storage_cost)
    plt.title("Inventory Storage Cost by Product Department")
    plt.xlabel("Product Department")
    plt.ylabel("Inventory Storage Cost")
    plt.savefig('Inventory Storage Cost by Prodcut Department.png')

    # the Warehouse Order Fulfillment (days) per Product Name
    fulfillment_per_product = df_fulfillment.groupby('Product Name')[' Warehouse Order Fulfillment (days) '].mean()

    plt.figure(figsize=(20,6))
    fulfillment_per_product.plot(kind='bar')
    plt.title('Average Warehouse Order Fulfillment (days) per Product Name')
    plt.xlabel('Product Name')
    plt.ylabel('Warehouse Order Fulfillment (days)')
    plt.savefig('Average Warehouse Order Fulfillment per Product Name.png')

    # Calculate the number of customers in each segment
    segment_counts = df['Customer Segment'].value_counts()

    # Extract segment labels and counts
    labels = segment_counts.index.to_list()
    counts = segment_counts.values.tolist()

    # Create a pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(counts, labels=labels, autopct="%1.1f%%")
    plt.title("Customer Segmentation")
    plt.savefig('Customer_Segmentation.png')

    # Monthly Sales Trends
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Order YearMonth', y='Gross Sales', data=df, estimator='sum', ci=None)
    plt.title('Monthly Sales Trends')
    plt.xlabel('Order YearMonth')
    plt.ylabel('Total Gross Sales')
    plt.savefig('Monthly Sales Trends.png')

    # Product Department-wise Sales
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Product Department', y='Gross Sales', data=df, estimator=sum, ci=None)
    plt.title('Product Department-wise Sales')
    plt.xlabel('Product Department')
    plt.ylabel('Total Gross Sales')
    plt.xticks(rotation=45, ha='right')
    plt.savefig('Prod Dept-wise Sales.png')

    # Customer Region-wise Sales
    plt.figure(figsize=(10, 6))
    df_region = df.groupby('Customer Region')['Gross Sales'].sum().reset_index()
    sns.barplot(x='Customer Region', y='Gross Sales', data=df_region)
    plt.title('Customer Region-wise Sales')
    plt.xlabel('Customer Region')
    plt.ylabel('Total Gross Sales')
    plt.xticks(rotation=45, ha='right')
    plt.savefig('Customer Region-wise Sales.png')

    # Discount vs. Profit
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Discount %', y='Profit', data=df)
    plt.title('Discount vs. Profit')
    plt.xlabel('Discount %')
    plt.ylabel('Profit')
    plt.savefig('Disc vs Profit.png')

    # Distribution of Order Quantity
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Order Quantity'], bins=20, kde=True)
    plt.title('Distribution of Order Quantity')
    plt.xlabel('Order Quantity')
    plt.ylabel('Frequency')
    plt.savefig('Difstribution of ORder Quantity.png')

    # Top Products by Gross Sales
    top_products = df.groupby('Product Name')['Gross Sales'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    top_products.plot(kind='barh')
    plt.title('Top 10 Products by Gross Sales')
    plt.xlabel('Total Gross Sales')
    plt.ylabel('Product Name')
    plt.gca().invert_yaxis()  # Invert y-axis to show top products at the top
    plt.savefig('Top 10 Products by Gross Sales.png')

    # Customer Market-wise Sales
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Customer Market', y='Gross Sales', hue='Product Department', data=df, estimator=sum, ci=None)
    plt.title('Customer Market-wise Sales by Product Department')
    plt.xlabel('Customer Market')
    plt.ylabel('Total Gross Sales')
    plt.legend(title='Product Department', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig('Customer Market-wise Sales by Product Department.png')

    # Order Processing Time Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Order Processing Time'], bins=20, kde=True)
    plt.title('Distribution of Order Processing Time')
    plt.xlabel('Order Processing Time (days)')
    plt.ylabel('Frequency')
    plt.savefig('Distribution of Order Processing Time.png')

    # Warehouse Inventory vs. Warehouse Order Fulfillment (days)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Warehouse Inventory', y='Warehouse Order Fulfillment (days)', data=df)
    plt.title('Warehouse Inventory vs. Warehouse Order Fulfillment Time')
    plt.xlabel('Warehouse Inventory')
    plt.ylabel('Warehouse Order Fulfillment (days)')
    plt.savefig('Warehouse Inventory vs. Warehouse Order Fulfillment Time.png')

    # Profit Margin by Product Department
    df['Profit Margin'] = (df['Profit'] / df['Gross Sales']) * 100
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Product Department', y='Profit Margin', data=df)
    plt.title('Profit Margin by Product Department')
    plt.xlabel('Product Department')
    plt.ylabel('Profit Margin (%)')
    plt.xticks(rotation=45)
    plt.savefig('Profit Margin by Product Department.png')

    # Customer Market-wise Order Quantity
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Customer Market', y='Order Quantity', data=df, estimator=sum, ci=None)
    plt.title('Customer Market-wise Order Quantity')
    plt.xlabel('Customer Market')
    plt.ylabel('Total Order Quantity')
    plt.savefig('Customer Market-wise Order Quantity.png')

    # Customer Region-wise Sales Growth
    sales_growth = df.groupby(['Customer Region', 'Order YearMonth'])['Gross Sales'].sum().reset_index()
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='Order YearMonth', y='Gross Sales', hue='Customer Region', data=sales_growth)
    plt.title('Customer Region-wise Sales Growth')
    plt.xlabel('Order YearMonth')
    plt.ylabel('Total Gross Sales')
    plt.grid(True)
    plt.legend(title='Customer Region', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig('Customer Region-wise Sales Growth.png')

    # Pairplot with Order Quantity and Gross Sales
    sns.pairplot(df[['Order Quantity', 'Gross Sales', 'Discount %', 'Profit']])
    plt.savefig('Pairplot with Order Quantity and Gross Sales.png')

    # Interactive Choropleth Map (using Plotly)
    region_sales = df.groupby('Customer Region')['Gross Sales'].sum().reset_index()
    fig = px.choropleth(region_sales, locations='Customer Region', locationmode='country names', color='Gross Sales',
                        hover_name='Customer Region', color_continuous_scale='Viridis')
    fig.update_layout(title_text='Customer Region-wise Gross Sales')
    fig.savefig('Interactive Choropleth Map.png')

    # 3D Scatter Plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['Gross Sales'], df['Profit'], df['Discount %'], c='blue', marker='o')
    ax.set_xlabel('Gross Sales')
    ax.set_ylabel('Profit')
    ax.set_zlabel('Discount %')
    plt.title('3D Scatter Plot')
    plt.savefig('3D Scatter Plot.png')

    # Monthly Sales Trends
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Order YearMonth', y='Gross Sales', data=df, estimator='sum', ci=None)
    plt.title('Monthly Sales Trends')
    plt.xlabel('Order YearMonth')
    plt.ylabel('Total Gross Sales')
    plt.savefig('monthly_sales_trends.png')  # Save the figure

    # Boxplot of Order Processing Time by Product Category
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Product Category', y='Order Processing Time', data=df)
    plt.title('Boxplot of Order Processing Time by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Order Processing Time (days)')
    plt.xticks(rotation=45)
    plt.savefig('Boxplot of Order Processing Time by Product Category.png')

    # the total Gross Sales per Order Year
    sales_per_year = df_orders.groupby(' Order Year ')[' Gross Sales '].sum()

    plt.figure(figsize=(10,6))
    sales_per_year.plot(kind='bar')
    plt.title('Total Gross Sales per Order Year')
    plt.xlabel('Order Year')
    plt.ylabel('Gross Sales')
    plt.savefig('Total Gross Sales per Order Year.png')

    # the total Profit per Product Category
    profit_per_category = df_orders.groupby('Product Category')[' Profit '].sum()

    plt.figure(figsize=(10,6))
    profit_per_category.plot(kind='bar')
    plt.title('Total Profit per Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Profit')
    plt.savefig('Total Profit per Product Category.png')

    # total Warehouse Inventory per Year Month
    inventory_per_month = df_inventory.groupby(' Year Month ')[' Warehouse Inventory '].sum()

    plt.figure(figsize=(10,6))
    inventory_per_month.plot(kind='line')
    plt.title('Total Warehouse Inventory per Year Month')
    plt.xlabel('Year Month')
    plt.ylabel('Warehouse Inventory')
    plt.savefig('Total Warehouse Inventory per Year Month.png')

    # average Inventory Cost Per Unit per Product Name
    cost_per_product = df_inventory.groupby('Product Name')['Inventory Cost Per Unit'].mean()

    plt.figure(figsize=(20,6))
    cost_per_product.plot(kind='bar')
    plt.title('Average Inventory Cost Per Unit per Product Name')
    plt.xlabel('Product Name')
    plt.ylabel('Inventory Cost Per Unit')
    plt.savefig('Average Inventory Cost Per Unit per Product Name.png')
    

if __name__ == "__main__":
    regenerate_figures()
