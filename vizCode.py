import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def createDf(filename):
    """
    Reads given file and returns it as a pandas dataframe after dropping duplicates if any
    """
    salesFile = pd.read_csv("WeeklySalesReport.csv")
    salesFile.drop_duplicates(inplace = True)
    return salesFile
    
def dataOveriew(df):
    """"
    Function to help get an overview of what kind of set you're working with
    """
    print(f'Overview of given file:')
    print('Number of rows: ', df.shape[0])
    print("Number of features:", df.shape[1])
    print("Data Features:")
    print(df.columns.tolist())
    print("Missing values:", df.isnull().sum().values.sum())
    print("Unique values:")
    print(df.nunique())

def applyWeekMasks(df):
    """
    Function applies mask's to datafile and returns 3 chunks of the original datafile
    """
    year_mask1 = (df['WEEK_ID'] >= 202134) & (df['WEEK_ID'] <= 202153)
    df_year_mask1_applied = df[year_mask1]
    year_mask2 = (df['WEEK_ID'] >= 202200) & (df['WEEK_ID'] <= 202270)
    df_year_mask2_applied = df[year_mask2]
    year_mask3 = (df['WEEK_ID'] >= 202302) & (df['WEEK_ID'] <= 202325)
    df_year_mask3_applied = df[year_mask3]
    return [df_year_mask1_applied, df_year_mask2_applied, df_year_mask3_applied]

def plotOrderCount(sales_df1, sales_df2, sales_df3):
    """
    Maps each week_ID to a sequential number and maps them to a unique week to combine 3 dataframes and plot
    """
    unique_weeks = sorted(set(sales_df1['WEEK_ID']) | set(sales_df2['WEEK_ID']) | set(sales_df3['WEEK_ID']))
    week_map = {week: i + 1 for i, week in enumerate(unique_weeks)}

    sales_df1['WEEK_SEQ'] = sales_df1['WEEK_ID'].map(week_map)
    sales_df2['WEEK_SEQ'] = sales_df2['WEEK_ID'].map(week_map)
    sales_df3['WEEK_SEQ'] = sales_df3['WEEK_ID'].map(week_map)
    plt.figure(figsize=(10, 6))
    plt.scatter(sales_df1['WEEK_SEQ'], sales_df1['ORDER_COUNT'], label='DF1 ORDER_COUNT', marker='o', color='blue')
    plt.scatter(sales_df2['WEEK_SEQ'], sales_df2['ORDER_COUNT'], label='DF2 ORDER_COUNT', marker='^', color='green')
    plt.scatter(sales_df3['WEEK_SEQ'], sales_df3['ORDER_COUNT'], label='DF3 ORDER_COUNT', marker='s', color='red')
    plt.xlabel('Sequential Weeks')
    plt.ylabel('Count')
    plt.title('Sales Data Comparison-ORDER_COUNT')
    plt.legend()
    plt.show()

def plotQuantityCount(sales_df1, sales_df2, sales_df3):
    """
    Maps each week_ID to a sequential number and maps them to a unique week to combine 3 dataframes and plot
    """
    unique_weeks = sorted(set(sales_df1['WEEK_ID']) | set(sales_df2['WEEK_ID']) | set(sales_df3['WEEK_ID']))
    week_map = {week: i + 1 for i, week in enumerate(unique_weeks)}

    sales_df1['WEEK_SEQ'] = sales_df1['WEEK_ID'].map(week_map)
    sales_df2['WEEK_SEQ'] = sales_df2['WEEK_ID'].map(week_map)
    sales_df3['WEEK_SEQ'] = sales_df3['WEEK_ID'].map(week_map)
    plt.figure(figsize=(10, 6))
    plt.scatter(sales_df1['WEEK_SEQ'], sales_df1['QUANTITIY_COUNT'], label='DF1 QUANTITIY_COUNT', marker='x', color='blue')
    plt.scatter(sales_df2['WEEK_SEQ'], sales_df2['QUANTITIY_COUNT'], label='DF2 QUANTITIY_COUNT', marker='+', color='green')
    plt.scatter(sales_df3['WEEK_SEQ'], sales_df3['QUANTITIY_COUNT'], label='DF3 QUANTITIY_COUNT', marker='*', color='red')
    plt.xlabel('Sequential Weeks')
    plt.ylabel('Count')
    plt.title('Sales Data Comparison-QUANTITY_COUNT')
    plt.legend()
    plt.show()

def add_volume_column(df):
    """
    Creates new dataframe from given one which replaces order and quantity with a volume column
    """
    new_df = df[['CONTACT_ID', 'WEEK_ID']].copy()
    new_df['VOLUME'] = df['ORDER_COUNT'] * df['QUANTITIY_COUNT']
    return new_df

def plotVolumeCount(sales_df1, sales_df2, sales_df3):
    """
    Maps each week_ID to a sequential number and maps them to a unique week to combine 3 dataframes and plot
    """
    unique_weeks = sorted(set(sales_df1['WEEK_ID']) | set(sales_df2['WEEK_ID']) | set(sales_df3['WEEK_ID']))
    week_map = {week: i + 1 for i, week in enumerate(unique_weeks)}

    sales_df1['WEEK_SEQ'] = sales_df1['WEEK_ID'].map(week_map)
    sales_df2['WEEK_SEQ'] = sales_df2['WEEK_ID'].map(week_map)
    sales_df3['WEEK_SEQ'] = sales_df3['WEEK_ID'].map(week_map)
    plt.figure(figsize=(10, 6))
    plt.scatter(sales_df1['WEEK_SEQ'], sales_df1['VOLUME'], label='DF1 VOLUME', marker='x', color='blue')
    plt.scatter(sales_df2['WEEK_SEQ'], sales_df2['VOLUME'], label='DF2 VOLUME', marker='+', color='green')
    plt.scatter(sales_df3['WEEK_SEQ'], sales_df3['VOLUME'], label='DF3 VOLUME', marker='*', color='red')
    plt.xlabel('Sequential Weeks')
    plt.ylabel('Count')
    plt.title('Sales Data Comparison-VOLUME')
    plt.legend()
    plt.show()

def perform_fft(df):
    """
    Function performs FFT as well as plot the results
    """
    volume_data = df['VOLUME'].values
    fft_values = np.fft.fft(volume_data)
    fft_freq = np.fft.fftfreq(len(volume_data))
    
    plt.figure(figsize=(10, 6))
    plt.plot(fft_freq, np.abs(fft_values))
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.title('FFT of VOLUME')
    plt.show()
    
    return fft_freq, fft_values

def oneCust(file, custNum):
    """
    Function takes original datafile and and returns new file with only given customer ID transactions
    """
    miniFile = file.loc[(file['CONTACT_ID'] == custNum), :]
    plt.scatter(miniFile['WEEK_ID'], miniFile['VOLUME'])
    plt.xlabel("Sequential Weeks")
    plt.ylabel("Volume Count")
    plt.title(f"Individual Customer Sales - {custNum}")
    plt.show()
    return miniFile