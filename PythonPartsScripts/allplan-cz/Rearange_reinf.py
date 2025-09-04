import sys

from BaseScriptObject import BaseScriptObject, BaseScriptObjectData
from CreateElementResult import CreateElementResult
from BuildingElement import BuildingElement
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_BaseElements as AllplanBaseElements

import NemAll_Python_Reinforcement as AllplanReinf
from TypeCollections.ModelEleList import ModelEleList
from NemAll_Python_Utility import ProgressBar

def check_allplan_version(build_ele, version):
    del build_ele
    del version
    return True

def create_script_object(build_ele: BuildingElement, script_object_data: BaseScriptObjectData) -> BaseScriptObject:
    return VyztuzScriptObject(build_ele, script_object_data)

class VyztuzScriptObject(BaseScriptObject):

    def __init__(self, build_ele: BuildingElement, script_object_data: BaseScriptObjectData):
        super().__init__(script_object_data)
        self.build_ele = build_ele
        self.run_action = False  # Flag for executing action
        self.run_action_straight = False  # Initialize here
        self.run_action_bend = False  # Initialize here
        self.merge_straight = False  # Initialize here
        self.merge_bend = False  # Initialize here
        self.run_action_shapes = False  # Initialize here
        self.run_rearrange = False  # Initialize here


    def on_control_event(self, event_id: int):
        if event_id == 1000:
            self.run_action = True
            self.run_action_straight = True
            self.run_action_bend = True
            self.merge_straight = False
            self.merge_bend = False
            self.run_action_shapes = False
            self.run_rearrange = True

        elif event_id == 1001:
            self.run_action = True
            self.run_action_straight = True
            self.run_action_bend = False
            self.merge_straight = False
            self.merge_bend = False
            self.run_action_shapes = False
            self.run_rearrange = False

        elif event_id == 1011:
            self.run_action = True
            self.run_action_straight = True
            self.run_action_bend = False
            self.merge_straight = True
            self.merge_bend = False
            self.run_action_shapes = False
            self.run_rearrange = False

        elif event_id == 1002:
            self.run_action = True
            self.run_action_bend = True
            self.run_action_straight = False
            self.merge_straight = False
            self.merge_bend = False
            self.run_action_shapes = False
            self.run_rearrange = False

        elif event_id == 1012:
            self.run_action = True
            self.run_action_bend = True
            self.run_action_straight = False
            self.merge_straight = False
            self.merge_bend = True
            self.run_action_shapes = False
            self.run_rearrange = False

        elif event_id == 2000:
            self.run_action = True
            self.run_action_bend = False
            self.run_action_straight = False
            self.merge_straight = False
            self.merge_bend = False
            self.run_action_shapes = False
            self.run_rearrange = True

        elif event_id == 3000:
            self.run_action = True
            self.run_action_bend = False
            self.run_action_straight = False
            self.merge_straight = False
            self.merge_bend = False
            self.run_action_shapes = True
            self.run_rearrange = True

        else:
            self.run_action = False
            self.run_action_straight = False
            self.run_action_bend = False
            self.merge_straight = False
            self.merge_bend = False
            self.run_action_shapes = False
            self.run_rearrange = False

    def execute(self) -> CreateElementResult:
        if self.run_action:
            all_elements = AllplanBaseElements.ElementsSelectService.SelectAllElements(self.document)
            model_ele_list = ModelEleList()

            i = self.build_ele.starting_mark_number_bend.value
            j = self.build_ele.starting_mark_number_straight.value
            start_bend = i
            start_straight = j
            sorting_bend = self.build_ele.sorting_bend.value
            sorting_bend_diameter = self.build_ele.sorting_bend_diameter.value
            sorting_straight = self.build_ele.sorting_straight.value
            sorting_straight_diameter = self.build_ele.sorting_straight_diameter.value
            round_straight = self.build_ele.round_straight.value
            round_bend = self.build_ele.round_bend.value
            lock_straight = self.build_ele.lock_straight.value
            lock_bend = self.build_ele.lock_bend.value

            if self.run_rearrange:
                AllplanReinf.ReinforcementUtil.Rearrange(
                    self.document,
                    1, 999,
                    9999, 999,
                    90000, 999,
                    0, False,
                    True,
                    False
                )
                del all_elements
                all_elements = AllplanBaseElements.ElementsSelectService.SelectAllElements(self.document)


            # --- Vyhledání a uložení rovných výztuží ---
            if self.run_action_straight:
                reinforcing_bars_straight = []
                try:
                    for element in all_elements:
                        if element is None:
                            continue
                        if element.GetElementAdapterType().GetTypeName() == "BarsDefinition_TypeUUID":
                            bar_position_data = AllplanReinf.BarPositionData(element)
                            code_count, bar_shape_codes, lengths = AllplanReinf.ReinforcementService.GetBarShapeCode(
                                element, AllplanReinf.ReinforcementService.BarShapeCodeStandard.eIso4066
                            )
                            if bar_shape_codes == [0]:
                                # Sběr prvků
                                reinforcing_bars_straight.append({
                                    'element': element,
                                    'bar_position_data': bar_position_data,
                                    'length': bar_position_data.Length,
                                    'diameter': bar_position_data.Diameter
                                })


                    # Třídění:
                    if sorting_straight_diameter:
                        reinforcing_bars_sorted = sorted(
                            reinforcing_bars_straight,
                            key=lambda x: (x['diameter'], x['length'])
                        )
                    elif sorting_straight:
                        reinforcing_bars_sorted = sorted(
                            reinforcing_bars_straight,
                            key=lambda x: x['length']
                        )
                    else:
                        reinforcing_bars_sorted = reinforcing_bars_straight

                    # for bar_info in reinforcing_bars_sorted:
                    #     bar_info.pop('diameter', None)  # Bez chyby, pokud už je odstraněn

                    pb_straight = ProgressBar(len(reinforcing_bars_sorted), 0, True)
                    pb_straight.SetTitle("Přečíslovávám přímé pruty...")


                    for bar_info in reinforcing_bars_sorted:

                        bar_position_data = bar_info['bar_position_data']
                        element = bar_info['element']
                        AllplanReinf.ReinforcementUtil.Rearrange(
                            self.document,
                            bar_position_data.GetPosition(), 99999,
                            bar_position_data.GetPosition(), 99999,
                            j, 999,
                            round_straight, lock_straight,
                            True,
                            False
                        )
                        j += 1
                        pb_straight.Step()
                    pb_straight.CloseProgressbar()

                except UnboundLocalError:
                    pass

                if self.merge_straight:
                    # Merge straight bars
                    AllplanReinf.ReinforcementUtil.Rearrange(
                        self.document,
                        start_straight, 999,
                        j, 999,
                        start_straight, 999,
                        round_straight, lock_straight,
                        True,
                        False
                    )


            # --- Vyhledání a uložení ohýbaných výztuží ---
            if self.run_action_bend:
                reinforcing_bars_bended = []
                try:
                    for element in all_elements:
                        if element is None:
                            continue
                        if element.GetElementAdapterType().GetTypeName() == "BarsDefinition_TypeUUID":
                            bar_position_data = AllplanReinf.BarPositionData(element)
                            code_count, bar_shape_codes, lengths = AllplanReinf.ReinforcementService.GetBarShapeCode(
                                element, AllplanReinf.ReinforcementService.BarShapeCodeStandard.eIso4066
                            )
                            if bar_shape_codes != [0]:
                                reinforcing_bars_bended.append({
                                    'element': element,
                                    'bar_position_data': bar_position_data,
                                    'length': bar_position_data.Length,
                                    'diameter': bar_position_data.Diameter
                                })

                    # Třídění:
                    if sorting_bend_diameter:
                        reinforcing_bars_sorted = sorted(
                            reinforcing_bars_bended,
                            key=lambda x: (x['diameter'], x['length'])
                        )
                    elif sorting_bend:
                        reinforcing_bars_sorted = sorted(
                            reinforcing_bars_bended,
                            key=lambda x: x['length']
                        )
                    else:
                        reinforcing_bars_sorted = reinforcing_bars_bended

                    # for bar_info in reinforcing_bars_sorted:
                    #     bar_info.pop('diameter', None)  # Bez chyby, pokud už je odstraněn

                    pb_bended = ProgressBar(len(reinforcing_bars_sorted), 0, True)

                    pb_bended.SetTitle("Přečíslovávám ohýbané pruty...")

                    for bar_info in reinforcing_bars_sorted:

                        bar_position_data = bar_info['bar_position_data']
                        element = bar_info['element']
                        AllplanReinf.ReinforcementUtil.Rearrange(
                            self.document,
                            bar_position_data.GetPosition(), 999,
                            bar_position_data.GetPosition(), 999,
                            i, 999,
                            round_bend, lock_bend,
                            True,
                            False
                        )
                        i += 1
                        pb_bended.Step()

                    pb_bended.CloseProgressbar()

                except UnboundLocalError:
                    pass

                if self.merge_bend:
                    # Merge bent bars
                    AllplanReinf.ReinforcementUtil.Rearrange(
                        self.document,
                        start_bend, 999,
                        i, 999,
                        start_bend, 999,
                        round_bend, lock_bend,
                        True,
                        False
                    )

            if self.run_action_shapes:
                # AllplanReinf.ReinforcementUtil.Rearrange(
                #     self.document,
                #     1, 999,
                #     9999, 999,
                #     90000, 999,
                #     0, False,
                #     True,
                #     False
                # )
                # del all_elements
                # all_elements = AllplanBaseElements.ElementsSelectService.SelectAllElements(self.document)

                reinforcing_bars_all = []
                i=1
                for element in all_elements:
                    if element is None:
                        continue
                    if element.GetElementAdapterType().GetTypeName() == "BarsDefinition_TypeUUID":
                        bar_position_data = AllplanReinf.BarPositionData(element)
                        code_count, bar_shape_codes, lengths = AllplanReinf.ReinforcementService.GetBarShapeCode(
                            element, AllplanReinf.ReinforcementService.BarShapeCodeStandard.eIso4066
                        )

                        reinforcing_bars_all.append({
                            'element': element,
                            'bar_position_data': bar_position_data,
                            'length': bar_position_data.Length,
                            'diameter': bar_position_data.Diameter,
                            'shape_code': bar_shape_codes if bar_shape_codes else 0
                        })

                reinforcing_bars_sorted = sorted(
                    reinforcing_bars_all,
                    key=lambda x: (x['shape_code'], x['diameter'], x['length'])
                )

                pb_all = ProgressBar(len(reinforcing_bars_sorted), 0, True)

                pb_all.SetTitle("Přečíslovávám všechny pruty...")

                for bar_info in reinforcing_bars_sorted:

                    bar_position_data = bar_info['bar_position_data']
                    element = bar_info['element']
                    AllplanReinf.ReinforcementUtil.Rearrange(
                        self.document,
                        bar_position_data.GetPosition(), 999,
                        bar_position_data.GetPosition(), 999,
                        i, 999,
                        round_bend, lock_bend,
                        True,
                        False
                    )
                    i += 1
                    pb_all.Step()

                pb_all.CloseProgressbar()


            self.run_action = False
            return CreateElementResult(elements=model_ele_list, placement_point=AllplanGeo.Point2D(0, 0))
        else:
            return CreateElementResult(elements=[], placement_point=AllplanGeo.Point2D(0, 0))
