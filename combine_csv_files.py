import os
import glob
import pandas as pd

def combine_csv_files(directory, output_file):
    # Change this to the directory where your CSVs are saved
    os.chdir(directory)
    all_files = glob.glob('michigan_law_*.csv')
    all_data = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        # Extract the year from the filename
        year = filename.split('_')[-1].split('.')[0]
        df['Year'] = year
        all_data.append(df)

    combined_csv = pd.concat(all_data, axis=0, ignore_index=True)
    combined_csv.to_csv(output_file, index=False)
    print(f"Combined CSV has been saved as {output_file}")

# Usage example
combine_csv_files('/Users/joonchoi/Desktop/STATS451/finalproj/data', 'combined_michigan_law.csv')
