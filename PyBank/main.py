import os
import pandas as pd

def get_file_data():
    file_path = 'Resources/budget_data.csv'
    return pd.read_csv(file_path)

if __name__ == "__main__":
    data = get_file_data()
    if data is not None:
        date_column = data['Date']
        profit_loss_column = data['Profit/Losses']
        
        # total months
        months_count = len(date_column)
        
        # total
        net_total_amount = profit_loss_column.sum()
        previous_profit_loss_column = profit_loss_column.shift(1)
        
        # delta series
        delta = profit_loss_column - previous_profit_loss_column
        
        # and average change
        average_change = round(delta.mean(), 2)
        
        # max & min
        greatest_increase = round(delta.max())
        greatest_increase_date = date_column[delta.idxmax()]
        
        greatest_decrease = round(delta.min())
        greatest_decrease_date = date_column[delta.idxmin()]
        
        
        print(f"Total Months: {months_count}\nTotal: ${net_total_amount}\nAverage Change: ${average_change}\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")       
        with open('analysis/budget_data.txt', 'w') as f:
            print(f"Total Months: {months_count}\nTotal: ${net_total_amount}\nAverage Change: ${average_change}\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n", file=f)