# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# This addon was created with the Serpens - Visual Scripting Addon.
# This code is generated from nodes and is not intended for manual editing.
# You can find out more about Serpens at <https://blendermarket.com/products/serpens>.


bl_info = {
    "name": "NSUNS Modding Addon",
    "description": "This Is A Modding Addon For NSUNS4",
    "author": "Clavilux",
    "version": (0, 0, 3),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "Some Bugs May Occur",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Modding"
}


###############   IMPORTS
import bpy
from bpy.utils import previews
import os
import math


###############   INITALIZE VARIABLES
###############   SERPENS FUNCTIONS
def exec_line(line):
    exec(line)

def sn_print(tree_name, *args):
    if tree_name in bpy.data.node_groups:
        item = bpy.data.node_groups[tree_name].sn_graphs[0].prints.add()
        for arg in args:
            item.value += str(arg) + ";;;"
        for area in bpy.context.screen.areas:
            area.tag_redraw()
    print(*args)

def sn_cast_string(value):
    return str(value)

def sn_cast_boolean(value):
    if type(value) == tuple:
        for data in value:
            if bool(data):
                return True
        return False
    return bool(value)

def sn_cast_float(value):
    if type(value) == str:
        try:
            value = float(value)
            return value
        except:
            return float(bool(value))
    elif type(value) == tuple:
        return float(value[0])
    elif type(value) == list:
        return float(len(value))
    elif not type(value) in [float, int, bool]:
        try:
            value = len(value)
            return float(value)
        except:
            return float(bool(value))
    return float(value)

def sn_cast_int(value):
    return int(sn_cast_float(value))

def sn_cast_boolean_vector(value, size):
    if type(value) in [str, bool, int, float]:
        return_value = []
        for i in range(size):
            return_value.append(bool(value))
        return tuple(return_value)
    elif type(value) == tuple:
        return_value = []
        for i in range(size):
            return_value.append(bool(value[i]) if len(value) > i else bool(value[0]))
        return tuple(return_value)
    elif type(value) == list:
        return sn_cast_boolean_vector(tuple(value), size)
    else:
        try:
            value = tuple(value)
            return sn_cast_boolean_vector(value, size)
        except:
            return sn_cast_boolean_vector(bool(value), size)

def sn_cast_float_vector(value, size):
    if type(value) in [str, bool, int, float]:
        return_value = []
        for i in range(size):
            return_value.append(sn_cast_float(value))
        return tuple(return_value)
    elif type(value) == tuple:
        return_value = []
        for i in range(size):
            return_value.append(sn_cast_float(value[i]) if len(value) > i else sn_cast_float(value[0]))
        return tuple(return_value)
    elif type(value) == list:
        return sn_cast_float_vector(tuple(value), size)
    else:
        try:
            value = tuple(value)
            return sn_cast_float_vector(value, size)
        except:
            return sn_cast_float_vector(sn_cast_float(value), size)

def sn_cast_int_vector(value, size):
    return int(sn_cast_float_vector(value, size))

def sn_cast_color(value, use_alpha):
    length = 4 if use_alpha else 3
    value = sn_cast_float_vector(value, length)
    tuple_list = []
    for data in range(length):
        data = value[data] if len(value) > data else value[0]
        tuple_list.append(sn_cast_float(min(1, max(0, data))))
    return tuple(tuple_list)

def sn_cast_list(value):
    if type(value) in [str, tuple, list]:
        return list(value)
    elif type(value) in [int, float, bool]:
        return [value]
    else:
        try:
            value = list(value)
            return value
        except:
            return [value]

def sn_cast_blend_data(value):
    if type(value) in [tuple, bool, int, float, list]:
        return None
    elif type(value) == str:
        try:
            value = eval(value)
            return value
        except:
            return None
    else:
        return None

def sn_cast_enum(string, enum_values):
    for item in enum_values:
        if item[1] == string:
            return item[0]
        elif item[0] == string.upper():
            return item[0]
    return string


