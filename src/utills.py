import numpy as np
import pandas as pd


def script_stages_and_form(file_form: str, file_stages: str) -> None:
    df_form = pd.read_excel(file_form)
    df_stages = pd.read_excel(file_stages)
    df_form = df_form.drop(
        columns=['Unnamed: 3', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 5', 'Unnamed: 7', 'Unnamed: 13'])
    df_form = df_form.rename(columns={'Unnamed: 4': 'Unnamed: 2'})
    df_stages = df_stages.replace({np.nan: 0})
    new_df = df_stages[4:]
    new_df = new_df[
        (new_df['Unnamed: 6'] - new_df['Unnamed: 9'] > 0) | (new_df['Unnamed: 6'] - new_df['Unnamed: 11'] > 0)]
    new_df = new_df[(new_df['Unnamed: 4'] == 'Нет') | (new_df['Unnamed: 4'] == 0)]
    df_stages = pd.concat([df_stages[:4], new_df])
    result = pd.merge(df_stages, df_form, how="left", on='Unnamed: 2')
    result.to_excel('Результат сведения таблиц.xlsx', index=False, header=False)


if __name__ == '__main__':
    script_stages_and_form(file_form='2107 формуляр.xls', file_stages='2107 этапы.xls')