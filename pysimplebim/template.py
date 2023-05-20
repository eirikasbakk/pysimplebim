from .common import Common
from .constraints import Resources_s as r_s, Model_s as m_s, ModelView_s as mv_s, Validation_s as v_s, Enrichment_s as e_s, Subtitution_s as s_s, Groups_s as g_s



class Resources(Common):
    """
    Functions in this class:\n
    Add Identity (for IFC PropertySet)
    """

    def __init__(self, workbook):
        super().__init__(workbook)
        self.wb.active = self.wb["Resources"]
        self.ws = self.wb.active

        self.functions = ["add_identity_for_ifc_propertyset"]

    # TODO Add Identity Source

    # TODO Add Identity
    
    def add_identity_for_ifc_propertyset(self, identity_source_key=None, identity_key=None, name=None, description=None, reference=None, propertyset_name=None, property_name=None, property_type=None ):
        """
        Required inputs:\n
        \t-identity_key\n
        \t-name\n 
        \t-propertyset_name\n
        \t-property_name\n
        Documentation on tool: #
        """
        dictionary= r_s.dict_add_identity_for_ifc_propertyset 
        
        function_name = "Add Identity (for IFC PropertySet)"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.add_identity_for_ifc_propertyset)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None


    # TODO Add Identity (for IFC Element Quantity)

    # TODO  Add Identity Metadata
   

