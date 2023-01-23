import bpy
import os

from .operators import folder_actions_operator as fld

def return_image_users(image):
    if image.use_fake_user:
        return image.users-1
    else:
        return image.users


# Internal Images
class IMGMNG_UL_internal_images_uilist(bpy.types.UIList):

    show_internal : bpy.props.BoolProperty(name = "Show Internals", description = "Show internal images")

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, flt_flag) :
        row = layout.row(align = True)

        # internal files
        if item.source in {'VIEWER','GENERATED'} \
        or not item.filepath:
            row.label(text="", icon="DOT")
            row.label(text="", icon="GHOST_ENABLED")
            row.label(text=item.name)

        # external files
        else:
            # RESOURCES FOLDER
            folderpath=fld.return_image_folder()
            if os.path.dirname(bpy.path.abspath(item.filepath))==folderpath:
                row.label(text="", icon="CHECKMARK")
            else:
                row.operator('imgmng.copy_image', text="", icon="FOLDER_REDIRECT").image=item.name

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

            # ADDITIONAL OPERATORS
            row.operator('imgmng.reload_image', text="", icon="FILE_REFRESH").image=item.name
            row.operator('imgmng.remove_image', text="", icon="X").image=item.name

    # def filter_items(self, context, data, propname):
    #     filtered = []
    #     ordered = []
    #
    #     items = getattr(data, propname)
    #
    #     # # Initialize with all items visible
    #     # flt_flags = [self.bitflag_filter_item] * len(items)
    #
    #     # Filter
    #     # if self.filter_by_random_prop:
    #
    #     # Name filtering
    #     if self.filter_name:
    #         helpers = bpy.types.UI_UL_list
    #         filtered = helpers.filter_items_by_name(
    #             self.filter_name,
    #             self.bitflag_filter_item,
    #             items,
    #             "name",
    #             reverse=False
    #             )
    #     else:
    #         # Initialize with all items visible
    #         filtered = [self.bitflag_filter_item] * len(items)
    #
    #     # Internal image filtering
    #     for i, item in enumerate(items):
    #         print(item.name)
    #         if item.source not in {'VIEWER','GENERATED'} \
    #         or not item.filepath:
    #             # filtered[i] &= ~self.bitflag_filter_item
    #             filtered[i] = self.bitflag_filter_item
    #
    #     # Invert the filter
    #     if filtered:
    #         show_flag = self.bitflag_filter_item & ~self.bitflag_filter_item
    #
    #         for i, bitflag in enumerate(filtered):
    #             if bitflag == show_flag:
    #                 filtered[i] = self.bitflag_filter_item
    #             else:
    #                 filtered[i] &= ~self.bitflag_filter_item
    #
    #     # for idx, item in enumerate(items) :
    #     #     if item.source in {'VIEWER','GENERATED'} \
    #     #     or not item.filepath:
    #     #         flt_flags[idx] &= ~self.bitflag_filter_item
    #
    #     return filtered, ordered

# External Images
class IMGMNG_UL_external_images_uilist(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, flt_flag) :
        row = layout.row(align = True)

        if item.imported:
            row.label(text="", icon="FILE_BLEND")
        else:
            row.operator('imgmng.import_image', text="", icon="IMPORT").filepath=item.filepath
        row.label(text=item.name)



### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_UL_internal_images_uilist)
    bpy.utils.register_class(IMGMNG_UL_external_images_uilist)

def unregister():
    bpy.utils.unregister_class(IMGMNG_UL_internal_images_uilist)
    bpy.utils.unregister_class(IMGMNG_UL_external_images_uilist)
