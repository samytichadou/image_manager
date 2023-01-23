import bpy
import os

from . import reload_available_images_operator as rld

def import_image(filepath):
    return bpy.data.images.load(filepath)

class IMGMNG_OT_import_image(bpy.types.Operator):
    bl_idname = "imgmng.import_image"
    bl_label = "Import Image"
    bl_description = "Import Image in Blender"
    bl_options = {'INTERNAL'}

    filepath: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        if not os.path.isfile(self.filepath):
            self.report({'WARNING'}, f"Image does not exist")
            rld.reload_available_images()
            return {'CANCELLED'}

        img=import_image(self.filepath)
        img.modification_time=str(os.path.getmtime(self.filepath))
        self.report({'INFO'}, f"Image imported : {self.filepath}")
        rld.reload_available_images()
        return {'FINISHED'}


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_OT_import_image)

def unregister():
    bpy.utils.unregister_class(IMGMNG_OT_import_image)