###############   IMPERATIVE CODE
###############   EVALUATED CODE
#######   NSUNS Modding Addon
class SNA_PT_NSUNS_Modding_Addon_35A0F(bpy.types.Panel):
    bl_label = "NSUNS Modding Add-on"
    bl_idname = "SNA_PT_NSUNS_Modding_Addon_35A0F"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = 'object'
    bl_category = 'Modding'
    bl_order = 0


    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        try:
            layout = self.layout
        except Exception as exc:
            print(str(exc) + " | Error in NSUNS Modding Add-on panel header")

    def draw(self, context):
        try:
            layout = self.layout
            op = layout.operator("xfbin_panel.copy_group",text=r"Copy Mesh Properties",emboss=True,depress=False,icon_value=598)
            op.prop_path = r"xfbin_mesh_data"
            op.prop_name = r"Mesh Properties"
            op = layout.operator("xfbin_panel.paste_group",text=r"Overwrite Mesh Properties",emboss=True,depress=False,icon_value=601)
            op.prop_path = r"xfbin_mesh_data"
            op.prop_name = r"Mesh Properties"
            layout.separator(factor=1.0)
            op = layout.operator("mesh.vertex_color_add",text=r"Add Vertex Color",emboss=True,depress=False,icon_value=31)
            op = layout.operator("mesh.vertex_color_remove",text=r"Remove Vertex Color",emboss=True,depress=False,icon_value=32)
            op = layout.operator("object.modifier_add",text=r"Add Modifier",emboss=True,depress=False,icon_value=241)
            op.type = sn_cast_enum(r"ARMATURE", [("DATA_TRANSFER","Data Transfer","Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another"),("MESH_CACHE","Mesh Cache","Deform the mesh using an external frame-by-frame vertex transform cache"),("MESH_SEQUENCE_CACHE","Mesh Sequence Cache","Deform the mesh or curve using an external mesh cache in Alembic format"),("NORMAL_EDIT","Normal Edit","Modify the direction of the surface normals"),("WEIGHTED_NORMAL","Weighted Normal","Modify the direction of the surface normals using a weighting method"),("UV_PROJECT","UV Project","Project the UV map coordinates from the negative Z axis of another object"),("UV_WARP","UV Warp","Transform the UV map using the difference between two objects"),("VERTEX_WEIGHT_EDIT","Vertex Weight Edit","Modify of the weights of a vertex group"),("VERTEX_WEIGHT_MIX","Vertex Weight Mix","Mix the weights of two vertex groups"),("VERTEX_WEIGHT_PROXIMITY","Vertex Weight Proximity","Set the vertex group weights based on the distance to another target object"),("ARRAY","Array","Create copies of the shape with offsets"),("BEVEL","Bevel","Generate sloped corners by adding geometry to the mesh's edges or vertices"),("BOOLEAN","Boolean","Use another shape to cut, combine or perform a difference operation"),("BUILD","Build","Cause the faces of the mesh object to appear or disappear one after the other over time"),("DECIMATE","Decimate","Reduce the geometry density"),("EDGE_SPLIT","Edge Split","Split away joined faces at the edges"),("MASK","Mask","Dynamically hide vertices based on a vertex group or armature"),("MIRROR","Mirror","Mirror along the local X, Y and/or Z axes, over the object origin"),("MULTIRES","Multiresolution","Subdivide the mesh in a way that allows editing the higher subdivision levels"),("REMESH","Remesh","Generate new mesh topology based on the current shape"),("SCREW","Screw","Lathe around an axis, treating the input mesh as a profile"),("SKIN","Skin","Create a solid shape from vertices and edges, using the vertex radius to define the thickness"),("SOLIDIFY","Solidify"," Make the surface thick"),("SUBSURF","Subdivision Surface","Split the faces into smaller parts, giving it a smoother appearance"),("TRIANGULATE","Triangulate","Convert all polygons to triangles"),("WELD","Weld","Find groups of vertices closer then dist and merges them together"),("WIREFRAME","Wireframe","Convert faces into thickened edges"),("ARMATURE","Armature","Deform the shape using an armature object"),("CAST","Cast","Shift the shape towards a predefined primitive"),("CURVE","Curve","Bend the mesh using a curve object"),("DISPLACE","Displace","Offset vertices based on a texture"),("HOOK","Hook","Deform specific points using another object"),("LAPLACIANDEFORM","Laplacian Deform","Deform based a series of anchor points"),("LATTICE","Lattice","Deform using the shape of a lattice object"),("MESH_DEFORM","Mesh Deform","Deform using a different mesh, which acts as a deformation cage"),("SHRINKWRAP","Shrinkwrap","Project the shape onto another object"),("SIMPLE_DEFORM","Simple Deform","Deform the shape by twisting, bending, tapering or stretching"),("SMOOTH","Smooth","Smooth the mesh by flattening the angles between adjacent faces"),("CORRECTIVE_SMOOTH","Smooth Corrective","Smooth the mesh while still preserving the volume"),("LAPLACIANSMOOTH","Smooth Laplacian","Reduce the noise on a mesh surface with minimal changes to its shape"),("SURFACE_DEFORM","Surface Deform","Transfer motion from another mesh"),("WARP","Warp","Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects"),("WAVE","Wave","Adds a ripple-like motion to an object’s geometry"),("CLOTH","Cloth",""),("COLLISION","Collision",""),("DYNAMIC_PAINT","Dynamic Paint",""),("EXPLODE","Explode","Break apart the mesh faces and let them follow particles"),("FLUID","Fluid",""),("OCEAN","Ocean","Generate a moving ocean surface"),("PARTICLE_INSTANCE","Particle Instance",""),("PARTICLE_SYSTEM","Particle System","Spawn particles from the shape"),("SOFT_BODY","Soft Body",""),("SURFACE","Surface",""),("SIMULATION","Simulation",""),])
            layout.separator(factor=1.2000000476837158)
            op = layout.operator("mesh.uv_texture_remove",text=r"Remove UV Map",emboss=True,depress=False,icon_value=19)
            op = layout.operator("mesh.uv_texture_add",text=r"Add UV Map",emboss=True,depress=False,icon_value=31)
        except Exception as exc:
            print(str(exc) + " | Error in NSUNS Modding Add-on panel")


###############   REGISTER ICONS
def sn_register_icons():
    icons = []
    bpy.types.Scene.nsuns_modding_addon_icons = bpy.utils.previews.new()
    icons_dir = os.path.join( os.path.dirname( __file__ ), "icons" )
    for icon in icons:
        bpy.types.Scene.nsuns_modding_addon_icons.load( icon, os.path.join( icons_dir, icon + ".png" ), 'IMAGE' )

def sn_unregister_icons():
    bpy.utils.previews.remove( bpy.types.Scene.nsuns_modding_addon_icons )


###############   REGISTER PROPERTIES
def sn_register_properties():
    pass

def sn_unregister_properties():
    pass


###############   REGISTER ADDON
def register():
    sn_register_icons()
    sn_register_properties()
    bpy.utils.register_class(SNA_PT_NSUNS_Modding_Addon_35A0F)


###############   UNREGISTER ADDON
def unregister():
    sn_unregister_icons()
    sn_unregister_properties()
    bpy.utils.unregister_class(SNA_PT_NSUNS_Modding_Addon_35A0F)