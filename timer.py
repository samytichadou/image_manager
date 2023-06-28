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

def update_3d_viewers(context):
    if context.scene.render.engine not in ['BLENDER_EEVEE','BLENDER_WORKBENCH']:
        wm = bpy.data.window_managers['WinMan']
        for window in wm.windows :
            for area in window.screen.areas :
                if area.type=='VIEW_3D' :
                    for space in area.spaces :
                        if space.type == 'VIEW_3D' and space.shading.type == 'RENDERED' :
                            space.shading.type = 'SOLID'
                            space.shading.type = 'RENDERED'

def timer_image_watcher():
    #print("IMGMNG --- Timer")
    interval = get_addon_preferences().timer_frequency

    # Reload folder
    rld.reload_available_images()

    # Reload images if needed
    chk_changes = False
    for i in bpy.data.images:
        if i.is_autoreloaded:
            if reload_image_modification_time(i):
                i.reload()
                chk_changes = True
                print(f"IMGMNG --- {i.name} reloaded")

    # Reload UI
    if chk_changes:
        print("IMGMNG --- Updating 3d views")
        update_3d_viewers(bpy.context)

    return interval


### REGISTER ---

def register():
    bpy.app.timers.register(timer_image_watcher, persistent=True)

def unregister():
    bpy.app.timers.unregister(timer_image_watcher)
