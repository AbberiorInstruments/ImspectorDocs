Interpolation
-------------

Imspector offers to interpolate images. The interpolation can be done in up to four directions. In the 'Interpolation'
dialog (:ref:`fig_data_interpolation`) first the resolution of the resulting image is given. Here typically integers are used as scaling factors.
Imspector offers tu use two algorithms that can be used to interpolate the data: 'Resample' and 'Lagrange Interpolation'.

The results of the interpolation directly show the differences of the algorithms. The 'Lagrange Interpolation' leads to
rather smooth images where the 'Resample' algorithm preserves the data.

.. _fig_data_interpolation:
.. figure:: /images/data/analysis/interpolation_dialog.png
   :width: 9 cm
   :align: center

   'Interpolation' dialog.