::CapturingReality

:: switch off console output
@echo off

call SetVariables.bat

:: variable storing path to images for creating model
set Images="%RootFolder%\img"

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
       
        

        





