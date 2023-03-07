import click
import logging
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import drilling as subsurfaceDrilling
from subsurfaceCollabor8 import production as subsurfaceProduction
from subsurfaceCollabor8 import common_utils
from subsurfaceCollabor8 import reports
from datetime import datetime
@click.group()
def messages():
  pass


@click.command(name='drilling',help='Command to specify if drilling data should be extracted')
@click.option('--datatype',
              type=click.Choice(['activities',
               'lithology',
               'status_info'], 
              case_sensitive=True),
              help='The type of drilling data to query for: activities, lithology or status_info',
              required=True)
@click.option('--format',
              type=click.Choice(['json', 'csv','excel','xml'], 
              case_sensitive=True),
              help='The type of format to extract the data to',
              required=True)
@click.option('--start',
              help='The start time to use in the form of e.g. UTC time or a date such as e.g. 2020-01-21T23:00:00.000Z',
              required=False)
@click.option('--end',
              help='The end time to use in the form of e.g. UTC time or a date such as e.g. 2020-01-21T23:00:00.000Z',
              required=False)
@click.option('--wellbore',
              help='The name of the wellbore to query for data',
              required=True)
@click.option('--output',
              help='The full path to the file where to store results',
              required=True)
@click.option('--log',
              help='The full path to the logfile where to write log information',
              required=True)
@click.option('--debug/--no-debug', default=False)
@click.option('--rolldays',
               help='Number of days to automatically roll data',
               default=0,
               required=False )
@click.option('--decimalformat',
              help='The decimal format to use for decimal separator',
              required=False, default=',')
def drilling(datatype,format,start,end,wellbore,output,log,debug,rolldays,decimalformat):
    __initialize_logging(log,debug)
    logging.info("Extracting data for - dataType:%s, format:%s, start:%s, end:%s, wellbore:%s, output:%s",
    datatype,format,start,end,wellbore,output)
    toDate=end 
    fromDate=start
    #get the token first
    authInfo=auth.AuthInfo()
    authInfo.init_from_env_vars()
    try:
        #create the filepath if not existing
        common_utils.create_filepath_if_not_exists(output)
        
        authObj=auth.Authenticate(authInfo) 
        token=authObj.authenticate()
        dObj=subsurfaceDrilling.DrillingData(token)
        #map the datatype
        type_enum=dObj.map_str_activity_to_enum(datatype)
        #handle rolldays
        if rolldays>0:
            toDate=common_utils.format_date_to_yy_mm_dd(common_utils.add_days(datetime.today(),1))
            fromDate=common_utils.format_date_to_yy_mm_dd(common_utils.substract_days(datetime.today(),rolldays))
        #need to handle the format
        if format=='json':
            #handle json
            dObj.get_json_data_to_file(output,fromDate,toDate,wellbore,type_enum)
            logging.info("Data written to:%s",output)
        elif format=='xml':
            dObj.get_xml_data(output,fromDate,toDate,wellbore,type_enum)
            logging.info("Data written to:%s",output)
        elif format=='csv':
            #handle csv
            dObj.get_csv_data(output,fromDate,toDate,wellbore,type_enum,decimalformat)
            logging.info("Data written to:%s",output)
        elif format=='excel':
            #handle excel
            dObj.get_excel_data(output,fromDate,toDate,wellbore,type_enum)
            logging.info("Data written to:%s",output)
        else:
            logging.info("Unknown format...")
    except Exception as err:
        logging.error("Failed in processing of drilling data:%s",str(err), exc_info=True)
    


@click.command(name='production',help='Command to specify if production data should be extracted')
@click.option('--datatype', 
              
              help='The type of production data to query for, e.g. to get export volumes use "Export" to get consumption (fuel/flare++) use "Consumption"',
              required=True)
@click.option('--format',
              type=click.Choice(['json', 'csv','excel','xml'], 
              case_sensitive=True),
              help='The type of format to extract the data to',
              required=True)
@click.option('--start',
              help='The start time to use in the form of e.g. UTC time or a date such as e.g. 2020-01-21T23:00:00.000Z',
              required=False)
@click.option('--end',
              help='The end time to use in the form of e.g. UTC time or a date such as e.g. 2020-01-21T23:00:00.000Z',
              required=False)
@click.option('--asset',
              help='The name of the asset to query for data e.g. GINA KROG',
              required=True)
@click.option('--output',
              help='The full path to the file where to store results',
              required=True)
@click.option('--log',
              help='The full path to the logfile where to write log information',
              required=True)
@click.option('--debug/--no-debug', default=False)
@click.option('--rolldays',
               help='Number of days to automatically roll data',
               default=0,
               required=False )
@click.option('--product',
              help='The product to query for e.g. gas',
              required=False, default='')
@click.option('--decimalformat',
              help='The decimal format to use for decimal separator',
              required=False, default=',')
