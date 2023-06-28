# INSTALATION STEPS

- Follow the step to install Vicalib from the original source:
   https://github.com/arpg/vicalib
- Instead of compiling the original, compile the version in the Vicalib folder of this repository.

# AUXILIAR CODE

- Calibrate_all.sh
   Launch calibration for each endoscope with the parameters used in the paper.
- PlotInliers_outliers.py [input.txt with all points from vicalib] [output.pdf for the plot]
   Plot final inliers of the Vicalib calibration and its position in the image.
- Summary_calibration.py [ list of xml files one for each endoscope ]
   Plot distortion curves for each endoscope.
- Reproject.py [ list of xml files one for each endoscope ]
   Plot the undistortion of a grid for each endoscope.

# EXAMPLE OF LAUNCH FOR ENDOSCOPE CALIBRATION AND OBTAIN ALL INFORMATION

- vicalib -grid_preset small -remove_outliers true -grid_small_rad 0.000848 -grid_large_rad 0.0007925 -grid_spacing 0.004224 -max_iters 5000 -models kb4 -frame_skip 45 -cam opencv://Endoscope_01.mov -output Endoscope_01/Endoscope_01.xml -log_dir Endoscope_01/ > Endoscope_01/Endoscope_01.txt
- python3 PlotInliers_outliers.py Endoscope_01/Endoscope_01.txt Endoscope_01/Endoscope_01.pdf
- python3 Summary_calibration.py Endoscope_01/Endoscope_01.xml
- python3 Reproject.py Endoscope_01/Endoscope_01.xml
