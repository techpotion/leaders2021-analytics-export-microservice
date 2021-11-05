import pandas as pd
import gen.pb.export_microservice_pb2 as pb2
from pprint import pprint
import time
import os

class Exporter:
    def __init__(self):
        try:
            os.mkdir('export')
        except:
            pass

    def __get_kinds_df(self, basic: dict) -> pd.DataFrame:
        df_kinds = pd.DataFrame(columns=['Виды спорта', ])
        for kind in basic['sportsKinds']:
            df_kinds = df_kinds.append({'Виды спорта': kind}, ignore_index=True)
        return df_kinds

    def __get_area_types_df(self, basic: dict) -> pd.DataFrame:
        df_area_types = pd.DataFrame(columns=['Типы спортзон'])
        for areatype in basic['areaTypes']:
            df_area_types = df_area_types.append({'Типы спортзон': areatype}, ignore_index=True)
        return df_area_types

    def __get_basic_df(self, basic: dict) -> pd.DataFrame:
        df_basic = pd.DataFrame(columns=['Кол-во спорт объектов', 'Площадь спорт. площадок', 'Кол-во спорт. площадок',  'Кол-во видов спорта', 'Кол-во спорт. услуг', 'Плотность населения'])
        df_basic = df_basic.append({
            'Кол-во спорт объектов': basic['sportsObjectsAmount'],
            'Площадь спорт. площадок': basic['areasSquare'],
            'Кол-во спорт. площадок': basic['areasAmount'],
            'Кол-во видов спорта': basic['sportsAmount'],
            'Кол-во спорт. услуг': basic['areaTypesAmount'],
            'Плотность населения': basic['density']
        }, ignore_index=True)
        return df_basic

    def __get_basic_per_100k(self, basic: dict) -> pd.DataFrame:
        df_basic_per_100k = pd.DataFrame(columns=['Кол-во спорт объектов на 100тыс. чел', 'Площадь спорт. площадок на 100тыс. чел', 'Кол-во спорт. площадок на 100тыс. чел',  'Кол-во видов спорта на 100тыс. чел'])
        df_basic_per_100k = df_basic_per_100k.append({
            'Кол-во спорт объектов на 100тыс. чел': basic['sportsObjectsAmountPer100k'],
            'Площадь спорт. площадок на 100тыс. чел': basic['areasSquarePer100k'],
            'Кол-во спорт. площадок на 100тыс. чел': basic['areasAmountPer100k'],
            'Кол-во видов спорта на 100тыс. чел': basic['sportsAmountPer100k'],
        }, ignore_index=True)
        return df_basic_per_100k

    def __dfs_to_xlsx(self, output: str, df_kinds, df_area_types, df_basic, df_basic_per_100k) -> None:
        with pd.ExcelWriter(output) as writer:
            df_basic.to_excel(writer, sheet_name='Аналитика', index=False)
            df_basic_per_100k.to_excel(writer, sheet_name='Аналитика на 100 тыс. чел', index=False)
            df_area_types.to_excel(writer, sheet_name='Виды спорт. услуг', index=False)
            df_kinds.to_excel(writer, sheet_name='Виды спорта', index=False)

    def to_xlsx(self, request: dict) -> str:
        basic = request['basicAnalytics']
        df_kinds = self.__get_kinds_df(basic)
        df_area_types = self.__get_area_types_df(basic)
        df_basic = self.__get_basic_df(basic)
        df_basic_per_100k = self.__get_basic_per_100k(basic)

        output_name = f'export/output-{int(time.time())}.xlsx'
        self.__dfs_to_xlsx(output_name, df_kinds, df_area_types, df_basic, df_basic_per_100k)

        return output_name

    def file_to_bytes(self, filepath: str) -> bytes:
        with open(filepath, 'rb') as content_file:
            content = content_file.read()
        content_file.close()
        os.remove(filepath)
        return content