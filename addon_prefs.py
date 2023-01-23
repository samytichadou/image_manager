import bpy
import os

addon_name = os.path.basename(os.path.dirname(__file__))

class IMGMNG_PT_addon_prefs(bpy.types.AddonPreferences):
    bl_idname = addon_name

    folder_name : bpy.props.StringProperty(
        name = "Folder Name",
        description = "Name of the Images Folder.",
        default="resources",
        )

    timer_frequency : bpy.props.FloatProperty(
        name="Fréquence (s)", 
        precision=2, 
        min=0.01, 
        max=3600.00, 
        default=10.00, 
        description="Fréquence de rafraichissement du timer",
        )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "folder_name")
        layout.prop(self, "timer_frequency", text="Timer")

        
# get addon preferences
def get_addon_preferences():
    addon = bpy.context.preferences.addons.get(addon_name)
    return getattr(addon, "preferences", None)


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_PT_addon_prefs)

def unregister():
    bpy.utils.unregister_class(IMGMNG_PT_addon_prefs)