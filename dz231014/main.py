import bpy
import random
import math

n = 10
t = 100

for i in range(n):
    bpy.ops.mesh.primitive_cube_add(align='WORLD', 
                                    location=(random.randint(-10, 10), random.randint(-10, 10), random.randint(0, 100)), scale=(1, 1, 1))

for i, e in enumerate([bpy.data.objects[el] for el in bpy.data.objects.keys() if el[:4] == "Cube"]):
        e.select_set(False)
    

for j in range(t):
    for i, e in enumerate([bpy.data.objects[el] for el in bpy.data.objects.keys() if el[:4] == "Cube"]):
        e.select_set(True)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='BOUNDS')
        bpy.ops.transform.rotate(value = 0.6 + i*1, orient_axis="Z", orient_type = "CURSOR")
        
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='BOUNDS')
        bpy.ops.transform.translate(value=(-0, -0, -3))
        if bpy.context.selected_objects[0].location[2] < 0:
            bpy.ops.transform.translate(value=(-0, -0, 100))
        e.select_set(False)

        
        
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
    
for i, e in enumerate([bpy.data.objects[el] for el in bpy.data.objects.keys() if el[:4] == "Cube"]):
    e.select_set(True)
    bpy.ops.object.delete()
