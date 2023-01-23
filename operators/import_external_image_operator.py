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

    @classmethod
    def poll(cls, context):
        props = context.scene.imgmng_properties
        if props.active_local_image_index in range(0,len(props.available_images)):
            return True

    def execute(self, context):
        props=context.scene.imgmng_properties
        available_images=props.available_images
        img=available_images[props.active_available_image_index]

        if not os.path.isfile(img.filepath):
            self.report({'WARNING'}, f"Image does not exist")
            rld.reload_available_images()
            return {'CANCELLED'}

        import_image(img.filepath)
        self.report({'INFO'}, f"Image imported : {img.name}")
        rld.reload_available_images()
        return {'FINISHED'}


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_OT_import_image)

def unregister():
    bpy.utils.unregister_class(IMGMNG_OT_import_image)
