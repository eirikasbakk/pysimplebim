from .config import Config

class Dropdowns():
    """ Class containing dropdowns in the templates and valid worksheets"""
    sheets = ["Enrichment", "Groups", "Model", "ModelView", "Resources", "Settings", "Substitution"]
    property_types = ["Date", "Number", "Text", "Yes/No", "Whole Number"]
    trim_types = ["Prefix", "Postfix","Anywhere","Regex","Regex Inverse"]
    yes_no = ["Yes", "No"]
    single_list = ["Single", "List", "None"]
    text_operators = ["Equals", "Contains", "StartsWith", "EndsWith", "Like", "Match", "NotEquals", "NotContains", "NotStartsWith", "NotEndsWith", "NotLike", "NotMatch"]
    numeric_operators = ["Equals", "NotEquals", "GreaterThan", "GreaterThanOrEqualTo", "LessThan", "LessThanOrEqualTo"]
    percent = [x for x in range(0,100)]
    replace_type = ["Whole Text", "Within Text"]
    rules_for_text_properties = ["Must be one of the Values", "Must contain one of the Values",  "Must start with one of the Values", "Must end with one of the Values",
    "Must be like one of the Values (with wildcards)", "Must match one of the Values (regular expression)", "Must have unique values", "Must not be any of the Values",     
    "Must not contain any of the Values", "Must not start with any of the Values", "Must not end with any of the Values", "Must not be like any of the Values (with wildcards)", 
    "Must not match any of the Values (regular expression)"]
    numeric_operators = ["Equals", "NotEquals", "GreaterThan", "GreaterThanOrEqualTo", "LessThan", "LessThanOrEqualTo"]
    and_or = ["And", "Or"]
    ifc_property_types = ["", None] #TODO in resources add identity for ifc propertyset
    requirement = ["Must Have Objects", "Must Not Have Objects", "No Requirement"]
    group_type = ["Manual", "Rule Based", "Container", "Template Only"]
    ifc_group_type = ["IfcGroup", "IfcSystem", "IfcZone", "IfcAsset"]


class Resources_s:

    #TODO
    dict_add_identity_source = None

    #TODO
    dict_add_identity = None

    dict_add_identity_for_ifc_propertyset = {
        0: {
            "name": "Identity Source Key",
            "required": False,
            "predefined": False,
            "source": None,
            "list_allowed": False
        },
        1: {
            "name": "Identity Key",
            "required": True,
            "predefined": False,
            "source": None,
            "list_allowed": False
        },
        2: {
            "name": "Name",
            "required": True, 
            "predefined": False,
            "source": None,
            "list_allowed": False,
        },
        3: {
            "name": "Description",
            "required": False, 
            "predefined": False,
            "source": None,
            "list_allowed": False,
        },
        4: {
            "name": "Reference",
            "required": False, 
            "predefined": False,
            "source": None,
            "list_allowed": False,
        },
        5: {
            "name": "PropertySet Name",
            "required": True, 
            "predefined": False,
            "source": None,
            "list_allowed": False,
        },
        6: {
            "name": "Property Name",
            "required": True, 
            "predefined": False, 
            "source": None,
            "list_allowed": False,
        },
        7: {
            "name": "Property Type",
            "required": False, 
            "predefined": True,
            "source": Dropdowns.ifc_property_types,
            "list_allowed": False,
        },
        "function_name" : "Add Identity (for IFC PropertySet)" 
        
        }

    #TODO
    dict_add_identity_for_ifc_element_quantity = None

    #TODO
    dict_add_identity_metadata = None    

