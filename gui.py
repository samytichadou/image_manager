import bpy
import os

from .operators.folder_actions_operator import return_image_folder

from bpy.types import bpy_prop_collection   

def search_image_uses(ID):
    def users(col):
        ret =  tuple(repr(o) for o in col if o.user_of_id(ID))
        return ret if ret else None
    raw=filter(None, (
        users(getattr(bpy.data, p)) 
        for p in  dir(bpy.data) 
        if isinstance(
                getattr(bpy.data, p, None), 
                bpy_prop_collection
                )                
        )
        )
    uses_list=[]
    for f in raw:
        splits=str(f).split('"')
        for s in splits:
            if "bpy.data." in s:
                uses_list.append(s.split("bpy.data.")[1])
    return uses_list

class IMGMNG_PT_image_panel(bpy.types.Panel):
    bl_label = "Image Manager"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        layout = self.layout
        row=layout.row(align=True)
        row.operator('image.open')
        row.separator()
        row.operator('imgmng.change_all_images_path_type', text="All Relative").relative=True
        row.operator('imgmng.change_all_images_path_type', text="All Absolute").relative=False

class IMGMNG_PT_local_images_sub(bpy.types.Panel):
    bl_label = "Local Images"
    bl_parent_id = "IMGMNG_PT_image_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    @classmethod
    def poll(cls, context):
        return bpy.data.images

    def draw(self, context):
        props = context.scene.imgmng_properties
        layout = self.layout

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
        if props.active_local_image_index in range(0,len(bpy.data.images)):
            active = bpy.data.images[props.active_local_image_index]
            col.prop(active, "filepath", text="")

class IMGMNG_PT_image_uses_sub(bpy.types.Panel):
    bl_label = ""
    bl_parent_id = "IMGMNG_PT_local_images_sub"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        props=context.scene.imgmng_properties
        if props.active_local_image_index in range(0,len(bpy.data.images)):
            img=bpy.data.images[props.active_local_image_index]
            if img.source not in {'VIEWER','GENERATED'} \
            and img.filepath:
                return True

    def draw_header(self, context):
        img=bpy.data.images[context.scene.imgmng_properties.active_local_image_index]
        uses=search_image_uses(img)

        layout = self.layout
        layout.label(text=f"Usage ({len(uses)})")
        #print(f"{img.name} - {users}")

    def draw(self, context):
        active = bpy.data.images[context.scene.imgmng_properties.active_local_image_index]
        layout = self.layout
        uses=search_image_uses(active)
        if uses:
            col=layout.column(align=True)
            for item in uses:
                col.label(text=str(item))
        else:
            layout.label(text="Image not used")

class IMGMNG_PT_available_images_sub(bpy.types.Panel):
    bl_label = "Resources Folder"
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

            layout.template_list(
                "IMGMNG_UL_external_images_uilist",
                "",
                props,
                "available_images",
                props,
                "active_available_image_index",
                rows=3
                )
            #if props.active_available_image_index in range(0,len(props.available_images)):


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_PT_image_panel)
    bpy.utils.register_class(IMGMNG_PT_local_images_sub)
    bpy.utils.register_class(IMGMNG_PT_image_uses_sub)
    bpy.utils.register_class(IMGMNG_PT_available_images_sub)

def unregister():
    bpy.utils.unregister_class(IMGMNG_PT_image_panel)
    bpy.utils.unregister_class(IMGMNG_PT_local_images_sub)
    bpy.utils.unregister_class(IMGMNG_PT_image_uses_sub)
    bpy.utils.unregister_class(IMGMNG_PT_available_images_sub)
