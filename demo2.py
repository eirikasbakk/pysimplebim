# Import library
from pysimplebim import template

# Set paths to excel-files that we are using
original_path = "assets/base.xlsx"
edited_path = "assets/edited2.xlsx"

# Use Resources sheet
wb = template.Resources(original_path)

# List all functions in the Resources sheet
wb.list_functions()

#Print all parameters in the given function
print(wb.get_function_parameters(wb.add_identity_for_ifc_propertyset))
