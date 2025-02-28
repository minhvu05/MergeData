import pandas as pd
import glob

def list_common_items(file1, file2, file3, ans_file):
    # Creating dataframes from given text files
    df1 = pd.read_csv('file1.txt', header=None, names=['word'])
    df2 = pd.read_csv('file2.txt', header=None, names=['word'])
    df3 = pd.read_csv('file3.txt', header=None, names=['word'])

    # Add columns to show  which word came from which file
    df1['file1'] = 'yes'
    df2['file2'] = 'yes'
    df3['file3'] = 'yes'

    # Merge all dataframes into 1
    df1 = pd.merge(df1, df2[['word']], on='word', how='left').fillna({'file2': 'no'})
    df1 = pd.merge(df1, df2[['word']], on='word', how='left').fillna({'file3': 'no'})

    final_df = pd.concat([df1[['word', 'file1', 'file2', 'file3']], 
                        df2[['word', 'file2']], 
                        df3[['word', 'file3']]], 
                        axis=0).drop_duplicates(subset=['word']).reset_index(drop=True)



    



list_common_items("file1.txt", "file2.txt", "file3.txt", "ans.txt")