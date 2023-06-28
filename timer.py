import bpy
import os

from .operators import reload_available_images_operator as rld
from .addon_prefs import get_addon_preferences

def reload_image_modification_time(image):
    if os.path.isfile(bpy.path.abspath(image.filepath)):
        new_mod=str(os.path.getmtime(bpy.path.abspath(image.filepath)))
        if new_mod!=image.modification_time:
            image.modification_time=new_mod
            return True
    else:
        image.modification_time="missing"
        return True
    return False

def timer_image_watcher():
    #print("IMGMNG --- Timer")
    interval = get_addon_preferences().timer_frequency
    # reload folder
    rld.reload_available_images()
    # reload images if needed
    for i in bpy.data.images:
        if i.is_autoreloaded:
            if reload_image_modification_time(i):
                i.reload()
                print(f"IMGMNG --- {i.name} reloaded")
    return interval


### REGISTER ---

def register():
    bpy.app.timers.register(timer_image_watcher, persistent=True)

def unregister():
    bpy.app.timers.unregister(timer_image_watcher)
