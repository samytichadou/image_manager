import bpy
import os


def return_image_folder():
    from ..addon_prefs import get_addon_preferences
    path=os.path.dirname(bpy.data.filepath)
    return os.path.join(path, get_addon_preferences().folder_name)

def open_in_explorer(path) :
    import platform
    import subprocess
    #windows
    if platform.system() == "Windows":
        if os.path.isfile(path):
            subprocess.Popen(r'explorer /select, "%s"' % path)
        else:
            subprocess.Popen(['explorer', path])
    #mac
    elif platform.system() == "Darwin":
        if os.path.isfile(path):
            subprocess.Popen(["open", "-a", "Finder", path])
        else:
            subprocess.Popen(["open", path])
    #linux
    else:
        if os.path.isfile(path):
            subprocess.Popen(["xdg-open", os.path.dirname(path)])
        else:
            subprocess.Popen(["xdg-open", path])

class IMGMNG_OT_create_image_folder(bpy.types.Operator):
    bl_idname = "imgmng.create_image_folder"
    bl_label = "Create Folder"
    bl_description = "Create external image folder."
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return bpy.data.is_saved

    def execute(self, context):
        folderpath=return_image_folder()
        if os.path.isdir(folderpath):
            self.report({'WARNING'}, "Folder already exists")
            return {'FINISHED'}
        os.mkdir(folderpath)
        self.report({'INFO'}, f"Folder created : {folderpath}")
        return {'FINISHED'}

class IMGMNG_OT_open_filepath(bpy.types.Operator):
    bl_idname = "imgmng.open_filepath"
    bl_label = "Open Folder"
    bl_description = "Open external image folder."
    bl_options = {'INTERNAL'}

    filepath: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        if not os.path.isdir(self.filepath) and\
        not os.path.isfile(self.filepath):
            self.report({'WARNING'}, "Folder/File does not exist")
            return {'FINISHED'}
        open_in_explorer(f"{self.filepath}/")
        self.report({'INFO'}, f"Folder opened : {self.filepath}")
        return {'FINISHED'}


### REGISTER ---

def register():
    bpy.utils.register_class(IMGMNG_OT_create_image_folder)
    bpy.utils.register_class(IMGMNG_OT_open_filepath)

def unregister():
    bpy.utils.unregister_class(IMGMNG_OT_create_image_folder)
    bpy.utils.unregister_class(IMGMNG_OT_open_filepath)