@click.option('--reporttype',
              type=click.Choice(['DPR',
               'MPRML-GOV',
               'MPRML-PARTNER',
               'ANY'], 
              case_sensitive=True),
              help='The type of report type to query for (optional) e.g. MPRML-GOV, DPR and so on',
              required=False,
              default='ANY')
@click.option('--filter',
              help='A possible additional filter to add to filter the data even more e.g. data_periods:["day"] to only include data with registered period day',
              required=False, default='')
@click.option('--include_only_sm3/--all_units',
              help='If set will filter away any non Sm3 volume units and datarows',
              default=False)
def production(datatype,format,start,end,asset,output,log,debug,rolldays,product,decimalformat,reporttype,filter,include_only_sm3):
    __initialize_logging(log,debug)
    logging.info("Extracting data for - dataType:%s, format:%s, start:%s, end:%s, asset:%s, output:%s, reporttype:%s",
    datatype,format,start,end,asset,output,reporttype)
    if reporttype=='ANY':
        reporttype=''
    fromDate=start 
    toDate=end
    #check if we need to add some additional signs to the data type in case it is a single query
    if datatype.find(',')!=-1:
            splitted=datatype.split(',')
            tempType=''
            i=0
            for item in splitted:
                if i==0:
                    tempType='"'+item+'"'
                else:
                    tempType=tempType+',"'+item+'"'
                i=+1
            datatype=tempType
                
    else:
        datatype='"'+datatype+'"'
    #get the token first
    authInfo=auth.AuthInfo()
    authInfo.init_from_env_vars()
    try:
        #create the filepath if not existing
        common_utils.create_filepath_if_not_exists(output)
        authObj=auth.Authenticate(authInfo) 
        token=authObj.authenticate()
        pObj=subsurfaceProduction.ProductionData(token)
        #map the datatype
        #need to check if we should just rolldays
        if rolldays>0:
            toDate=common_utils.format_date_to_yy_mm_dd(common_utils.add_days(datetime.today(),1))
            fromDate=common_utils.format_date_to_yy_mm_dd(common_utils.substract_days(datetime.today(),rolldays))
        #need to handle the format
        if format=='json':
            #handle json
            pObj.get_json_data_to_file(output,fromDate,toDate,asset,datatype,product,reporttype,filter)
            logging.info("Data written to:%s",output)
        elif format=='xml':
            pObj.get_xml_data(output,fromDate,toDate,asset,datatype,product,reporttype)
            logging.info("Data written to:%s",output)
        elif format=='csv':
            #handle csv
            pObj.get_csv_data(output,fromDate,toDate,asset,datatype,product,decimalformat,reporttype,filter)
            logging.info("Data written to:%s",output)
        elif format=='excel':
            #handle excel
            pObj.get_excel_data(output,fromDate,toDate,asset,datatype,product,reporttype,filter,includeOnlySm3=include_only_sm3)
            logging.info("Data written to:%s",output)
        else:
            logging.info("Unknown format...")
        
    except Exception as err:
        logging.error("Failed in processing of production data:%s",str(err), exc_info=True)
    

def __initialize_logging(log_file,debug):
    #make sure that the path to the logfile exists
    common_utils.create_filepath_if_not_exists(log_file)
    if debug==False:
        logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
        )
    else:
        logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
        )



@click.command(name='publish',help='Command to publish a report')
@click.option('--reporttype',
              type=click.Choice(['DPR10',
               'DPR20',
               'MPR-GOV',
               'MPR-PARTNER',
               'DDR-GOV'], 
              case_sensitive=True),
              help='The type of report to publish DPR20, MPR-GOV, MPR-PARTNER or DDR-GOV',
              required=True)
@click.option('--reportfile',
              help='The full path to the report file to publish',
              required=True)
@click.option('--log',
              help='The full path to the logfile where to write log information',
              required=True)
@click.option('--debug/--no-debug', default=False)
def publish(reporttype,reportfile,log,debug):
    __initialize_logging(log,debug)
    logging.info("Publishing report type:%s, file:%s",
    reporttype,reportfile)
    #get the token first
    authInfo=auth.AuthInfo()
    authInfo.init_from_env_vars()
    try:
        authObj=auth.Authenticate(authInfo) 
        token=authObj.authenticate()
        report=reports.Reports(token)
        #map the report type to the enum
        reportEnum=report.map_str_reporttype_to_enum(reporttype)
        #submit it
        result=report.publish(reportEnum,reportfile)
        logging.info("Published report, response:%s",str(result))
    except Exception as err:
        logging.error("Failed in publish:%s",str(err),exc_info=True)


@click.command()
@click.pass_context
def help(ctx):
    print(ctx.parent.get_help())



messages.add_command(drilling)
messages.add_command(production)
messages.add_command(publish)
messages.add_command(help)

if __name__ == '__main__':
    messages()