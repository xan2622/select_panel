# ----- BEGIN GPL LICENSE BLOCK -----
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ----- END GPL LICENSE BLOCK -----

bl_info = {
    "name" : "Select panel",
    "author" : "Daniel Calderón",
    "description" : "Select Panel",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

class View3DPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Select"

    @classmethod
    def poll(cls, context):
        return (context.object is not None)


class SelectPanelObj(View3DPanel, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_test_2"
    bl_label = "Select Panel"
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Select")
        col = layout.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.5
        row.operator("object.select_all", text="All").action='SELECT'
        row.operator("object.select_all", text="None").action='DESELECT'
        row.operator("object.select_all", text="Invert").action='INVERT'
        
        layout.label(text="select")
        col = layout.column(align=True)
        col.scale_y = 1.5
        row = col.row(align=True)
        row.operator("view3d.select_box", text="Box")
        row.operator("view3d.select_circle", text="Brush")
        col.operator("object.select_by_type")
        
        col = layout.column(align=True)
        col.scale_y = 1.5
        row = col.row(align=True)
        row.operator("object.select_camera", text="Camera")
        row.operator("object.select_mirror", text="Mirror")
        row.operator("object.select_random", text="Random")
        
        col = layout.column(align=True)
        col.scale_y = 1.5
        row = col.row(align=True)
        row.operator("object.select_more")
        row.operator("object.select_less")
        
        col = layout.column(align=True)
        col.scale_y = 1.5
        col.operator_menu_enum("object.select_grouped", "type", text="Grouped...")
        col.operator_menu_enum("object.select_linked", "type", text="Linked...")
        col.operator("object.select_pattern", text="Search name")
        
        
class SelectPanelMesh(View3DPanel, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_test_3"
    bl_label = "Select Panel"
    bl_context ="mesh_edit"

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Select")
        row = layout.row(align=True)
        row.scale_y = 1.3
        row.operator("mesh.select_all", text="All").action = 'SELECT'
        row.operator("mesh.select_all", text="None").action = 'DESELECT'
        row.operator("mesh.select_all", text="Invert").action = 'INVERT'
        
        row = layout.row(align=True)
        row.scale_y = 1.3
        row.operator("view3d.select_box", text="Box")
        row.operator("view3d.select_circle", text="Circle")
        
        row = layout.row(align=True)
        row.scale_y = 1.3
        row.operator("mesh.select_random", text="Random")
        row.operator("mesh.select_nth", text="Checker Des")
        
        col = layout.column(align=True)
        col.scale_y = 1.3
        col.operator("mesh.edges_select_sharp")
        
        

        col = layout.column(align=True)
        col.scale_y = 2
        col.operator("mesh.select_similar", text="Similar")
        
        col = layout.column(align=True)
        col.operator("mesh.select_non_manifold", text="Non Manifold")
        col.operator("mesh.select_loose", text="Loose")
        col.operator("mesh.select_interior_faces", text="Interior faces")
        col.operator("mesh.select_face_by_sides", text="By sides")
        col.operator("mesh.select_ungrouped", text="Ungrouped verts")
        
        col = layout.column(align=True)
        col.scale_y = 2
        row = col.row(align=True)
        row.scale_x = 4
        row.operator("mesh.select_more", text="", icon="ADD")
        row.operator("mesh.select_less", text="", icon="REMOVE")
        row.operator("mesh.select_next_item", text="", icon="FRAME_NEXT")
        row.operator("mesh.select_prev_item", text="", icon="FRAME_PREV")
        

        col = layout.column(align=True)
        col.scale_y = 1.3
        row = col.row(align=True)
        row.operator("mesh.loop_multi_select", text="Loop").ring=False
        row.operator("mesh.loop_multi_select", text="Ring").ring=True
        row = col.row(align=True)
        row.operator("mesh.loop_to_region", text="Loop inner region").select_bigger=False
        row.operator("mesh.region_to_loop", text="Boundary Loop")
        
 
        row = layout.row(align=True)
        row.scale_y = 1.3
        row.operator("mesh.select_linked", text="Linked")        
        row.operator("mesh.shortest_path_select", text="Shortest")        
        row.operator("mesh.faces_select_linked_flat", text="Coplanar")
        

        col = layout.column(align=True)
        col.scale_y = 1.3
        col.operator("mesh.select_axis")
        col.operator("mesh.select_mirror")
        col.operator("mesh.ext_deselect_boundary")
        
        
        
        
def register():
    bpy.utils.register_class(SelectPanelObj)
    bpy.utils.register_class(SelectPanelMesh)


def unregister():
    bpy.utils.unregister_class(SelectPanelObj)
    bpy.utils.unregister_class(SelectPanelMesh)

if __name__ == "__main__":
    register()
