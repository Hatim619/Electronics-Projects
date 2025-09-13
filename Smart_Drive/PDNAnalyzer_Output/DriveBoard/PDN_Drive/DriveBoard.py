designFile = "D:/Proffesional/Learning/Motor Driver/Design Files/Smart_Drive/PDNAnalyzer_Output/DriveBoard/odb.tgz"

powerNets = ["Vin_L", "VA", "VM_L", "VL-", "Vin_R", "VB", "VM_R_", "VR-"]

groundNets = ["GND", "SP_L", "VL+", "SP_R", "VR+"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("pdna_comp_Motor_A_PWR_IN_3", "1") ],
"ground_pins": [ ("pdna_comp_Motor_A_PWR_IN_3", "2") ],
"voltage": 34,
"Rpin": 0.01,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("pdna_comp_Motor_A_PWR_OUT_4", "1") ],
"ground_pins": [ ("pdna_comp_Motor_A_PWR_OUT_4", "2") ],
"current": 10,
"Rpin": 0.01,
}
,
{
"id": "2",
"type": "source",
"power_pins": [ ("pdna_comp_Motor_B_PWR_IN_2", "1") ],
"ground_pins": [ ("pdna_comp_Motor_B_PWR_IN_2", "2") ],
"voltage": 34,
"Rpin": 0.01,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("pdna_comp_Motor_B_PWR_OUT_1", "1") ],
"ground_pins": [ ("pdna_comp_Motor_B_PWR_OUT_1", "2") ],
"current": 10,
"Rpin": 0.01,
}
]


voltage_regulators = [
{
"id": "4",
"type": "linear",

"in": [ ("F1", "1") ],
"out": [ ("F1", "2") ],
"ref": [],

"v2": -0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0025,
}
,
{
"id": "5",
"type": "linear",

"in": [ ("FET1", "3") ],
"out": [ ("FET1", "2") ],
"ref": [],

"v2": -0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0025,
}
,
{
"id": "6",
"type": "linear",

"in": [ ("FET3", "2") ],
"out": [ ("FET3", "3") ],
"ref": [],

"v2": -0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0025,
}
,
{
"id": "7",
"type": "linear",

"in": [ ("R7", "1") ],
"out": [ ("R7", "2") ],
"ref": [],

"v2": -0.15,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0075,
}
,
{
"id": "8",
"type": "linear",

"in": [ ("FET4", "3") ],
"out": [ ("FET4", "2") ],
"ref": [],

"v2": -0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0025,
}
,
{
"id": "9",
"type": "linear",

"in": [ ("R17", "1") ],
"out": [ ("R17", "2") ],
"ref": [],

"v2": -0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0075,
}
,
{
"id": "10",
"type": "linear",

"in": [ ("FET9", "3") ],
"out": [ ("FET9", "2") ],
"ref": [],

"v2": -0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0025,
}
,
{
"id": "11",
"type": "linear",

"in": [ ("F2", "1") ],
"out": [ ("F2", "2") ],
"ref": [],

"v2": -0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0025,
}
,
{
"id": "12",
"type": "linear",

"in": [ ("FET6", "3") ],
"out": [ ("FET6", "2") ],
"ref": [],

"v2": -0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0025,
}
,
{
"id": "13",
"type": "linear",

"in": [ ("FET8", "2") ],
"out": [ ("FET8", "3") ],
"ref": [],

"v2": -0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0025,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 2.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.8, 'Thickness': 0.0016},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 2.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
