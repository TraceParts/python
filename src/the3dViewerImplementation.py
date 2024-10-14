import argparse

from src.utils.myUrlFormater import my_url_formater


def get_possible_options_with_default_values():
    # This is made to simplify the options' management.
    # The default values are gathered from the documentation and will be used to create more concise URLs.
    # For example : if EnableMirrorEffect is affected to 'false' in the function call, it will be ignored as it is its default value.
    return {
        "SupplierID": None,
        "PartNumber": None,
        "Product": None,
        "SelectionPath": None,

        "SetBackgroundColor": "0xFFFFFF",
        "SetRenderMode": "shaded-edged",
        "EnableMirrorEffect": "false",
        "DisplayCoordinateSystem": "false",
        "EnablePresentationMode": "false",
        "DisplayUIMenu": "true",
        "DisplayUIContextMenu": "true",
        "MergeUIMenu": "false",
        "MenuAlwaysVisible": "false",
        "DisplayUIResetButtonMenu": "true",
        "DisplayUIScreenshotButtonMenu": "true",
        "DisplayUISettingsSubMenu": "true",
        "DisplayUIPresentationModeButtonMenu": "true",
        "DisplayUIViewsSubContextMenu": "true",
        "DisplayUIRenderModesSubContextMenu": "true",
    }


# THERE IS NO API CALL HERE. This function provides a 3D viewer of the 3D model of one given configuration of a catalog
# documentation : https://developers.traceparts.com/v2/reference/3d-viewer-implementation

def the_3d_viewer_implementation(elsid: str, culture_info: str, optional_parameters: dict) -> str:
    print("There is no API call here. Inputs are just arranged and formated to get the corresponding URL.")
    optional_parameters_string = ""
    possible_options_with_default_values = get_possible_options_with_default_values()
    for parameter_key in optional_parameters.keys():
        # We go through all function options and check if they are usable (not None)
        # And if they are different from their default values
        if parameter_key in possible_options_with_default_values and optional_parameters[parameter_key] is not None:
            if optional_parameters[parameter_key] != possible_options_with_default_values[parameter_key]:
                # Values are formated to avoid special characters
                optional_parameters_string += "&{0}={1}".format(parameter_key,
                                                                my_url_formater(
                                                                    str(optional_parameters[parameter_key])))
    url = "https://www.traceparts.com/els/{0}/{1}/api/viewer/3d?{2}".format(elsid, culture_info,
                                                                            optional_parameters_string)
    return url


parser = argparse.ArgumentParser()
# Required
required = parser.add_argument_group(
    title="Required parameters. At least one of the following pairs (Pair 1 and Pair 2) are required to.")
required.add_argument("elsid",
                      help="Your EasyLink Solutions ID (ELS ID), provided in the email with your Tenant Uid and your API key")
required.add_argument("cultureInfo", help="Language of the labels.")
# Required pairs (one of those pairs must be given)
pair1 = parser.add_argument_group(
    title="Pair 1 : Both parameters (SupplierID and PartNumber) have to be used together. In this case, the couple “Product” and “SelectionPath” is not to use.")
pair1.add_argument("--SupplierID",
                   help="ClassificationCode provided by the 'availability' endpoints")
pair1.add_argument("--PartNumber",
                   help="Identifier of a product (to use in combination with SupplierID). Part number as stored in the TraceParts database.")
pair2 = parser.add_argument_group(
    title="Pair 2 : Both parameters (Product and SelectionPath) have to be used together. In this case, the couple “SupplierID” and “PartNumber” is not to use.")
pair2.add_argument("--Product",
                   help="PartFamilyCode provided by the 'availability' endpoints")
pair2.add_argument("--SelectionPath",
                   help="Sequence of parameters which defines a unique configuration for one given partFamilyCode.")
# Optional
optional = parser.add_argument_group(title="Those arguments are optional. They have default values.")
parser.add_argument("--SetBackgroundColor", default="0xFFFFFF",
                    help="(Hexadecimal ex: 0xFFFFFF) Sets a color on the background of the 3D viewer.")
parser.add_argument("--SetRenderMode", choices=["shaded-edged", "shaded", "transparent", "wireframe", "edged"], default="shaded-edged",
                    help="Rendering of the 3D model. Values: “shaded-edged”, “shaded”, “transparent”, “wireframe”, “edged”")
parser.add_argument("--EnableMirrorEffect", choices=["true", "false"], default="false",
                    help="Enable the mirror effect on the XZ plane")
parser.add_argument("--DisplayCoordinateSystem", choices=["true", "false"], default="false",
                    help="Display the coordinate system")
parser.add_argument("--EnablePresentationMode", choices=["true", "false"], default="false",
                    help="The model rotates on the Y axis until a user interaction")
parser.add_argument("--DisplayUIMenu", choices=["true", "false"], default="true",
                    help="Display the toolbars (on the bottom and on the right)")
parser.add_argument("--DisplayUIContextMenu", choices=["true", "false"], default="true",
                    help="Enable the contextual menu with Views and Render sub menus")
parser.add_argument("--MergeUIMenu", choices=["true", "false"], default="false",
                    help="Merge the contextual menu inside the main menu")
parser.add_argument("--MenuAlwaysVisible", choices=["true", "false"], default="false",
                    help="Always display the toolbar")
parser.add_argument("--DisplayUIResetButtonMenu", choices=["true", "false"], default="true",
                    help="Display the Reset button")
parser.add_argument("--DisplayUIScreenshotButtonMenu", choices=["true", "false"], default="true",
                    help="Display the Screenshot button")
parser.add_argument("--DisplayUISettingsSubMenu", choices=["true", "false"], default="true",
                    help="Display the Settings menu")
parser.add_argument("--DisplayUIPresentationModeButtonMenu", choices=["true", "false"], default="true",
                    help="Display the Presentation button")
parser.add_argument("--DisplayUIViewsSubContextMenu", choices=["true", "false"], default="true",
                    help="Display the Views sub menu (for the contextual menu)")
parser.add_argument("--DisplayUIRenderModesSubContextMenu", choices=["true", "false"], default="true",
                    help="Display the Render sub menu (for the contextual menu)")

if __name__ == '__main__':
    args = parser.parse_args()
    print(the_3d_viewer_implementation(args.elsid, args.cultureInfo, args.__dict__))
