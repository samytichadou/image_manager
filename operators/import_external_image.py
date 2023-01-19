import bpy

def import_image(filepath):
    img=bpy.data.images.load(filepath)
    return img

class IMGMNG_OT_import_image(bpy.types.Operator):
    bl_idname = "imgmng.import_image"
    bl_label = "Import Image"
    bl_description = "Import Image in Blender"
    bl_options = {'INTERNAL'}

    image: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        props=context.scene
        img=bpy.data.images[self.image]
        dst=fld.return_image_folder()

        if os.path.dirname(bpy.path.abspath(img.filepath))==dst:
            self.report({'WARNING'}, f"Image Already in Folder : {self.image}")
            return {'CANCELLED'}

        filepath=copy_relink_image_at_location(img, dst)
        self.report({'INFO'}, f"Image Copied : {filepath}")
        rld.reload_available_images()
        return {'FINISHED'}


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_OT_copy_image)

def unregister():
    bpy.utils.unregister_class(IMGMNG_OT_copy_image)
