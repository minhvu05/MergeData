import pandas as pd
import glob

def merge_data(file1, file2, file3, ans_file):
    # Creating dataframes from given text files
    df1 = pd.read_csv('file1.txt', header=None, names=['word']).drop_duplicates()
    df2 = pd.read_csv('file2.txt', header=None, names=['word']).drop_duplicates()
    df3 = pd.read_csv('file3.txt', header=None, names=['word']).drop_duplicates()

    # Add columns to show  which word came from which file
    df1['file1'] = 'yes'
    df2['file2'] = 'yes'
    df3['file3'] = 'yes'

    # Merge all dataframes into 1
    merged_df = pd.merge(df1[['word', 'file1']], df2[['word', 'file2']], on='word', how='outer')
    merged_df = pd.merge(merged_df, df3[['word', 'file3']], on='word', how='outer')

    # Replace all the NaN values with no
    merged_df['file1'] = merged_df['file1'].fillna('no')
    merged_df['file2'] = merged_df['file2'].fillna('no')
    merged_df['file3'] = merged_df['file3'].fillna('no')

    # Create a count to see when and which column to put yes in
    merged_df['count'] = merged_df[['file1', 'file2', 'file3']].apply(lambda row: row == 'yes', axis=1).sum(axis=1)

    # Formatting the dataframe
    merged_df = merged_df[['word', 'file1', 'file2', 'file3', 'count']]
    merged_df.columns = ['data', file1, file2, file3, 'count']

    # More efficient way to remove data as one of the possible items
    merged_df = merged_df[merged_df['data'] != 'data']

    # Sorting y/n by count
    merged_df = merged_df.sort_values('count', ascending = False)


    # ; to separate each column
    merged_df.to_csv(ans_file, index=False, sep=';', header=True)

  

merge_data("file1.txt", "file2.txt", "file3.txt", "output.txt")

