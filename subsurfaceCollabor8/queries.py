from string import Template


def get_drilling_activity_query(period_start,period_end,wellborename):
    """
    Generates a GraphQL query for getting wellbore activity information in given period and for given wellbore

    Parameters
    ----------
    period_start -> start of period e.g. "2020-01-21T23:00:00.000Z" 
    period_end -> end of period e.g. "2020-03-26T12:00:00.000Z"
    wellborename -> name of wellbore e.g. "34/4-M-4 H"

    """
    query='''
    query {
  drilling {
    drillingActivity(
      limit: 1000
      period_after: "$start"
      period_before: "$end"
      entityName:"$name"
    ) {
      created
      modified
      endTime
      startTime
      dataStartTime
      dataEndTime
      dataEntity {
        name
        type
      }
     conveyance
     state
     stateDetailActivity
     phase
     proprietaryCode
     comment
     measuredDepth{
      unitOfMeasurement
      value
    }
      measuredHoleStart{
        startTime
        endTime
        unitOfMeasurement
        value
      }
      trueVerticalDepth{
        unitOfMeasurement
        value
      }
      
     
   
  }
  }
}
    '''
    s = Template(query)
    return s.substitute(start=period_start,end=period_end,name=wellborename)

def get_drilling_lithology_description(wellborename):
  """
  Generates a GraphQL query for getting wellbore lithology information for given wellbore

  Parameters
  ----------

  wellborename -> name of wellbore e.g. "34/4-M-4 H"
  """
  query='''
  query {
  drilling {
    lithology(limit: 1000
   
      
      entityName: ["$wellbore"])
      {
        dataEntity{
          name 
          uid
      }
      dataStartTime
      dataEndTime
      endTime
      startTime
      lithologyDecription
      showDescription
      measuredDepthTop{
        unitOfMeasurement
        value
      }
      measuredDepthBottom{
        unitOfMeasurement
        value
      }
      trueVerticalDepthTop{
        unitOfMeasurement
        value
      }
      trueVerticalDepthBottom{
        unitOfMeasurement
        value 
      } 
      created
      modified
      
  }
}
}

  '''
  s = Template(query)
  return s.substitute(wellbore=wellborename)


def get_drilling_status_info_query(period_start,period_end,wellborename):
  """
  Generates a GraphQL query for getting wellbore status information in given period and for given wellbore

  Parameters 
  ----------

  period_start -> start of period e.g. "2020-01-21T23:00:00.000Z" 
  period_end -> end of period e.g. "2020-03-26T12:00:00.000Z"
  wellborename -> name of wellbore e.g. "34/4-M-4 H"

  """
  query='''
  query {
  drilling {
    statusInfo(
      limit: 1000
      period_after: "$start"
      period_before: "$end"
      entityName:"$name"
    ) {
      dataStartTime
      dataEndTime
      dataEntity {
        name
        type
      }
      waterDepth{
        unitOfMeasurement
        value
      }
      sourceSystemReportName
      created
      modified
      reportNumber
      diameterCasingLast {
        unitOfMeasurement
        value
      }
      diameterHole {
        unitOfMeasurement
        value
      }
      diameterPilot {
        unitOfMeasurement
        value
      }
      distanceDrilled {
        unitOfMeasurement
        value
      }
      elevationKelly {
        unitOfMeasurement
        value
      }
      fixedRig
      forecast24Hrs
      sum24Hrs
      highPressureHighTemperature
      tightWell
      ropCurrent{
        unitOfMeasurement
        value
      }
      measuredDepth {
        unitOfMeasurement
        value
      }
      measuredDepthCasingLast {
        unitOfMeasurement
        value
      }
      measuredDepthDiameterHoleStart {
        unitOfMeasurement
        value
      }
      measuredDepthDiameterPilotPlan {
        unitOfMeasurement
        value
      }
      measuredDepthKickoff {
        unitOfMeasurement
        value
      }
      measuredDepthPlanned {
        unitOfMeasurement
        value
      }
      measuredDepthPlugTop {
        unitOfMeasurement
        value
      }
      pressTestType
      primaryConveyance
      ropCurrent {
        unitOfMeasurement
        value
      }
      tightWell
      timeHoleStart
      trueVerticalDepth {
        unitOfMeasurement
        value
      }
      trueVerticalDepthDiameterPilotPlan {
        unitOfMeasurement
        value
      }
      trueVerticalDepthKickoff {
        unitOfMeasurement
        value
      }
      typeWellbore
      waterDepth {
        unitOfMeasurement
        value
      }
      wellheadElevation {
        unitOfMeasurement
        value
      }
      
     
    }
   
   
  }
 
}

  '''
  s = Template(query)
  return s.substitute(start=period_start,end=period_end,name=wellborename)

