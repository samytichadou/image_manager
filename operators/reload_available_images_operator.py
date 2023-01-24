import bpy
import os

from .folder_actions_operator import return_image_folder

img_extensions={
    ".bmp",
    ".sgi",
    ".rgb",
    ".bw",
    ".png",
    ".jpg",
    ".jpeg",
    ".jp2",
    ".jp2",
    ".j2c",
    ".tga",
    ".cin",
    ".dpx",
    ".exr",
    ".hdr",
    ".tif",
    ".tiff",
    ".webp",
}

def reload_available_images():
    img_coll=bpy.context.scene.imgmng_properties.available_images
    folderpath=return_image_folder()
    if not os.path.isdir(folderpath):
        #print("Image Manager --- No valid image folder")
        return False
    img_coll.clear()
    for f in os.listdir(folderpath):
        if os.path.splitext(f)[1] in img_extensions:
            new=img_coll.add()
            new.name=f
            new.filepath=os.path.join(folderpath, f)

            for img in bpy.data.images:
                if bpy.path.abspath(img.filepath)==new.filepath:
                    new.imported=True
                    break
    return True


class IMGMNG_OT_reload_available_images(bpy.types.Operator):
    bl_idname = "imgmng.reload_available_images"
    bl_label = "Reload Available Images"
    bl_description = "Reload available images from the external folder"
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        folderpath=return_image_folder()
        if not os.path.isdir(folderpath):
            self.report({'WARNING'}, "No image folder")
            return {'FINISHED'}
        reload_available_images()
        self.report({'INFO'}, f"Images reloaded")
        return {'FINISHED'}

### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_OT_reload_available_images)

def unregister():
    bpy.utils.unregister_class(IMGMNG_OT_reload_available_images)
