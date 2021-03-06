Smoothing
---------

In Imspector images can be smoothed using the 'Smooth stack' dialog (:ref:`fig_data_smoothing`).
To smooth an image, the stack that should be smoothed is selected on the left side of the dialog.
Then the type of smoothing has to be selected on the right side. Imspector offers different methods to smooth images:

- Typically smoothing is performed using Gaussian kernels with different sizes. To smooth an image using a Gaussian select
  'Smooth' on the right side as 'Smoothing Type'.
- 'Median' allows to apply a median filter. This is commonly done to reduce 'salt & pepper noise'.
- Lowpass gauss
- Lowpass cutoff

.. _fig_data_smoothing:
.. figure:: /images/data/analysis/smooth_dialog.png
   :width: 9 cm
   :align: center

   'Smooth Stack' dialog.