class Model(Common):
    """
    Functions in this class:\n
    \t-Add Identity to Object\n
    \t-Add Property to Object Class or Group\n
    \t-Add Identity to Property\n
    \t-Swap Property Values\n
    \t-Trim Text Property Values (before copy)\n
    \t-Find and Replace Text Property Values (before copy)\n
    \t-Set Property Values Based on Text Property Value (before copy)\n
    \t-Copy Property Values\n
    \t-Trim Text Property Values (after copy)\n
    \t-Find and Replace Text Property Values (after copy)\n
    \t-Set Property Values Based on Text Property Value (after copy)
    """

    def __init__(self, workbook):
        super().__init__(workbook)
        self.wb.active = self.wb["Model"]
        self.ws = self.wb.active

        self.functions = ["add_identity_to_object", 
                          "add_property_to_object_class_or_group",
                          "add_identity_to_property",
                          "swap_property_values",
                          "trim_text_property_values_before_copy",
                          "find_and_replace_text_property_values_before_copy",
                          "set_property_values_based_on_text_property_values_before_copy",
                          "copy_property_values",
                          "trim_text_property_values_after_copy",
                          "find_and_replace_text_property_values_after_copy",
                          "set_property_values_based_on_text_property_values_after_copy"
                          ]

    # Add Identity to Object
    def add_identity_to_object(self, object=None, identity_to_add=None, make_default=None):
        """
        Required inputs:\n
        \t-object\n
        \t-identity_to_add\n
        Documentation on tool: #"""
        dictionary = m_s.dict_add_identity_to_object
        function_name = "Add Identity to Object"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.add_identity_to_object)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None
  

    # Add Property to Object Class or Group
    def add_property_to_object_class_or_group(self, object_or_group=None, property=None, property_type=None, single_list=None, unit_symbol=None):
        """
        Required inputs:\n
        \t-object_or_group\n
        \t-property\n
        \t-property_type\n
        Documentation on tool: #
        """
        dictionary= m_s.dict_add_property_to_object_class_or_group
        function_name = "Add Property to Object Class or Group"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.add_property_to_object_class_or_group)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None


    #Add Identity to Property
    def add_identity_to_property(self, object, existing_property, identity_to_add, make_default):
        """
        Required inputs:\n
        \t-object\n
        \t-existing_property\n
        \t-identity_to_add\n
        Documentation on tool: #
        """
        dictionary= m_s.dict_add_identity_to_property
        function_name = "Add Identity to Property"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.add_identity_to_property)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None
    

    #Swap Property Values
    def swap_property_values(self, object=None, property_1=None, property_2=None):
        """
        Required inputs:\n
        \t-object\n 
        \t-property_1\n 
        \t-property_2\n
        Documentation on tool: #
        """
        dictionary= m_s.dict_swap_property_values
        function_name = "Swap Property Values"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.swap_property_values)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None

    #Trim Text Property Values (before copy)
    def trim_text_property_values_before_copy(self, object_or_group=None, trim_property=None, trim_type=None, case_sensitive=None, text_to_trim=None):
        """
        Required inputs:\n
        \t-object_or_group\n 
        \t-trim_property\n
        \t-trim_type\n
        \t-text_to_trim\n
        Documentation on tool: #
        """
        dictionary= m_s.dict_trim_text_property_values_before_copy
        function_name = "Trim Text Property Values (before copy)"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.trim_text_property_values_before_copy)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None

    #Find and Replace Text Property Values (before copy)
    def find_and_replace_text_property_values_before_copy(self, object_or_group=None, find_property=None, text_operator=None, find_value=None, replace_value=None, replace_type=None):
        """
        Required inputs:\n
        \t-object_or_group\n
        \t-find_property\n 
        \t-text_property\n
        Documentation on tool: #
        """
        dictionary= m_s.dict_find_and_replace_text_property_values_before_copy
        function_name = "Find and Replace Text Property Values (before copy)"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.find_and_replace_text_property_values_before_copy)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None

    #Set Property Values Based on Text Property Value (before copy)
    def set_property_values_based_on_text_property_values_before_copy(self, object_or_group=None, find_property=None, text_operator=None, find_value=None, set_property=None, set_value=None):
        """
        Required inputs:\n
        \t-object_or_group\n
        \t-set_property\n
        \t-set_value\n
        Documentation on tool: #
        """
        dictionary= m_s.dict_set_property_values_based_on_text_property_values_before_copy
        function_name = "Set Property Values Based on Text Property Value (before copy)"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.set_property_values_based_on_text_property_values_before_copy)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None

    #Copy Property Values
    def copy_property_values(self, object_or_group=None,from_property=None, to_property=None, copy_empty_values=None, overwrite_non_empty_values=None, regular_expression=None):
        """
        required inputs:\n
        \t-object_or_group\n
        \t-from_property\n
        \t-to_property\n
        Documentation on tool: #
        """
        dictionary = m_s.dict_copy_property_values
        function_name = "Copy Property Values"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.copy_property_values)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None

    #Trim Text Property Values (after copy)
    def trim_text_property_values_after_copy(self, object_or_group=None, trim_property=None, trim_type=None, case_sensitive=None, text_to_trim=None):
        """
        Required inputs:\n
        \t-object_or_group\n
        \t-trim_property\n
        \t-trim_type\n
        \t-text_to_trim\n
        Documentation on tool: #
        """
        dictionary= m_s.dict_trim_text_property_values_before_copy
        function_name = "Trim Text Property Values (after copy)"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.trim_text_property_values_after_copy)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None

    #Find and Replace Text Property Values (after copy)
    def find_and_replace_text_property_values_after_copy(self, object_or_group=None, find_property=None, text_operator=None, find_value=None, replace_value=None, replace_type=None):
        """
        Required inputs:\n
        \t-object_or_group\n
        \t-find_property\n
        \t-text_property\n
        Documentation on tool: #
        """
        dictionary= m_s.dict_find_and_replace_text_property_values_after_copy
        function_name = "Find and Replace Text Property Values (after copy)"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.find_and_replace_text_property_values_after_copy)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None

    #Set Property Values Based on Text Property Value (after copy)
    def set_property_values_based_on_text_property_values_after_copy(self, object_or_group=None, find_property=None, text_operator=None, find_value=None, set_property=None, set_value=None):
        """
        Required inputs:\n
        \t-object_or_group\n
        \t-set_property,set_value\n
        Documentation on tool: #
        """
        dictionary= m_s.dict_set_property_values_based_on_text_property_values_after_copy
        function_name = "Set Property Values Based on Text Property Value (after copy)"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.set_property_values_based_on_text_property_values_after_copy)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None

    #Rotate Site Around Pivot Point
    #TODO

    #Move and Rotate Site
    #TODO

    #Move and Rotate Project
    #TODO



class ModelView(Common):
    """
    Functions in this class:\n
    Include/Exclude Objects Based on Object Class or Group\n
    Include/Exclude Property\n
    Set Object Color and Transparency Based on Object Class or Group
    """
    def __init__(self, workbook):
        super().__init__(workbook)
        self.wb.active = self.wb["ModelView"]
        self.ws = self.wb.active

        self.functions = ["include_exclude_objects_based_on_object_class_or_group",
                          "include_exclude_property",
                          "set_object_color_and_transparency_based_on_object_class_or_group"]
    
    def include_exclude_objects_based_on_object_class_or_group(self, object_or_group=None, include=None):
        """
        Required inputs:\n
        \t-object_or_group\n
        \t-include\n

        Documentation on tool: #
        """
        dictionary = mv_s.dict_include_exclude_objects_based_on_object_class_or_group
        function_name = "Include/Exclude Objects Based on Object Class or Group"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.include_exclude_objects_based_on_object_class_or_group)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None
    
    
    def include_exclude_property(self, object=None, property=None, include=None):
        """
        Required inputs:\n
        \t-object\n 
        \t-property\n 
        \t-include\n
        Documentation on tool: #
        """
        dictionary = mv_s.dict_include_exclude_property
        function_name = "Include/Exclude Property"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.include_exclude_property)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None
    

    def set_object_color_and_transparency_based_on_object_class_or_group(self, object_or_group=None, color=None, transparency:int=None):
        """
        Required inputs:\n
        \t-object_or_group\n
        Documentation on tool: #
        """
        dictionary = mv_s.dict_set_object_color_and_transparency_based_on_object_class_or_group
        function_name = "Set Object Color and Transparency Based on Object Class or Group"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.set_object_color_and_transparency_based_on_object_class_or_group)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None
    