class Model_s:

    """ Containing all the settings for the fields in the different functions in the Modelsheet"""

    dict_add_identity_to_object = {
        0: {
            "name": "Object [+]",
            "required": True,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "Identity to Add [+]",
            "required": True,
            "predefined": False,
            "list_allowed": True
        },
        2: {
            "name": "Make Default",
            "required": False,
            "predefined": True,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        "function_name" : "Add Identity to Object" 
    }

    dict_add_property_to_object_class_or_group = {
        0: {
            "name": "Object or Group",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True,
        },
        1: {
            "name": "Property",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True,
        },
        2: {
            "name": "Property Type",
            "required": True, 
            "predefined": True,
            "source": Dropdowns.property_types,
            "list_allowed": False,
        },
        3: {
            "name": "Single/List",
            "required": False, 
            "predefined": True,
            "source": Dropdowns.single_list,
            "list_allowed": False
        },
        4: {
            "name": "Unit Symbol",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        "function_name" : "Add Property to Object Class or Group" 
    }

    dict_add_identity_to_property = {
        0: {
            "name": "Object [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True,
        },
        1: {
            "name": "Existing Property",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False,
        },
        2: {
            "name": "Identity to Add",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False,
        },
        3: {
            "name": "Make Default",
            "required": False, 
            "predefined": True,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        "function_name" : "Add Identity to Property" 
    }

    dict_swap_property_values = {
        0: {
            "name": "Object [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "Property 1",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        2: {
            "name": "Property 2",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        "function_name" : "Swap Property Values" 
    }


    dict_trim_text_property_values_before_copy = {
        0: {
            "name": "Object or Group [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "Trim Property [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        2: {
            "name": "Trim Type",
            "required": True, 
            "type": str,
            "predefined": True,
            "source": Dropdowns.trim_types,
            "list_allowed": False
        },
        3: {
            "name": "Case Sensitive",
            "required": False, 
            "predefined": False,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        4: {
            "name": "Text to Trim",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        "function_name" : "Trim Text Property Values (before copy)" 
    }

    dict_find_and_replace_text_property_values_before_copy = {
        0: {
            "name": "Object or Group [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "Find Property [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        2: {
            "name": "Text Operator",
            "required": True, 
            "type": str,
            "predefined": True,
            "source": Dropdowns.text_operators,
            "list_allowed": False
        },
        3: {
            "name": "Case Sensitive",
            "required": False, 
            "predefined": False,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        4: {
            "name": "Find Value [+]",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        5: {
            "name": "Replace Value",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        6: {
            "name": "Replace Type",
            "required": False, 
            "type": str,
            "predefined": False,
            "source": Dropdowns.replace_type,
            "list_allowed": False
        },
        "function_name" : "Find and Replace Text Property Values (before copy)" 
    }

    dict_set_property_values_based_on_text_property_values_before_copy = {
        0: {
            "name": "Object or Group [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "Find Property [+]",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        2: {
            "name": "Text Operator",
            "required": False, 
            "type": str,
            "predefined": True,
            "source": Dropdowns.text_operators,
            "list_allowed": False
        },
        3: {
            "name": "Case Sensitive",
            "required": False, 
            "predefined": True,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        4: {
            "name": "Find Value [+]",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        5: {
            "name": "Set Property",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        6: {
            "name": "Set Value",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        "function_name" : "Set Property Values Based on Text Property Value (before copy)" 
    }
    
    dict_copy_property_values = {
        0: {
            "name": "Object or Group [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "From Property",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        2: {
            "name": "To Property",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        3: {
            "name": "Copy Empty Values",
            "required": False, 
            "predefined": True,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        4: {
            "name": "Overwrite Non Empty Values",
            "required": False, 
            "predefined": True,
            "source": Dropdowns.yes_no,
            "list_allowed": True
        },
        5: {
            "name": "Regular Expression",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        "function_name" : "Copy Property Values" 
    }

    dict_trim_text_property_values_after_copy = {
        0: {
            "name": "Object or Group [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "Trim Property [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        2: {
            "name": "Trim Type",
            "required": True, 
            "type": str,
            "predefined": True,
            "source": Dropdowns.trim_types,
            "list_allowed": False
        },
        3: {
            "name": "Case Sensitive",
            "required": False, 
            "predefined": False,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        4: {
            "name": "Text to Trim",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        "function_name" : "Trim Text Property Values (after copy)" 
    }

    #TODO
    dict_find_and_replace_text_property_values_after_copy = {
        0: {
            "name": "Object or Group [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "Find Property [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        2: {
            "name": "Text Operator",
            "required": True, 
            "type": str,
            "predefined": True,
            "source": Dropdowns.text_operators,
            "list_allowed": False
        },
        3: {
            "name": "Case Sensitive",
            "required": False, 
            "predefined": False,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        4: {
            "name": "Find Value [+]",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        5: {
            "name": "Replace Value",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        6: {
            "name": "Replace Type",
            "required": False, 
            "type": str,
            "predefined": False,
            "source": Dropdowns.replace_type,
            "list_allowed": False
        },
        "function_name" : "Find and Replace Text Property Values (after copy)" 
    }

    dict_set_property_values_based_on_text_property_values_after_copy = {
        0: {
            "name": "Object or Group [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "Find Property [+]",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        2: {
            "name": "Text Operator",
            "required": False, 
            "type": str,
            "predefined": True,
            "source": Dropdowns.text_operators,
            "list_allowed": False
        },
        3: {
            "name": "Case Sensitive",
            "required": False, 
            "predefined": False,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        4: {
            "name": "Find Value [+]",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": True
        },
        5: {
            "name": "Set Property",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        6: {
            "name": "Set Value",
            "required": False, 
            "type": str,
            "predefined": False,
            "list_allowed": False
        },
        "function_name" : "Set Property Values Based on Text Property Value (after copy)" 
    }
    

class ModelView_s:

    dict_include_exclude_objects_based_on_object_class_or_group = {
        0: {
            "name": "Object or Group [+]",
            "required": True,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "Include",
            "required": False,
            "predefined": True,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        "function_name" : "Include/Exclude Objects Based on Object Class or Group"
    }

    dict_include_exclude_property = {
    0: {
        "name": "Object [+]",
        "required": True, 
        "type": str,
        "predefined": False,
        "list_allowed": True,
    },
    1: {
        "name": "Property [+]",
        "required": True, 
        "type": str,
        "predefined": False,
        "list_allowed": True,
    },
    2: {
        "name": "Include",
        "required": False, 
        "predefined": True,
        "source": Dropdowns.yes_no,
        "list_allowed": False,
    },
        "function_name" : "Include/Exclude Property"
    }

    dict_set_object_color_and_transparency_based_on_object_class_or_group = {
    0: {
        "name": "Object or Group [+]",
        "required": True, 
        "type": str,
        "predefined": False,
        "list_allowed": True
    },
    1: {
        "name": "Color",
        "required": False, 
        "type": str,
        "predefined": True,
        "source": Config.colors,
        "list_allowed": False
    },
    2: {
        "name": "Transparency %",
        "required": False, 
        "type": "int",
        "predefined": False,
        "list_allowed": False
    },
    "function_name" : "Set Object Color and Transparency Based on Object Class or Group"
    }


class Validation_s():

    dict_required_objects = {
        0: {
            "name": "Object or Group [+]",
            "required": True,
            "predefined": False,
            "source": None,
            "list_allowed": True
        },
        1: {
            "name": "Requirement",
            "required": False,
            "predefined": True,
            "source": Dropdowns.requirement,
            "list_allowed": False
        },
        "function_name" : "Required Objects" 
    }

    dict_required_properties = {
        0: {
            "name": "Object or Group [+]",
            "required": True,
            "predefined": False,
            "source": None,
            "list_allowed": True
        },
        1: {
            "name": "Property",
            "required": True,
            "predefined": False,
            "source": None,
            "list_allowed": True
        },
        2: {
            "name": "Yes/No",
            "required": False,
            "predefined": True,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        "function_name" : "Required Properties" 
    }

    dict_rules_for_text_property_values = {
        0: {
            "name": "Object or Group [+]",
            "required": True,
            "predefined": False,
            "source": None,
            "list_allowed": True
        },
        1: {
            "name": "Text Property [+]",
            "required": True,
            "predefined": False,
            "source": None,
            "list_allowed": True
        },
        2: {
            "name": "Rule for Text Property",
            "required": False,
            "predefined": True,
            "source": Dropdowns.rules_for_text_properties,
            "list_allowed": False
        },
        3: {
            "name": "Case Sensitive",
            "required": False,
            "predefined": True,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        4: {
            "name": "Allow Empty",
            "required": False,
            "predefined": True,
            "source": Dropdowns.yes_no,
            "list_allowed": False
        },
        5: {
            "name": "Separator",
            "required": False,
            "predefined": False,
            "source": None, 
            "list_allowed": False
        },
        6: {
            "name": "Value [+]",
            "required": True,
            "predefined": False,
            "source": None, 
            "list_allowed": True
        },
        "function_name" : "Rules for Text Property Values" 
    }


class Enrichment_s():
    #TODO
    pass 

class Subtitution_s():

    dict_substitution_list = {
        0: {
            "name": "List Name",
            "required": True,
            "predefined": False,
            "list_allowed": False
        },
        1: {
            "name": "List Values",
            "required": True,
            "predefined": False,
            "list_allowed": True
        },
        "function_name" : "Substitution Lists"
    }


class Groups_s:

    dict_add_group_categories = {
        0: {
            "name": "Group Category Key",
            "required": True,
            "predefined": False,
            "list_allowed": False
        },
        1: {
            "name": "Group Category Name",
            "required": True,
            "predefined": False,
            "list_allowed": False
        },
        2: {
            "name": "Parent Group Category",
            "required": False,
            "predefined": False,
            "list_allowed": False
        },
        "function_name" : "Add Group Categories" 
    }

    dict_define_groups_based_on_property_values= {
        0: {
            "name": "Group Name",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": False,
        },
        1: {
            "name": "Object Class [+]",
            "required": True, 
            "type": str,
            "predefined": False,
            "list_allowed": True,
        },
        2: {
            "name": "Property [+]",
            "required": True, 
            "predefined": True,
            "list_allowed": True, 
        },
        3: {
            "name": "Numeric Operator …or…", # TODO One, this or the next, must be present
            "required": False, 
            "predefined": True,
            "source": Dropdowns.numeric_operators,
            "list_allowed": False
        },
        4: {
            "name": "Text Operator ", # TODO 
            "required": False, 
            "predefined": True,
            "source": Dropdowns.text_operators,
            "list_allowed": False
        },
        5: {
            "name": "Value [+]", 
            "required": False, 
            "predefined": False,
            "list_allowed": True
        },
        6: {
            "name": "And/Or", 
            "required": False, 
            "predefined": True,
            "source": Dropdowns.and_or,
            "list_allowed": False
        },
        7: {
            "name": "Group Type", 
            "required": False, 
            "predefined": True,
            "source": Dropdowns.group_type,
            "list_allowed": False
        },
        8: {
            "name": "Parent Group", 
            "required": False, 
            "predefined": False,
            "list_allowed": False
        },
        9: {
            "name": "Group Category", 
            "required": False, 
            "predefined": False,
            "list_allowed": False
        },
        "function_name" : "Define Groups Based on Property Values" 
    }

    dict_assign_groups_to_group_categories= {
        0: {
            "name": "Group Name [+]",
            "required": True,
            "predefined": False,
            "list_allowed": True
        },
        1: {
            "name": "Type of IFC Group …or...",
            "required": False,
            "predefined": True,
             "source": Dropdowns.ifc_group_type,
            "list_allowed": False
        },
        2: {
            "name": " Group Category Key or Name",
            "required": False,
            "predefined": False,
            "list_allowed": False
        },
        "function_name" : "Assign Groups to Group Categories" 
    }








