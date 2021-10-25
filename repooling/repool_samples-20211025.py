
from opentrons import protocol_api

metadata = {
    'apiLevel': '2.5',
    'author': 'Jon Sanders'}

def run(protocol: protocol_api.ProtocolContext):
    
    # define deck positions and labware
    
    # tips
    tiprack_20f = protocol.load_labware('opentrons_96_filtertiprack_20ul', 9)
    
    # tubes
    tuberack_11 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 11)
    
    # initialize pipettes
    pipette = protocol.load_instrument('p20_single_gen2', 
                                            'right',
                                            tip_racks=[tiprack_20f])
                                            
    # plates

    # Plate BBE25-27_BSM27
    library1 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 1, 'BBE25-27_BSM27')

    # Plate BSM35A_YS35
    library2 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2, 'BSM35A_YS35')

    # Plate YS-35-2a
    library3 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 3, 'YS-35-2a')

    # Plate YS-35-2b
    library4 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 4, 'YS-35-2b')

    # Plate MG_test
    library5 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 5, 'MG_test')

    # Transfer library1 high samples
    pipette.consolidate([8.90, 5.50, 9.60, 10.00, 1.70, 8.40, 1.20, 9.40, 5.20, 10.30, 6.40, 14.90, 10.40, 1.10, 2.20, 2.70, 2.00, 1.60, 7.20, 6.50, 7.30, 13.70, 6.30, 6.50, 5.90, 10.60, 8.20, 5.90, 12.90, 13.70, 11.70, 4.50, 5.80, 10.50, 12.80, 9.60, 11.30, 3.10, 6.60, 8.50],
                        [library1.wells_by_name()[well_name] for well_name in ['E1', 'F1', 'C3', 'D3', 'F3', 'G3', 'A4', 'B4', 'F4', 'G4', 'H4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'B7', 'E7', 'F7', 'B8', 'D8', 'F8', 'A9', 'B9', 'G9', 'A10', 'B10', 'D10', 'H10', 'G11', 'E12']],
                        tuberack_11['A1'])

    # Transfer library1 low samples
    pipette.consolidate([20.00, 8.90, 13.60, 7.90, 20.00, 1.90, 1.60, 18.80, 1.80, 2.20, 1.70, 20.00, 1.80, 2.80, 1.60, 2.20, 3.00, 1.80, 3.60, 3.30, 1.90, 3.60, 1.80, 2.00, 3.20, 2.60, 1.70, 6.30, 1.60, 2.00, 20.00, 1.80, 4.30, 1.80, 1.60, 2.10, 2.00, 2.40, 7.00, 4.90, 4.00],
                        [library1.wells_by_name()[well_name] for well_name in ['B1', 'D1', 'H1', 'A3', 'B3', 'E3', 'C4', 'D4', 'E4', 'G6', 'H6', 'C7', 'D7', 'G7', 'H7', 'A8', 'E8', 'G8', 'H8', 'C9', 'D9', 'E9', 'F9', 'H9', 'C10', 'E10', 'F10', 'G10', 'B11', 'C11', 'D11', 'E11', 'F11', 'H11', 'A12', 'B12', 'C12', 'D12', 'F12', 'G12', 'H12']],
                        tuberack_11['B1'])

    # Transfer library2 high samples
    pipette.consolidate([9.80, 13.90, 13.70, 14.80, 13.60, 13.90, 8.20, 14.10, 13.70, 11.50, 11.50, 11.50, 14.90, 6.10, 11.40, 11.50, 9.50, 14.80, 0.60, 1.10],
                        [library2.wells_by_name()[well_name] for well_name in ['G1', 'A3', 'B3', 'F3', 'G3', 'C4', 'H4', 'B5', 'C5', 'E5', 'G5', 'H5', 'A6', 'H6', 'B7', 'F7', 'B8', 'D8', 'E10', 'F10']],
                        tuberack_11['A2'])

    # Transfer library2 low samples
    pipette.consolidate([1.90, 1.90, 2.10, 19.70, 4.60, 1.90, 11.00, 1.60, 1.70, 2.30, 2.20, 3.10, 20.00, 3.50, 2.30, 2.40, 2.00, 1.70, 2.10, 2.80, 1.80, 2.90, 1.70, 1.70, 1.90, 2.70, 2.90, 2.40, 1.50, 1.80, 13.50, 1.80, 19.20, 4.40, 20.00, 13.70, 12.60, 20.00, 4.20, 20.00, 20.00, 14.20, 13.20, 20.00, 20.00, 20.00, 9.80, 3.80, 20.00, 20.00, 2.70, 6.00, 15.20, 6.20, 9.60],
                        [library2.wells_by_name()[well_name] for well_name in ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'H1', 'B2', 'D2', 'E2', 'G2', 'C3', 'D3', 'E3', 'H3', 'A4', 'D4', 'E4', 'F4', 'G4', 'D5', 'F5', 'B6', 'E6', 'F6', 'A7', 'E7', 'G7', 'H7', 'A8', 'C8', 'F8', 'A9', 'C9', 'D9', 'E9', 'F9', 'H9', 'A10', 'B10', 'C10', 'D10', 'H10', 'B11', 'C11', 'D11', 'E11', 'G11', 'H11', 'B12', 'D12', 'E12', 'F12', 'G12', 'H12']],
                        tuberack_11['B2'])

    # Transfer library3 high samples
    pipette.consolidate([3.80, 1.20, 5.40, 6.40, 2.90, 3.40, 0.90, 2.40, 3.60, 12.70, 9.50, 7.70, 12.80, 1.10, 14.40, 1.40, 9.70, 1.00, 14.40, 12.90, 1.00, 2.10, 10.70, 13.30, 12.90, 1.30, 13.60],
                        [library3.wells_by_name()[well_name] for well_name in 
                        ['A1', 'B1', 'D1', 'H1', 'A2', 'C2', 'D2', 'E2', 'F2',  'G2', 'H2', 'B3',  'C3', 'D3',  'E3', 'F3', 'G3', 'H3',  'C4',  'D4', 'F4', 'G4',  'H4',  'A5',  'B5', 'C5',  'F5']],
                        tuberack_11['A3'])

    # Transfer library3 low samples
    pipette.consolidate([1.50, 2.10, 2.70, 2.30, 2.30, 2.50, 5.80, 4.20, 5.00, 2.30, 2.70, 5.50, 2.90],
                        [library3.wells_by_name()[well_name] for well_name in 
                        ['C1', 'E1', 'F1', 'G1', 'B2', 'A3', 'A4', 'B4', 'E4', 'D5', 'E5', 'G5', 'H5']],
                        tuberack_11['B3'])

    # Transfer library4 high samples
    pipette.consolidate([12.70, 9.20, 7.40, 1.80, 7.10, 1.70, 1.10, 1.40, 2.20, 14.50, 12.30, 11.00],
                        [library4.wells_by_name()[well_name] for well_name in 
                        ['A6', 'B6', 'C6', 'E6', 'A7', 'E7', 'C8', 'A9', 'F9', 'B10', 'B11', 'C11']],
                        tuberack_11['A3'])

    # Transfer library4 low samples
    pipette.consolidate([2.60, 5.00, 6.00, 4.00, 2.80, 3.30, 3.20, 20.00, 4.00, 5.50, 6.50, 1.80, 3.00, 14.40, 9.70, 19.10, 5.90, 1.90, 2.40, 5.90, 8.90, 12.20, 6.20, 8.90, 1.80, 5.00, 14.80, 8.40, 14.40, 5.70, 6.70, 3.50, 17.20, 4.50, 13.00, 2.70, 4.70, 2.10, 2.90, 10.40, 18.20, 5.30, 8.60],
                        [library4.wells_by_name()[well_name] for well_name in 
                        ['D6', 'F6', 'G6', 'H6', 'B7', 'C7', 'D7', 'F7', 'G7', 'H7', 'A8', 'B8', 'D8', 'E8', 'F8', 'G8', 'H8', 'B9', 'C9', 'D9', 'E9', 'G9', 'H9', 'A10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 'A11', 'D11', 'E11', 'F11', 'G11', 'H11', 'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12']],
                        tuberack_11['B3'])

    # Transfer library5 high samples
    pipette.consolidate([0.80, 1.10, 1.50, 14.90, 1.00, 1.20, 0.90, 0.90, 1.00, 0.70, 0.80, 0.80, 0.70, 1.70, 1.50, 1.10, 1.00, 0.80, 1.60, 2.20, 0.80, 0.90, 0.80, 0.70, 1.10, 0.70, 0.90, 0.80, 0.70, 0.80, 1.00, 0.60],
                        [library5.wells_by_name()[well_name] for well_name in ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'B2', 'D2', 'E2', 'G2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'A4', 'D4', 'E4', 'F4', 'G4', 'H4', 'B5', 'C5', 'D5', 'A6', 'B6', 'E6', 'F6', 'H6']],
                        tuberack_11['A4'])

    # Transfer library5 low samples
    pipette.consolidate([5.80],
                        [library5.wells_by_name()[well_name] for well_name in ['C4']],
                        tuberack_11['B4'])
