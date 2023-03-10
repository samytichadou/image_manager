import bpy

class IMGMNG_PR_available_images(bpy.types.PropertyGroup) :
    filepath : bpy.props.StringProperty(
        name='Available Image Filepath',
        )
    imported : bpy.props.BoolProperty()

class IMGMNG_PR_properties(bpy.types.PropertyGroup) :
    available_images: bpy.props.CollectionProperty(
        type = IMGMNG_PR_available_images,
        name="Available Images",
        )

    active_local_image_index : bpy.props.IntProperty(
        name='Local Image Index',
        )
    active_available_image_index : bpy.props.IntProperty(
        name='Available Image Index',
        )

class IMGMNG_PR_image_parents(bpy.types.PropertyGroup) :
    type_items = [
        ('MATERIAL', 'Material', ""),
        ('WORLD', 'World', ""),
        ('NODEGROUP', 'NodeGroup', ""),
    ]
    type : bpy.props.EnumProperty(name = "Type", items = type_items, default = 'MATERIAL')
    filepath : bpy.props.StringProperty(
        name='Available Image Filepath',
        )    


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_PR_available_images)
    bpy.utils.register_class(IMGMNG_PR_properties)
    bpy.types.Scene.imgmng_properties = \
        bpy.props.PointerProperty(type = IMGMNG_PR_properties, name="Image Manager Properties")

    bpy.types.Image.is_autoreloaded = \
        bpy.props.BoolProperty(name="Image autoreloaded")
    bpy.types.Image.modification_time = \
        bpy.props.StringProperty(name="Image modification time")

def unregister():
    bpy.utils.unregister_class(IMGMNG_PR_available_images)
    bpy.utils.unregister_class(IMGMNG_PR_properties)
    
    del bpy.types.Scene.imgmng_properties
    del bpy.types.Image.modification_time
