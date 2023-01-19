import bpy
import shutil
import os

from . import folder_actions_operator as pck
from . import reload_available_images_operator as rld

def pack_image(image):
    image.pack()

def unpack_image_at_location(image, location):
    image.unpack()

    filename=os.path.basename(image.filepath)
    src=bpy.path.abspath(image.filepath)
    dst=os.path.join(location, filename)

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)

    os.remove(src)
    os.rmdir(os.path.dirname(src))

    image.filepath=dst
    return dst

class IMGMNG_OT_pack_operator(bpy.types.Operator):
    bl_idname = "imgmng.pack_image"
    bl_label = "Pack Image"
    bl_description = "Pack image."
    bl_options = {'INTERNAL'}

    image: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        pack_image(bpy.data.images[self.image])
        self.report({'INFO'}, f"Image Packed : {self.image}")
        return {'FINISHED'}

class IMGMNG_OT_unpack_operator(bpy.types.Operator):
    bl_idname = "imgmng.unpack_image"
    bl_label = "Unpack Image"
    bl_description = "Unpack image in resources folder."
    bl_options = {'INTERNAL'}

    image: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        filepath=unpack_image_at_location(bpy.data.images[self.image], pck.return_image_folder())
        self.report({'INFO'}, f"Image Unpacked : {filepath}")
        rld.reload_available_images()
        return {'FINISHED'}


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_OT_pack_operator)
    bpy.utils.register_class(IMGMNG_OT_unpack_operator)

def unregister():
    bpy.utils.unregister_class(IMGMNG_OT_pack_operator)
    bpy.utils.unregister_class(IMGMNG_OT_unpack_operator)
