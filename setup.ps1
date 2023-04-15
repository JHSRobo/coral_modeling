Remove-Item -Path "C:\Users\Jamme\OneDrive\Pictures\Robotics\Photogrammetry\coral\*.png"

Copy-Item -Path "\\wsl.localhost\Ubuntu-20.04\home\jhsrobo\ROVMIND\ros_workspace\src\img_capture\img\coral\*.png" -Destination "C:\Users\Jamme\OneDrive\Pictures\Robotics\Photogrammetry\coral"
