import bpy
import os
import shutil

from . import folder_actions_operator as fld
from . import reload_available_images_operator as rld

def copy_relink_image_at_location(image, location):
    filename=os.path.basename(image.filepath)
    src=bpy.path.abspath(image.filepath)
    dst=os.path.join(location, filename)

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)

    image.filepath=dst
    return dst

class IMGMNG_OT_copy_image(bpy.types.Operator):
    bl_idname = "imgmng.copy_image"
    bl_label = "Copy Image"
    bl_description = "Copy image in resources folder."
    bl_options = {'INTERNAL','UNDO'}

    image: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        img=bpy.data.images[self.image]
        dst=fld.return_image_folder()

        if os.path.dirname(bpy.path.abspath(img.filepath))==dst:
            self.report({'WARNING'}, f"Image Already in Folder : {self.image}")
            return {'CANCELLED'}

        filepath=copy_relink_image_at_location(img, dst)
        img.modification_time=str(os.path.getmtime(filepath))
        self.report({'INFO'}, f"Image Copied : {filepath}")
        rld.reload_available_images()
        return {'FINISHED'}


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_OT_copy_image)

def unregister():
    bpy.utils.unregister_class(IMGMNG_OT_copy_image)
