import bpy

class IMGMNG_PR_properties(bpy.types.PropertyGroup) :
    active_local_image_index : bpy.props.IntProperty(
        name='Local Image Index',
        )
    active_available_image_index : bpy.props.IntProperty(
        name='Available Image Index',
        )


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_PR_properties)
    bpy.types.Scene.imgmng_properties = \
        bpy.props.PointerProperty(type = IMGMNG_PR_properties, name="Image Manager Properties")

def unregister():
    bpy.utils.unregister_class(IMGMNG_PR_properties)
    del bpy.types.Scene.imgmng_properties