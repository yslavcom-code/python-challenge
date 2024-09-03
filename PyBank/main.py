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
        
        print("Financial analysis\n----------------------------\n")
        format_string = "Total Months: {months_count}\nTotal: ${net_total_amount}\nAverage Change: ${average_change:.2f}\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
        format_values = {'months_count':months_count, 'net_total_amount':net_total_amount, 'average_change':average_change, 'greatest_increase_date':greatest_increase_date, 'greatest_increase':greatest_increase, 'greatest_decrease_date':greatest_decrease_date, 'greatest_decrease':greatest_decrease}
        formatted_output = format_string.format(**format_values)
        print(formatted_output)
        with open('analysis/budget_data.txt', 'w') as f:
            print("Financial analysis\n----------------------------\n", file=f)
            print(formatted_output, file=f)