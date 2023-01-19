import bpy

def return_image_users(image):
    if image.use_fake_user:
        return image.users-1
    else:
        return image.users


# Internal Images
class IMGMNG_UL_internal_images_uilist(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, flt_flag) :
        row = layout.row(align = True)

        # LOGO
        # internal files
        if item.source in {'VIEWER','GENERATED'} \
        or not item.filepath:
            row.label(text="", icon="FILE_BACKUP")
        # external files
        else:
            row.label(text="", icon="DISK_DRIVE")

        # COMMON
        row.prop(item, "name", text="", emboss=False)
        # row.label(text=str(return_image_users(item)))
        # row.prop(item, "users", text="", emboss=False)
        row.prop(item, "use_fake_user", text="")

        # PACK UNPACK
        if item.packed_file:
            row.operator('imgmng.unpack_image', text="", icon="PACKAGE").image=item.name
        else:
            row.operator('imgmng.pack_image', text="", icon="UGLYPACKAGE").image=item.name


# External Images
class IMGMNG_UL_external_images_uilist(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, flt_flag) :
        row = layout.row(align = True)

        row.label(text=item.name)


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_UL_internal_images_uilist)
    bpy.utils.register_class(IMGMNG_UL_external_images_uilist)

def unregister():
    bpy.utils.unregister_class(IMGMNG_UL_internal_images_uilist)
    bpy.utils.unregister_class(IMGMNG_UL_external_images_uilist)
