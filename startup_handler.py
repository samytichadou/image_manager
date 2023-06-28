import bpy
from bpy.app.handlers import persistent

from .timer import reload_image_modification_time

@persistent
def reload_images_handler(scene):
    print("IMGMNG --- Reloading images modification time")
    for img in bpy.data.images:
        reload_image_modification_time(img)


### REGISTER ---

def register():
    bpy.app.handlers.load_post.append(reload_images_handler)

def unregister():
    bpy.app.handlers.load_post.remove(reload_images_handler)
