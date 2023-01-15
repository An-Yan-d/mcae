import bpy

def coords(objName, space='GLOBAL'):
    # Store reference to the bpy.data.objects datablock
    obj = bpy.data.objects[objName]
    
    # Store reference to bpy.data.objects[].meshes datablock
    if obj.mode == 'EDIT':
        v = bmesh.from_edit_mesh(obj.data).verts
    elif obj.mode == 'OBJECT':
        v = obj.data.vertices

    if space == 'GLOBAL':
        # Return T * L as list of tuples
        return [(obj.matrix_world @ v.co).to_tuple() for v in v]
    elif space == 'LOCAL':
        # Return L as list of tuples
        return [v.co.to_tuple() for v in v]

objs=bpy.context.selected_objects


frame_start = bpy.context.scene.frame_start
frame_end = bpy.context.scene.frame_end
filename='output'
f = open(r"F:\program\particles_MC\mcae-main\files\\"+filename+".txt", "w")

for i in range(frame_start, frame_end):
    bpy.context.scene.frame_set(i)
    bpy.context.scene.update_render_engine()
    f.write("Frame %d\n" % i)
    for o in objs:
        c=coords(o.name)
        for v in c:
            f.write("v %f %f %f\n" % (v[0], v[1], v[2]))