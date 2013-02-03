import bpy
import string
import os

# Get the font name
fontName = os.getenv('fontName')
if fontName == None:
    raise ValueError('The value of fontName is mandatory')
else:
    fontFile = fontName
    fontName = fontName.split('.')[0]

if not os.path.isdir(os.getcwd() + '/' + fontName):
    os.mkdir(os.getcwd() + '/' + fontName)

# Clean scene
for obj in bpy.data.objects:
    obj.select = True
bpy.ops.object.delete()

# Init the text object
bpy.ops.font.open(filepath='whitrabt.ttf')
bpy.ops.object.text_add()
text = bpy.data.objects['Text']
text.data.extrude = 0.2
text.data.font = bpy.data.fonts[1]
bpy.ops.transform.rotate(90, axis=(1,0,0))
bpy.ops.transform.rotate(90, axis=(0,0,1))

for letter in string.ascii_letters + string.digits:
    text.data.body = letter
    path = os.getcwd() + '/' + fontName + '/' + letter + '.obj'
    bpy.ops.export_scene.obj(
            filepath=path,
            use_triangles=True,
            use_normals=True,
            use_materials=False,
            use_blen_objects=False,
            axis_forward='X',
            axis_up='Z')
