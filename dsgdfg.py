import pandas as pd
import pandas.api.types as ptypes

filename = input("Please, enter name of your file: ")  


class DataFrameStructureError(Exception):
    pass

class DataTypeError(Exception):
    pass

class Dataframe:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.df = pd.read_csv(filename)
        except FileNotFoundError:
            print('No such file')
            raise SystemExit()
        except pd.errors.EmptyDataError:
            print('No data')
            raise SystemExit()
        except pd.errors.ParserError:
            print('Wrong data, invalid columns')
            raise SystemExit()
        
        try:
            self.column_list_from_file = self.df.columns.to_list()
            self.df_original = pd.read_csv('var3_copy.csv')
            self.column_list_main = self.df_original.columns.to_list()
            
            if self.column_list_from_file != self.column_list_main:
                raise DataFrameStructureError('Wrong structure')
            else:
                print('Everything alright')
        except DataFrameStructureError:
            print('Please, remake your columns, we were expecting', self.column_list_main, ', but you provided', self.column_list_from_file)
            raise SystemExit()
        
        # Проверка соответствия типов данных
        expected_dtypes = self.df_original.dtypes.to_dict()
        actual_dtypes = self.df.dtypes.to_dict()

        for column in expected_dtypes:
            if column in actual_dtypes and not ptypes.is_dtype_equal(actual_dtypes[column], expected_dtypes[column]):
                print(f'Error: Column "{column}" has incorrect data type: {actual_dtypes[column]}, expected {expected_dtypes[column]}')
                raise SystemExit()

        print("File loaded and verified successfully!")

df = Dataframe(filename)
