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
def drilling(datatype,format,start,end,wellbore,output,log,debug,rolldays):
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
            dObj.get_csv_data(output,fromDate,toDate,wellbore,type_enum)
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
              type=click.Choice(['Production',
               'Injection',
               'Consumption',
               'Import',
               'Export',
               'Inventory',
               'InstallationData'], 
              case_sensitive=True),
              help='The type of production data to query for, e.g. to get export volumes user "export" to get consumption (fuel/flare++) use "Consumption"',
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
def production(datatype,format,start,end,asset,output,log,debug,rolldays,product):
    __initialize_logging(log,debug)
    logging.info("Extracting data for - dataType:%s, format:%s, st art:%s, end:%s, asset:%s, output:%s",
    datatype,format,start,end,asset,output)
    fromDate=start 
    toDate=end
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
        type_enum=pObj.map_str_prod_datatype_to_enum(datatype)
        #need to check if we should just rolldays
        if rolldays>0:
            toDate=common_utils.format_date_to_yy_mm_dd(common_utils.add_days(datetime.today(),1))
            fromDate=common_utils.format_date_to_yy_mm_dd(common_utils.substract_days(datetime.today(),rolldays))
        #need to handle the format
        if format=='json':
            #handle json
            pObj.get_json_data_to_file(output,fromDate,toDate,asset,type_enum,product)
            logging.info("Data written to:%s",output)
        elif format=='xml':
            pObj.get_xml_data(output,fromDate,toDate,asset,type_enum,product)
            logging.info("Data written to:%s",output)
        elif format=='csv':
            #handle csv
            pObj.get_csv_data(output,fromDate,toDate,asset,type_enum,product)
            logging.info("Data written to:%s",output)
        elif format=='excel':
            #handle excel
            pObj.get_excel_data(output,fromDate,toDate,asset,type_enum,product)
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