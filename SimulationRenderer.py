# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 10:54:14 2026

@author: wjbroke
"""

from ovito.io import import_file
from ovito.vis import ViewportOverlayInterface, Viewport, PythonViewportOverlay, ColorLegendOverlay
from ovito.data import DataCollection
import ovito.vis
from ovito.modifiers import ColorCodingModifier
from ovito.qt_compat import QtCore

timearray = [9000] # The indices of the simulation dump files

concentration = 0.2 # Change these values to suit your needs
temp = 300
dt = 0.0001
width = 2.0

for t in timearray:
    file = "dump.prelim4."+ str(concentration)+"."+str(temp)+"."+str(dt)+"."+str(width)+"."+str(t)
    
    pipeline = import_file(file) # Load input file
    modifier = ColorCodingModifier(
                              property = 'xi1',
                              gradient = ColorCodingModifier.BlueWhiteRed(),
                              start_value = 0.0,
                              end_value = 1.0) # Gradient for color mapping
    pipeline.modifiers.append(modifier)
    
    pipeline.add_to_scene() # Add the pipeline to the scene
    
    data = pipeline.compute() # Compute the pipeline
    
    property1 = data.particles["Position"].array[:,1] # Y Posiiton
    property2 = data.particles["xi1"] # Atomic Molar Concentration
    
    class ScatterPlotOverlay(ViewportOverlayInterface): # This class creates a scatterplot of y-coords vs. a.m.f.
        def render(self, canvas, **kwargs):
            with canvas.mpl_figure(pos = (0.02,0.02), size = (0.35,0.35), anchor = "south west", alpha = 0.5, tight_layout=True) as fig:
                ax = fig.subplots()
                ax.scatter(property1, property2, alpha = 0.6, s=5, color = "blue")
                ax.set_title("Position vs. Atomic Molar Concentration", fontsize = 15)
                ax.set_xlabel("Y Position (Angstroms)", fontsize = 10)
                ax.set_ylabel("Atomic Molar Concentration", fontsize = 10)
    
    vp = Viewport() # Set up the viewport
    vp.type = Viewport.Type.Perspective
    vp.camera_dir = (-0.89,-0.44,0)
    vp.zoom_all()
    
    
    legend = ColorLegendOverlay(
        title = 'xi_B',
        alignment = QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom,
        orientation = QtCore.Qt.Orientation.Horizontal,
        offset_x = -0.04,
        label1 = '0%',
        label2 = '100%',
        font = 'Arial,10,-1,5,75,0,0,0,0,0,Bold',
        font_size = 0.1)
    
    legend.modifier = modifier
    
    vp.overlays.append(legend) # Add the legend to the viewport
    
    vp.overlays.append( PythonViewportOverlay( delegate=ScatterPlotOverlay())) # Add the custom scatterplot to the viewport
   
    
    vp.render_image(
        size = (1280,720),
        filename = "render2."+ str(concentration)+"."+str(temp)+"."+str(dt)+"."+str(width)+"."+str(t)+".png",
        background = (0.89,0.863,0.808), # Background color for RGB on [0,1]
        renderer = ovito.vis.OpenGLRenderer() # Use Tachyon for shadows
    ) # Render everything
    


