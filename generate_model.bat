::CapturingReality

:: switch off console output
@echo off


:: path to RealityCapture application
set RealityCaptureExe="C:\Program Files\Capturing Reality\RealityCapture\RealityCapture.exe"

set RootFolder="C:\Users\Jamme\OneDrive\Pictures\Robotics\Photogrammetry"

:: variable storing path to images for creating model
set Images="C:\Users\Jamme\OneDrive\Pictures\Robotics\Photogrammetry\coral"

:: set a new name for calculated model
set ModelName="CoralModel"

:: run RealityCapture
%RealityCaptureExe% -addFolder %Images% ^
        -align ^
        -setReconstructionRegionAuto ^
        -calculateNormalModel ^
        -selectMarginalTriangles ^
        -removeSelectedTriangles ^
        -renameSelectedModel %ModelName% ^
        -calculateTexture ^
        -save %Project% ^
        -quit
       
        

        





