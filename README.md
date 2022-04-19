# A recreation in Blender and Python of the multi-plane microscopy techniques

Multiplane microscopy is a technique to obtain 3D information by measuring multiple foci and checking which focus produces the sharpest image of the tracer particle.
Using a camera set-up as shown, with the horizontal line as the point of focus (note that distances are in metres because they are inconsequential in blender):

<p float="left">
  <img src="https://github.com/H00267382/Multiplane-Microscopy/blob/main/11%20top%20view.png" height="500" width="30%" />
  <img src="https://github.com/H00267382/Multiplane-Microscopy/blob/main/12%20top%20view.png" height="500" width="30%" /> 
  <img src="https://github.com/H00267382/Multiplane-Microscopy/blob/main/13%20top%20view.png" height="500" width="30%" />
</p>

Which produces Input images:

<p float="left">
  <img src="https://github.com/H00267382/Multiplane-Microscopy/blob/main/11.0-min.png" width="30%" />
  <img src="https://github.com/H00267382/Multiplane-Microscopy/blob/main/12.0-min.png" width="30%" /> 
  <img src="https://github.com/H00267382/Multiplane-Microscopy/blob/main/13.0-min.png" width="30%" />
</p>

The python file provided as **Sharpness.py** calculates the sharpness of each image and from that it predicts the location of the bead.

The output text reads:

----

**The predicted z value based on sharpness is 12.875 m**

**With 24 samples**

----

And produces a graph:

![BeadSharpness](https://user-images.githubusercontent.com/66416355/164016315-c415fbfc-28e3-4c68-9687-c34b44b6abc2.png)


A visual of undersampling below shows why the function is inaccurate with only 9 planes.

The first graph shows sampling of 12 planes, the second shows sampling of 8 planes and the final graph shows sampling 6 planes.

<p float="left">
  <img src="https://user-images.githubusercontent.com/66416355/164022541-6b483feb-a36d-49d8-926c-094fdfa49878.png" width="33%" />
  <img src="https://user-images.githubusercontent.com/66416355/164022551-17cfa292-4245-46ad-913e-bab9dca9e186.png" width="33%" /> 
  <img src="https://user-images.githubusercontent.com/66416355/164022552-3274b2d0-4196-4840-b5f3-f4523c171111.png" width="33%" />
</p>
