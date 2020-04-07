from string import Template


def get_drilling_activity_query(period_start,period_end,wellborename):
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
   
def get_drilling_status_info_query(period_start,period_end,wellborename):
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