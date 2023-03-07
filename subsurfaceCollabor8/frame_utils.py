from pandas import DataFrame
import os

def frame_to_csv(frame:DataFrame,output_file:str,decimal_format=',',
float_format=None,date_format=None,quote_char='"',no_data_repr='',sep=';'):
    """
    Converts a pandas dataframe to a csv file

    Parameters
    ----------

    output_file -> path to file to write to
    decimal_format -> decimal separator to use default ","
    float_format -> format mask to use for floats, default none
    date_format -> format mask for date, default none 
    quote_char -> string quote char, default '"'
    no_data_repr -> how to represent empty columns, default ''

    """
    frame.to_csv(output_file,decimal=decimal_format,
    float_format=float_format,date_format=date_format,
    quotechar=quote_char,na_rep=no_data_repr,sep=sep)

def frame_to_csv_str(frame:DataFrame,decimal_format=',',
float_format=None,date_format=None,quote_char='"',no_data_repr='',sep=';'):
    """
    Converts a pandas dataframe to a csv formatted string

    Parameters
    ----------

    decimal_format -> decimal separator to use default ","
    float_format -> format mask to use for floats, default none
    date_format -> format mask for date, default none 
    quote_char -> string quote char, default '"'
    no_data_repr -> how to represent empty columns, default ''

    """
    return frame.to_csv(None,decimal=decimal_format,
    float_format=float_format,date_format=date_format,
    quotechar=quote_char,na_rep=no_data_repr,sep=sep)

def frame_to_excel(frame:DataFrame,output_file:str,
float_format=None,no_data_rep='',sheetName='Sheet1',includeOnlySm3=False):
    """
    Converts a pandas data frame to a excel file

    Parameters
    ----------

    output_file -> path to file to write to
    float_format -> format mask for floats e.g. '%.2f' will format to 2 decimals, default None
    no_data_rep -> how empty columns should be represented, default ''
    includeOnlySm3-> will only include Sm3 volumes
    """
    if includeOnlySm3:
        #need to filter the frame to only include Sm3 volumes
        filtered_frame=frame.loc[frame['volume.uom'] == 'Sm3'] 
        filtered_frame.to_excel(output_file,sheet_name=sheetName,
    float_format=float_format,na_rep=no_data_rep)
    else:
        frame.to_excel(output_file,sheet_name=sheetName,
    float_format=float_format,na_rep=no_data_rep)