def get_production_volumes(period_start,period_end,entity_name,volume_type):
  """
  Generates a production volumes query using enity name matching (exact match)

  Parameters
  ----------

  period_start -> start of period
  period_end -> end of period
  entity_name -> name of entity e.g. GINA KROG
  volume_type -> the type of volumes to fetch e.g. "Production", "Injection", "Consumption" or several in the form of
  "Consumption","Production" ++

  """
  query='''
    query {
  production {
    data(
      start: "$start"
      end: "$end"
      report_data_subtypes: [$type]
      entity_names: ["$name"]
      limit: 10000
    ) {
      sourceSystemReportName
      sourceStartTime
      sourceEndTime
      dataStartTime
      dataEndTime
      sourceEntity {
        name
        type
      }
      owningEntity {
        name
        type
      }
      dataEntity {
        name
        type
      }
      dataPeriod
      name
      type
      product
      productName
      qualifier
      volume {
        uom
        value
      }
     
      wellMeasurements {
        chokeSize {
          uom
          value
        }
        whp {
          uom
          value
        }
        wht {
          uom
          value
        }
        bhp {
          uom
          value
        }
        bht {
          uom
          value
        }
        operationTime{
          uom 
          value
        }
         annulusTemp
        {
        uom 
        value
        }
        annulusPress{
          uom 
          value 
        }
        dscp{
          uom 
          value
        }
         dsct{
          uom 
          value
        }
      }
      sourceSystemName
      sourceSystemVersion
      quality
      created
      modified
       measurements{
        mass{
          value
          unitOfMeasurement
        }
        density{
          value
          unitOfMeasurement
        }
      }
      comment
      uid
    }
    
  }
}
    '''
  s = Template(query)
  return s.substitute(start=period_start,end=period_end,name=entity_name,type=volume_type)


def get_production_volumes_several_assets(period_start,period_end,entity_name,volume_type,additionalFilter=''):
  """
  Generates a production volumes query using enity name matching (exact match)

  Parameters
  ----------

  period_start -> start of period
  period_end -> end of period
  entity_name -> name of entity e.g. GINA KROG
  volume_type -> the type of volumes to fetch e.g. "Production", "Injection", "Consumption" or several in the form of
  "Consumption","Production" ++

  """
  query='''
    query {
  production {
    data(
      start: "$start"
      end: "$end"
      report_data_subtypes: [$type]
      $add_filter
      entity_names: [$name]
      limit: 10000
    ) {
      sourceSystemReportName
      sourceStartTime
      sourceEndTime
      dataStartTime
      dataEndTime
      sourceEntity {
        name
        type
      }
      owningEntity {
        name
        type
      }
      dataEntity {
        name
        type
      }
      dataPeriod
      name
      type
      product
      productName
      qualifier
      volume {
        uom
        value
      }
     
      wellMeasurements {
        chokeSize {
          uom
          value
        }
        whp {
          uom
          value
        }
        wht {
          uom
          value
        }
        bhp {
          uom
          value
        }
        bht {
          uom
          value
        }
        operationTime{
          uom 
          value
        }
         annulusTemp
        {
        uom 
        value
        }
        annulusPress{
          uom 
          value 
        }
        dscp{
          uom 
          value
        }
         dsct{
          uom 
          value
        }
      }
      sourceSystemName
      sourceSystemVersion
      quality
      created
      modified
       measurements{
        mass{
          value
          unitOfMeasurement
        }
        density{
          value
          unitOfMeasurement
        }
      }
      comment
      uid
    }
    
  }
}
    '''
  s = Template(query)
  return s.substitute(start=period_start,end=period_end,name=entity_name,type=volume_type,add_filter=additionalFilter)



def get_production_volumes_regex(period_start,period_end,
entity_name,volume_type,product='',reportType='',additionalFilter=''):
  """
  Creates a production volumes query with the given period and tries to match entity names
  using a regex pattern
  """
  query=''
  if product=="":
    query=__get_production_query() 
  else:
    query=__get_production_query_for_product()
  #additional filtering
  addFilter=''
  if reportType!='':
    addFilter=addFilter+'source_system_names: ["'+reportType+'"] '
  if additionalFilter!='':
    if addFilter=='':
      addFilter=addFilter+additionalFilter+' '
    else:
      addFilter=addFilter+additionalFilter+' '
  s = Template(query)
  return s.substitute(start=period_start,end=period_end,name=entity_name,type=volume_type,
  product_type=product,add_filter=addFilter)

