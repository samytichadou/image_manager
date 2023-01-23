import bpy

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
        reload_image(bpy.data.images[self.image])
        self.report({'INFO'}, f"Image Reloaded : {self.image}")
        return {'FINISHED'}

class IMGMNG_OT_remove_image(bpy.types.Operator):
    bl_idname = "imgmng.remove_image"
    bl_label = "Remove Image"
    bl_options = {'INTERNAL'}

    image: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        remove_image(bpy.data.images[self.image])
        self.report({'INFO'}, f"Image Removed : {self.image}")
        return {'FINISHED'}


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_OT_reload_image)
    bpy.utils.register_class(IMGMNG_OT_remove_image)

def unregister():
    bpy.utils.unregister_class(IMGMNG_OT_reload_image)
    bpy.utils.unregister_class(IMGMNG_OT_remove_image)