class Validation(Common):
    """
    Functions in this class:\n
    Required Objects\n
    Required Properties\n
    Rules for Text Property Values
    """
    def __init__(self, workbook):
        super().__init__(workbook)
        self.wb.active = self.wb["Validation"]
        self.ws = self.wb.active

        self.functions = ["required_objects",
                          "required_properties",
                          "rules_for_text_property_values"]
    
    def required_objects(self, object_or_group=None, requirement=None):
        """
        Required input:\n
        \t-object_or_group\n
        Documentation on tool: #
        """
        dictionary = v_s.dict_required_objects
        function_name = "Required Objects"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.required_objects)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None


    def required_properties(self, object_or_group=None, property=None, yes_no=None):
        """
        Required input:\n
        \t-object_or_group\n 
        \t-property\n
        Documentation on tool: #
        """
        dictionary = v_s.dict_required_properties
        function_name = "Required Properties"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.required_properties)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None


    def rules_for_text_property_values(self, object_or_group=None, text_property=None, rule_for_text_property=None, case_sensitive=None, allow_empty=None, separator=None, value=None):
        """
        Required input:\n
        \t-object_or_group\n
        \t-text_property\n
        \t-value\n
        Documentation on tool: #
        """
        dictionary = v_s.dict_rules_for_text_property_values
        function_name = "Rules for Text Property Values"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.rules_for_text_property_values)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None
 

class Enrichment(Common):
    def __init__(self, workbook):
        super().__init__(workbook)
        self.wb.active = self.wb["Enrichment"]
        self.ws = self.wb.active

        self.functions = []
    
    def copy_section(self):
        """Copy the sample section to an empty space"""
        # TODO
        pass

    def expand_function(self):
        """Expand the function with more columns"""
        #TODO
        pass
    
    def enrich(self, group):
        #TODO
        pass


class Substitution(Common):
    """
    Functions in this class:\n
    Substitution Lists\n
    """
    def __init__(self, workbook):
        super().__init__(workbook)
        self.wb.active = self.wb["Substitution"]
        self.ws = self.wb.active

        self.functions = ["substitution_lists"]
    
    def substitution_lists(self, list_name=None, list_values=None):
        """
        Required inputs:\n
        \t-list_name\n
        \t-list_values\n

        Documentation on tool: #
        """
        dictionary = s_s.dict_substitution_list
        function_name = "Substitution Lists"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.substitution_lists)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None
    

class Groups(Common):
    """
    Functions in this class:\n
    Define Groups Based on Property Values
    """
    def __init__(self, workbook):
        super().__init__(workbook)
        self.wb.active = self.wb["Groups"]
        self.ws = self.wb.active

        self.functions = ["define_groups_based_on_property_values",
                          "assign_groups_to_group_categories"
                          ]
    
    # TODO
    # Add Group Categories

    def define_groups_based_on_property_values(self, group_name=None, object_class=None, property=None, numberic_operator=None, text_operator=None, case_sensitive=None, value=None, and_or=None, group_type=None, parent_group=None, group_category=None):
        """
        Required inputs:\n
        group_name, object_class, property, numeric_operator, text_operator\n
        Not required - but useful:\n
        value\n
        Documentation on tool: # 
        """
        dictionary = g_s.dict_define_groups_based_on_property_values
        function_name = "Define Groups Based on Property Values"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.define_groups_based_on_property_values)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None
        

    def assign_groups_to_group_categories(self, group_name, type_of_ifc_group, group_category_key_or_name = None):
        """
        Required inputs:\n
        \t-group_name\n
        \t-object_class\n
        \t-type_of_ifc_group\n
        \t-Note!  group_category_key_or_name can be used instead of type_of_ifc_group:\n
        Documentation on tool: #
        """
        dictionary = g_s.dict_assign_groups_to_group_categories
        function_name = "Assign Groups to Group Categories"
        self.find_functions(self.ws)
        parameters = self.get_function_parameters(self.assign_groups_to_group_categories)
        cell = self.find_function_start(function_name)
        self.write_row(parameters,locals(),cell, dictionary)
        self.insert_row_after(cell, len(parameters))
        return None



    # TODO
    # Add Classification Systems