def get_production_volumes_for_flownames(period_start,period_end,
volume_type='',flowNames='',reportType=''):
  """
  Creates a production volumes query with the given period and tries to match entity names
  using a regex pattern
  """
  if period_start=='' or period_end=='' or reportType=='' or flowNames=='':
    raise Exception("Not all parameters required specified")
    
  addFilter=''
  query=__get_production_query_for_flow_names()
  if reportType!='':
    addFilter='source_system_names: ["'+reportType+'"]'
  
  s = Template(query)
  return s.substitute(start=period_start,end=period_end,type=volume_type,
  names=flowNames,add_filter=addFilter)



def __get_production_query_for_flow_names():
  query= '''
    query {
  production {
    data(
      start: "$start"
      end: "$end"
      report_data_subtypes: [$type]
      names:["$names"]
      $add_filter
      limit: 10000
    ) {
      sourceSystemReportName
      sourceStartTime
      sourceEndTime
      dataStartTime
      dataEndTime
      sourceEntity {
        name
        type
      }
      owningEntity {
        name
        type
      }
      dataEntity {
        name
        type
      }
      dataPeriod
      name
      type
      product
      productName
      qualifier
      volume {
        uom
        value
      }
     
      wellMeasurements {
        chokeSize {
          uom
          value
        }
        whp {
          uom
          value
        }
        wht {
          uom
          value
        }
        bhp {
          uom
          value
        }
        bht {
          uom
          value
        }
        operationTime{
          uom 
          value
        }
         annulusTemp
        {
        uom 
        value
        }
        annulusPress{
          uom 
          value 
        }
        dscp{
          uom 
          value
        }
        dsct{
          uom 
          value
        }
      }
      sourceSystemName
      sourceSystemVersion
      quality
      created
      modified
      measurements{
        mass{
          value
          unitOfMeasurement
        }
        density{
          value
          unitOfMeasurement
        }
      }
      comment
      uid
    }
   
    
  }
}
    '''
  return query



def __get_production_query_for_product():
  query= '''
    query {
  production {
    data(
      start: "$start"
      end: "$end"
      report_data_subtypes: [$type]
      entity_names: ["$name"]
      products: ["$product_type"]
      $add_filter
      limit: 10000
    ) {
      sourceSystemReportName
      sourceStartTime
      sourceEndTime
      dataStartTime
      dataEndTime
      sourceEntity {
        name
        type
      }
      owningEntity {
        name
        type
      }
      dataEntity {
        name
        type
      }
      dataPeriod
      name
      type
      product
      productName
      qualifier
      volume {
        uom
        value
      }
     
      wellMeasurements {
        chokeSize {
          uom
          value
        }
        whp {
          uom
          value
        }
        wht {
          uom
          value
        }
        bhp {
          uom
          value
        }
        bht {
          uom
          value
        }
        operationTime{
          uom 
          value
        }
         annulusTemp
        {
        uom 
        value
        }
        annulusPress{
          uom 
          value 
        }
        dscp{
          uom 
          value
        }
        dsct{
          uom 
          value
        }
      }
      sourceSystemName
      sourceSystemVersion
      quality
      created
      modified
      measurements{
        mass{
          value
          unitOfMeasurement
        }
        density{
          value
          unitOfMeasurement
        }
      }
      comment
      uid
    }
    
  }
}
    '''
  return query

def __get_production_query():
  query= '''
    query {
  production {
    data(
      start: "$start"
      end: "$end"
      report_data_subtypes: [$type]
      entity_names: ["$name"]
      $add_filter
      limit: 10000
    ) {
      sourceSystemReportName
      sourceStartTime
      sourceEndTime
      dataStartTime
      dataEndTime
      sourceEntity {
        name
        type
      }
      owningEntity {
        name
        type
      }
      dataEntity {
        name
        type
      }
      dataPeriod
      name
      type
      product
      productName
      qualifier
      volume {
        uom
        value
      }
     
      wellMeasurements {
        chokeSize {
          uom
          value
        }
        whp {
          uom
          value
        }
        wht {
          uom
          value
        }
        bhp {
          uom
          value
        }
        bht {
          uom
          value
        }
        operationTime{
          uom 
          value
        }
         annulusTemp
        {
        uom 
        value
        }
        annulusPress{
          uom 
          value 
        }
        dscp{
          uom 
          value
        }
        dsct{
          uom 
          value
        }
      }
      sourceSystemName
      sourceSystemVersion
      quality
      created
      modified
      measurements{
        mass{
          value
          unitOfMeasurement
        }
        density{
          value
          unitOfMeasurement
        }
      }
      comment
      uid
    }
    
  }
}
    '''
  return query