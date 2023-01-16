import bpy
import os

from .operators.folder_actions import return_image_folder

class IMGMNG_PT_image_panel(bpy.types.Panel):
    bl_label = "Image Manager"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    @classmethod
    def poll(cls, context):
        if bpy.data.images:
            return True

    def draw(self, context):
        layout = self.layout

class IMGMNG_PT_local_images_sub(bpy.types.Panel):
    bl_label = "Local Images"
    bl_parent_id = "IMGMNG_PT_image_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        props = context.scene.imgmng_properties
        layout = self.layout

        if props.active_local_image_index in range(0,len(bpy.data.images)):
            col=layout.column(align=True)
            col.template_list(
                "IMGMNG_UL_internal_images_uilist",
                "",
                bpy.data,
                "images",
                props,
                "active_local_image_index",
                rows=3
                )
            # selected image path
            active = bpy.data.images[props.active_local_image_index]
            col.prop(active, "filepath", text="")

class IMGMNG_PT_available_images_sub(bpy.types.Panel):
    bl_label = "Available Images"
    bl_parent_id = "IMGMNG_PT_image_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        props = context.scene.imgmng_properties
        folderpath=return_image_folder()
        layout = self.layout
        
        row=layout.row(align=True)
        row.label(text=folderpath)

        if not os.path.isdir(folderpath):
            row.operator('imgmng.create_image_folder', text="", icon="NEWFOLDER")
        else:
            row.operator('imgmng.reload_available_images', text="", icon="FILE_REFRESH")
            row.operator('imgmng.open_filepath', text="", icon="FILE_FOLDER").filepath=folderpath

            if props.active_available_image_index in range(0,len(props.available_images)):
                layout.template_list(
                    "IMGMNG_UL_external_images_uilist",
                    "",
                    props,
                    "available_images",
                    props,
                    "active_available_image_index",
                    rows=3
                    )


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_PT_image_panel)
    bpy.utils.register_class(IMGMNG_PT_local_images_sub)
    bpy.utils.register_class(IMGMNG_PT_available_images_sub)

def unregister():
    bpy.utils.unregister_class(IMGMNG_PT_image_panel)
    bpy.utils.unregister_class(IMGMNG_PT_local_images_sub)
    bpy.utils.unregister_class(IMGMNG_PT_available_images_sub)    