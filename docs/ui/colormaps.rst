==========
Color maps
==========

In Imspector the colormap ‘Fire' is typically selected (Fig. 1). Furthermore a variety of built-in colormaps can be chosen (Fig. 2)
The active colormap is displayed at the bottom of the measurement window. On the left and right bottom of the colormap,
the minimum and maximum gray value is given. In a stack view the colormap is adjusted to the maximum/minimum of the current selection.

.. figure:: /images/ui/colormap_fire.jpg
   :width: 12 cm
   :align: center

   'Fire' colormap.

Properties of the colormap can be changed using right-click context menu. To access this menu the active colormap has to be right-clicked.

Changing the Colormap
---------------------

Enter colormap right-click context menu. To change the colormap choose the first entry of the menu ‘Colormap' and simply
select the colormap of choice.

.. figure:: /images/ui/colormaps.jpg
   :width: 14 cm
   :align: center

   Built-in colormaps.

Copy Colormaps

Colormaps can be copied between measurements using standard Windows shortcuts.

1. The colormap has to be selected using left-click and is copied using :kbd:`ctrl + c`. Then insert the copied colormap
   into the new image using :kbd:`ctrl + v`
2. Alternatively, the colormap can be copied using drag and drop. To this end, the active colormap has to be selected
   using :kbd:`ctrl + left-click`, drag to the new image and drop it.

Locking the Minimum/Maximum Gray Values of the Colormap
Enter colormap right-click context menu. To fix the gray values of the colormap, choose 'Lock' and select if you like to
fix the maximum or the minimum value.
Note that this option may be particularly helpful during image acquisition.

Linear and Logarithmic Representation of the Colormap
In Imspector gray values can be represented in a linear or logarithmic mode. Typically the colormap is set to a linear mode.
To change the colormap mode to logarithmic scale, please enter colormap right-click context menu and click 'Logarithmic'.
If the logarithmic mode is active, a tick is shown in front of this entry.

Adjusting the Colormap Values
The displayed minimum and maximum gray values can be adjusted by different means

1. The respective value can be accessed and changed after double-clicking the value at the bottom of the colormap.
2. The values can be adjusted to the minimum/maximum gray value of the image or a selected region in the colormap right-click context menu.
3. The values can be adjusted to the minimum/maximum gray value of the image or a selected region by pressing :kbd:`F9 / F10`.
   (F9: maximum value; F10: minimum value).

Note that the colormap must be visible at the bottom to do this.

Custom Colormaps

In addition, new colormaps can be created using a colormap editor (Fig. 3). To create a custom colormap, the colormap
editor has to be opened. To this end, the colormap context has to be opened by right-clicking the active colormap.
Then select 'New'.

.. figure:: /images/ui/colormap_custom_dialog.png
   :width: 8 cm
   :align: center

   'Colormap editor' dialog.

Note that colormaps can be saved and loaded again.