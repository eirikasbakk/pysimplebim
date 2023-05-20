# Import library
from pysimplebim import template 

# Set paths to excel-files that we are using
original_path = "assets/base.xlsx"
edited_path = "assets/edited.xlsx"

# load a file and specify wich woorksheet you are using
wb = template.ModelView(original_path)

# Use a couple of functions from the worksheet
for i in range(5):

    wb.include_exclude_objects_based_on_object_class_or_group(f"Alle barner + {str(i)}", "Yes")
    wb.include_exclude_property("Yes", "No")

# Save the file
wb.save_workbook(edited_path)

# load the file again to work in another sheet
wb = template.Substitution(edited_path)

# Use a function
wb.substitution_lists("alle", [str(i) for i in range(10)])

# Save the file
wb.save_workbook(edited_path)

wb = template.Validation(edited_path)
wb.required_objects(object_or_group="Første", requirement= "Must Have Objects_")

wb.save_workbook(edited_path)

