import bpy

# Internal Images
class IMGMNG_UL_internal_images_uilist(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, flt_flag) :
        row = layout.row(align = True)

        # packed file
        if item.packed_file:
            row.label(text="", icon="PACKAGE")
            row.prop(item, "name", text="", emboss=False)
        # internal files
        elif item.source in {'VIEWER','GENERATED'} \
        or not item.filepath:
            row.label(text="", icon="FILE_BACKUP")
            row.prop(item, "name", text="", emboss=False)
        # external files
        else:
            row.label(text="", icon="DISK_DRIVE")
            row.prop(item, "name", text="", emboss=False)     

# External Images
class IMGMNG_UL_external_images_uilist(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, flt_flag) :
        row = layout.row(align = True)

        # packed file
        if item.packed_file:
            row.label(text="", icon="PACKAGE")
            row.prop(item, "name", text="", emboss=False)
        # internal files
        elif item.source in {'VIEWER','GENERATED'} \
        or not item.filepath:
            row.label(text="", icon="FILE_BACKUP")
            row.prop(item, "name", text="", emboss=False)
        # external files
        else:
            row.label(text="", icon="DISK_DRIVE")
            row.prop(item, "name", text="", emboss=False)   

### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_UL_internal_images_uilist)
    bpy.utils.register_class(IMGMNG_UL_external_images_uilist)

def unregister():
    bpy.utils.unregister_class(IMGMNG_UL_internal_images_uilist)
    bpy.utils.unregister_class(IMGMNG_UL_external_images_uilist)