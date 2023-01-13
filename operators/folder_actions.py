import bpy
import os

def return_image_folder():
    from ..addon_prefs import get_addon_preferences
    path=os.path.dirname(bpy.data.filepath)
    return os.path.join(path, get_addon_preferences().folder_name)

class IMGMNG_OT_create_image_folder(bpy.types.Operator):
    bl_idname = "imgmng.create_image_folder"
    bl_label = "Create Folder"
    bl_description = "Create external image folder."
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        folderpath=return_image_folder()
        if os.path.isdir(folderpath):
            self.report({'WARNING'}, "Folder already exists")
            return {'FINISHED'}
        os.mkdir(folderpath)
        self.report({'INFO'}, f"Folder created : {folderpath}")
        return {'FINISHED'}


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_OT_create_image_folder)

def unregister():
    bpy.utils.unregister_class(IMGMNG_OT_create_image_folder)