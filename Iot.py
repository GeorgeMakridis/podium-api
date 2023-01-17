class Iot:

    def __init__(self, vessel_code=None, airCoolerCWInLETPress= None, scavAirFireDetTempNo1= None, scavAirFireDetTempNo2= None, scavAirFireDetTempNo3= None, scavAirFireDetTempNo4= None,
                 scavAirFireDetTempNo5= None, scavAirFireDetTempNo6= None, scavAirFireDetTempNo7= None, scavAirFireDetTempNo8= None, scavAirFireDetTempNo9= None, scavAirFireDetTempNo10= None,
                 scavAirFireDetTempNo11= None, scavAirFireDetTempNo12= None, coolerCWinTemp= None, cfWInPress= None, controlAirPress= None, cylLoTemp= None, exhVVSpringAirInPress= None,
                 foFlow= 0.0, foInPress= None, foInTemp= None, hfoViscocityHighLow= None, hpsBearingTemp= None, jcfWInTempLow= None, cylExhGasOutTempNo1= None, cylExhGasOutTempNo2= None,
                 cylExhGasOutTempNo3= None, cylExhGasOutTempNo4= None, cylExhGasOutTempNo5= None, cylExhGasOutTempNo6= None, cylExhGasOutTempNo7= None, cylExhGasOutTempNo8= None,
                 cylExhGasOutTempNo9= None, cylExhGasOutTempNo10= None, cylExhGasOutTempNo11= None, cylExhGasOutTempNo12= None, cylJCFWOutTempNo1= None, cylJCFWOutTempNo2= None,
                 cylJCFWOutTempNo3= None, cylJCFWOutTempNo4= None, cylJCFWOutTempNo5= None, cylJCFWOutTempNo6= None, cylJCFWOutTempNo7= None, cylJCFWOutTempNo8= None, cylJCFWOutTempNo9= None,
                 cylJCFWOutTempNo10= None, cylJCFWOutTempNo11= None, cylJCFWOutTempNo12= None, cylPistonCOOutTempNo1= None, cylPistonCOOutTempNo2= None, cylPistonCOOutTempNo3= None,
                 cylPistonCOOutTempNo4= None, cylPistonCOOutTempNo5= None, cylPistonCOOutTempNo6= None, cylPistonCOOutTempNo7= None, cylPistonCOOutTempNo8= None, cylPistonCOOutTempNo9= None,
                 cylPistonCOOutTempNo10= None, cylPistonCOOutTempNo11= None, cylPistonCOOutTempNo12= None, tcExhGasInTempNo1= None, tcExhGasInTempNo2= None, tcExhGasInTempNo3= None, tcExhGasInTempNo4= None,
                 tcExhGasOutTempNo1= None, tcExhGasOutTempNo2= None, tcExhGasOutTempNo3= None, tcExhGasOutTempNo4= None, tcLOInLETPressNo1= None, tcLOInLETPressNo2= None, tcLOInLETPressNo3= None,
                 tcLOInLETPressNo4= None, tcLOOutLETTempNo1= None, tcLOOutLETTempNo2= None, tcLOOutLETTempNo3= None, tcLOOutLETTempNo4= None, tcRPMNo1= None, tcRPMNo2= None, tcRPMNo3= None, tcRPMNo4= None,
                 orderRPMBridgeLeverer= None, RPM= None, scavAirInLetPress= None, scavAirReceiverTemp= None, startAirPress= None, thrustPadTemp= None, mainLOInLetPress= None, mainLOInTemp= None,
                 foTemperature= None, foTotVolume= 3.0, POWER= None, scavengeAirPressure= None, TORQUE= None, coolingWOutLETTempNo1= None, coolingWOutLETTempNo2= None, coolingWOutLETTempNo3= None,
                 coolingWOutLETTempNo4= None, foVolConsumption= 0.0, foConsumption= None, foID= None):

            self.vessel_code = vessel_code
            self.airCoolerCWInLETPress = airCoolerCWInLETPress
            self.scavAirFireDetTempNo1 = scavAirFireDetTempNo1
            self.scavAirFireDetTempNo2 = scavAirFireDetTempNo2
            self.scavAirFireDetTempNo3 = scavAirFireDetTempNo3
            self.scavAirFireDetTempNo4 = scavAirFireDetTempNo4
            self.scavAirFireDetTempNo5 = scavAirFireDetTempNo5
            self.scavAirFireDetTempNo6 = scavAirFireDetTempNo6
            self.scavAirFireDetTempNo7 = scavAirFireDetTempNo7
            self.scavAirFireDetTempNo8 = scavAirFireDetTempNo8
            self.scavAirFireDetTempNo9 = scavAirFireDetTempNo9
            self.scavAirFireDetTempNo10 = scavAirFireDetTempNo10
            self.scavAirFireDetTempNo11 = scavAirFireDetTempNo11
            self.scavAirFireDetTempNo12 = scavAirFireDetTempNo12
            self.coolerCWinTemp = coolerCWinTemp
            self.cfWInPress = cfWInPress
            self.controlAirPress = controlAirPress
            self.cylLoTemp = cylLoTemp
            self.exhVVSpringAirInPress = exhVVSpringAirInPress
            self.foFlow = foFlow
            self.foInPress = foInPress
            self.foInTemp = foInTemp
            self.hfoViscocityHighLow = hfoViscocityHighLow
            self.hpsBearingTemp = hpsBearingTemp
            self.jcfWInTempLow = jcfWInTempLow
            self.cylExhGasOutTempNo1 = cylExhGasOutTempNo1
            self.cylExhGasOutTempNo2 = cylExhGasOutTempNo2
            self.cylExhGasOutTempNo3 = cylExhGasOutTempNo3
            self.cylExhGasOutTempNo4 = cylExhGasOutTempNo4
            self.cylExhGasOutTempNo5 = cylExhGasOutTempNo5
            self.cylExhGasOutTempNo6 = cylExhGasOutTempNo6
            self.cylExhGasOutTempNo7 = cylExhGasOutTempNo7
            self.cylExhGasOutTempNo8 = cylExhGasOutTempNo8
            self.cylExhGasOutTempNo9 = cylExhGasOutTempNo9
            self.cylExhGasOutTempNo10 = cylExhGasOutTempNo10
            self.cylExhGasOutTempNo11 = cylExhGasOutTempNo11
            self.cylExhGasOutTempNo12 = cylExhGasOutTempNo12
            self.cylJCFWOutTempNo1 = cylJCFWOutTempNo1
            self.cylJCFWOutTempNo2 = cylJCFWOutTempNo2
            self.cylJCFWOutTempNo3 = cylJCFWOutTempNo3
            self.cylJCFWOutTempNo4 = cylJCFWOutTempNo4
            self.cylJCFWOutTempNo5 = cylJCFWOutTempNo5
            self.cylJCFWOutTempNo6 = cylJCFWOutTempNo6 
            self.cylJCFWOutTempNo7 = cylJCFWOutTempNo7
            self.cylJCFWOutTempNo8 = cylJCFWOutTempNo8 
            self.cylJCFWOutTempNo9 = cylJCFWOutTempNo9
            self.cylJCFWOutTempNo10 = cylJCFWOutTempNo10 
            self.cylJCFWOutTempNo11 = cylJCFWOutTempNo11
            self.cylJCFWOutTempNo12 = cylJCFWOutTempNo12
            self.cylPistonCOOutTempNo1 = cylPistonCOOutTempNo1
            self.cylPistonCOOutTempNo2 = cylPistonCOOutTempNo2 
            self.cylPistonCOOutTempNo3 = cylPistonCOOutTempNo3
            self.cylPistonCOOutTempNo4 = cylPistonCOOutTempNo4 
            self.cylPistonCOOutTempNo5 = cylPistonCOOutTempNo5 
            self.cylPistonCOOutTempNo6 = cylPistonCOOutTempNo6 
            self.cylPistonCOOutTempNo7 = cylPistonCOOutTempNo7
            self.cylPistonCOOutTempNo8 = cylPistonCOOutTempNo8 
            self.cylPistonCOOutTempNo9 = cylPistonCOOutTempNo9
            self.cylPistonCOOutTempNo10 = cylPistonCOOutTempNo10 
            self.cylPistonCOOutTempNo11 = cylPistonCOOutTempNo11
            self.cylPistonCOOutTempNo12 = cylPistonCOOutTempNo12
            self.tcExhGasInTempNo1 = tcExhGasInTempNo1
            self.tcExhGasInTempNo2 = tcExhGasInTempNo2 
            self.tcExhGasInTempNo3 = tcExhGasInTempNo3 
            self.tcExhGasInTempNo4 = tcExhGasInTempNo4
            self.tcExhGasOutTempNo1 = tcExhGasOutTempNo1
            self.tcExhGasOutTempNo2 = tcExhGasOutTempNo2 
            self.tcExhGasOutTempNo3 = tcExhGasOutTempNo3 
            self.tcExhGasOutTempNo4 = tcExhGasOutTempNo4
            self.tcLOInLETPressNo1 = tcLOInLETPressNo1
            self.tcLOInLETPressNo2 = tcLOInLETPressNo2 
            self.tcLOInLETPressNo3 = tcLOInLETPressNo3
            self.tcLOInLETPressNo4 = tcLOInLETPressNo4
            self.tcLOOutLETTempNo1 = tcLOOutLETTempNo1
            self.tcLOOutLETTempNo2 = tcLOOutLETTempNo2 
            self.tcLOOutLETTempNo3 = tcLOOutLETTempNo3
            self.tcLOOutLETTempNo4 = tcLOOutLETTempNo4
            self.tcRPMNo1 = tcRPMNo1
            self.tcRPMNo2 = tcRPMNo2 
            self.tcRPMNo3 = tcRPMNo3 
            self.tcRPMNo4 = tcRPMNo4
            self.orderRPMBridgeLeverer = orderRPMBridgeLeverer
            self.RPM = RPM
            self.scavAirInLetPress = scavAirInLetPress 
            self.scavAirReceiverTemp = scavAirReceiverTemp 
            self.startAirPress = startAirPress
            self.thrustPadTemp = thrustPadTemp 
            self.mainLOInLetPress = mainLOInLetPress 
            self.mainLOInTemp = mainLOInTemp
            self.foTemperature = foTemperature 
            self.foTotVolume = foTotVolume 
            self.POWER = POWER
            self.scavengeAirPressure = scavengeAirPressure
            self.TORQUE = TORQUE
            self.coolingWOutLETTempNo1 = coolingWOutLETTempNo1
            self.coolingWOutLETTempNo2 = coolingWOutLETTempNo2 
            self.coolingWOutLETTempNo3 = coolingWOutLETTempNo3
            self.coolingWOutLETTempNo4 = coolingWOutLETTempNo4
            self.foVolConsumption = foVolConsumption
            self.foConsumption = foConsumption
            self.foID = foID

