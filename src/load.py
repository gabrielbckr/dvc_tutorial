import pandas as pd


def load_raw_dataset(read_path, write_path) -> pd.DataFrame:
    columns = [
        'ID,' 'Age', 'Gender', 'Education', 'Country', 'Ethnicity', 
        'Nscore', 'Escore', 'Oscore', 
        'Ascore', 'Cscore,' 'Impulsive', 'SS', 'Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Caff', 
        'Cannabis', 'Choc', 'Coke', 'Crack', 'Ecstasy', 'Ketamine', 'Legalh', 'LSD', 'Meth',
        'Mushrooms', 'Nicotinem', 'Semer', 'VSA'  
    ]
    df = pd.read_csv(read_path, names=columns).iloc[:,:-20]
    print(df.head())
    df.to_csv(write_path)


if __name__ == "__main__":
    load_raw_dataset('data/01_raw/drug_consumption.data', 'data/02_trusted/d.csv')