import bpy
import os

from . import reload_available_images_operator as rld
from . import folder_actions_operator as fld

def reload_image(image):
    image.reload()

def remove_image(image):
    bpy.data.images.remove(image)

class IMGMNG_OT_reload_image(bpy.types.Operator):
    bl_idname = "imgmng.reload_image"
    bl_label = "Reload Image"
    bl_options = {'INTERNAL'}

    image: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        img=bpy.data.images[self.image]
        reload_image(img)
        img.modification_time=str(os.path.getmtime(bpy.path.abspath(img.filepath)))
        self.report({'INFO'}, f"Image Reloaded : {self.image}")
        return {'FINISHED'}

class IMGMNG_OT_remove_image(bpy.types.Operator):
    bl_idname = "imgmng.remove_image"
    bl_label = "Remove Image"
    bl_options = {'INTERNAL','UNDO'}

    image: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        remove_image(bpy.data.images[self.image])
        rld.reload_available_images()
        self.report({'INFO'}, f"Image Removed : {self.image}")
        return {'FINISHED'}

class IMGMNG_OT_reveal_image(bpy.types.Operator):
    bl_idname = "imgmng.reveal_image"
    bl_label = "Reveal Image"
    bl_options = {'INTERNAL'}

    image: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        img=bpy.data.images[self.image]
        fld.open_in_explorer(bpy.path.abspath(img.filepath))
        self.report({'INFO'}, f"Image Revealed : {self.image}")
        return {'FINISHED'}

class IMGMNG_OT_change_path_type(bpy.types.Operator):
    bl_idname = "imgmng.change_path_type"
    bl_label = "Change Path Type"
    bl_description = "Toggle between relative and absolute path"
    bl_options = {'INTERNAL','UNDO'}

    image: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        img=bpy.data.images[self.image]
        if img.filepath.startswith("//"):
            img.filepath=bpy.path.abspath(img.filepath)
        else:
            img.filepath=bpy.path.relpath(img.filepath)
        self.report({'INFO'}, f"Image Path Changed : {img.filepath}")
        return {'FINISHED'}



### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_OT_reload_image)
    bpy.utils.register_class(IMGMNG_OT_remove_image)
    bpy.utils.register_class(IMGMNG_OT_reveal_image)
    bpy.utils.register_class(IMGMNG_OT_change_path_type)

def unregister():
    bpy.utils.unregister_class(IMGMNG_OT_reload_image)
    bpy.utils.unregister_class(IMGMNG_OT_remove_image)
    bpy.utils.unregister_class(IMGMNG_OT_reveal_image)
    bpy.utils.unregister_class(IMGMNG_OT_change_path_type)
