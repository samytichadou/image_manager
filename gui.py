import bpy

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

class IMGMNG_PT_internal_images_sub(bpy.types.Panel):
    bl_label = "Internal Images"
    bl_parent_id = "IMGMNG_PT_image_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        props = context.scene.imgmng_properties
        layout = self.layout

        if props.active_image_index in range(0,len(bpy.data.images)):
            col=layout.column(align=True)
            col.template_list(
                "IMGMNG_UL_internal_images_uilist",
                "",
                bpy.data,
                "images",
                props,
                "active_image_index",
                rows=3
                )
            # selected image path
            active = bpy.data.images[props.active_image_index]
            col.prop(active, "filepath", text="")


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_PT_image_panel)
    bpy.utils.register_class(IMGMNG_PT_internal_images_sub)

def unregister():
    bpy.utils.unregister_class(IMGMNG_PT_image_panel)
    bpy.utils.unregister_class(IMGMNG_PT_internal_images_sub)