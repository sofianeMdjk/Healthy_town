import pandas as pd


def load_dataset(path):
    dataset_url = path

    df = pd.read_csv(
        dataset_url,
        usecols=lambda col: col not in ["ID_Espani"]
    )

    danger_1 = df.head(15)
    danger_2 = df.loc[16:31, :]
    danger_3 = df.loc[32:50, :]

    danger1_data = [danger_1['latitude'], danger_1['longitude'], danger_1['score'], danger_1['Nom_Espai']]
    danger2_data = [danger_2['latitude'], danger_2['longitude'], danger_2['score'], danger_2['Nom_Espai']]
    danger3_data = [danger_3['latitude'], danger_3['longitude'], danger_3['score'], danger_3['Nom_Espai']]

    return danger1_data, danger2_data, danger3_data




