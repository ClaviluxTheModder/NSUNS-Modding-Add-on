bl_info = {
    "name" : "NMA",
    "author" : "Clavilux", 
    "description" : "",
    "blender" : (3, 0, 1),
    "version" : (0, 0, 8),
    "location" : "",
    "waring" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "NSUNS Modding" 
}


import bpy
import bpy.utils.previews



def string_to_int(value):
    if value.isdigit():
        return int(value)
    return 0

def string_to_icon(value):
    if value in bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.keys():
        return bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items[value].value
    return string_to_int(value)
    
def icon_to_string(value):
    for icon in bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items:
        if icon.value == value:
            return icon.name
    return "NONE"
    
def enum_set_to_string(value):
    if type(value) == set:
        if len(value) > 0:
            return "[" + (", ").join(list(value)) + "]"
        return "[]"
    return value
    
def string_to_type(value, to_type, default):
    try:
        value = to_type(value)
    except:
        value = default
    return value

addon_keymaps = {}
_icons = None
panel = {}



class SNA_PT_NSUNS_MODDING_ADDON_V008_91FEB(bpy.types.Panel):
    bl_label = 'NSUNS Modding Addon v0.0.8'
    bl_idname = 'SNA_PT_NSUNS_MODDING_ADDON_V008_91FEB'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'NMA V0.0.8'
    bl_order = 0
    bl_options = {'HEADER_LAYOUT_EXPAND'}
    
    bl_ui_units_x=0
    @classmethod
    def poll(cls, context):
        return not (False)
    
    def draw_header(self, context):
        layout = self.layout
        
    def draw(self, context):
        layout = self.layout
        
        split_DF10B = layout.split(factor=0.5, align=False)
        split_DF10B.alert = False
        split_DF10B.enabled = True
        split_DF10B.use_property_split = False
        split_DF10B.use_property_decorate = False
        split_DF10B.scale_x = 1.0
        split_DF10B.scale_y = 1.0
        split_DF10B.alignment = 'Expand'.upper()
        op = layout.operator('mesh.vertex_color_add', text='Add Vertex Color', icon_value=31, emboss=True, depress=False)
        op = layout.operator('mesh.vertex_color_remove', text='Remove Vertex Color', icon_value=32, emboss=True, depress=False)
        op = layout.operator('object.modifier_add', text='Add Modifier', icon_value=94, emboss=True, depress=False)
        split_6D8E0 = layout.split(factor=0.5, align=False)
        split_6D8E0.alert = False
        split_6D8E0.enabled = True
        split_6D8E0.use_property_split = False
        split_6D8E0.use_property_decorate = False
        split_6D8E0.scale_x = 1.0
        split_6D8E0.scale_y = 1.0
        split_6D8E0.alignment = 'Expand'.upper()
        op = layout.operator('mesh.uv_texture_remove', text='Remove UV Map', icon_value=32, emboss=True, depress=False)
        op = layout.operator('mesh.uv_texture_add', text='Add UV Map', icon_value=31, emboss=True, depress=False)
        op = layout.operator('object.remove_lod', text='A Random Button', icon_value=0, emboss=True, depress=False)



def register():
    
    global _icons
    _icons = bpy.utils.previews.new()
    
    
    bpy.utils.register_class(SNA_PT_NSUNS_MODDING_ADDON_V008_91FEB)

def unregister():
    
    global _icons
    bpy.utils.previews.remove(_icons)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    
    bpy.utils.unregister_class(SNA_PT_NSUNS_MODDING_ADDON_V008_91FEB)

