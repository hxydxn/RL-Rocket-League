class Body_Darkcar_SK extends Actor;

#exec MESH MODELIMPORT MESH=Body_Darkcar_SK MODELFILE=Body_Darkcar_SK.psk
#exec MESH ORIGIN      MESH=Body_Darkcar_SK X=-0 Y=-0 Z=-0 YAW=0 PITCH=0 ROLL=0
// rotator: P=0 Y=0 R=0
#exec MESH SCALE       MESH=Body_Darkcar_SK X=1 Y=1 Z=1

#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="chassis_jnt" TAG="RocketBoost" YAW=0 PITCH=0 ROLL=0 X=-61.9053 Y=0 Z=3.75
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="chassis_jnt" TAG="AntennaSocket" YAW=0 PITCH=0 ROLL=0 X=-13.5221 Y=-17.7708 Z=12.5
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="chassis_jnt" TAG="HatSocket" YAW=0 PITCH=0 ROLL=0 X=-6.72362 Y=0 Z=22
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="chassis_jnt" TAG="FrontSocket" YAW=0 PITCH=0 ROLL=0 X=86.025 Y=0 Z=-7
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="chassis_jnt" TAG="Underglow" YAW=0 PITCH=0 ROLL=0 X=0 Y=0 Z=-18.25
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="chassis_jnt" TAG="L_Front_Light_03" YAW=0 PITCH=0 ROLL=0 X=81.5 Y=-3 Z=1.75
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="chassis_jnt" TAG="R_Front_Light_03" YAW=0 PITCH=0 ROLL=0 X=81.5 Y=3 Z=1.75
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="FL_Pivot_jnt" TAG="L_Front_Light_01" YAW=0 PITCH=0 ROLL=0 X=17 Y=-7.5 Z=1
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="FR_Pivot_jnt" TAG="R_Front_Light_01" YAW=0 PITCH=0 ROLL=0 X=17 Y=7.5 Z=1
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="FR_Pivot_jnt" TAG="R_Front_Light_02" YAW=0 PITCH=0 ROLL=0 X=8 Y=-3.5 Z=11
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="FL_Pivot_jnt" TAG="L_Front_Light_02" YAW=0 PITCH=0 ROLL=0 X=8 Y=3.5 Z=11
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="BR_WheelTranslation_jnt" TAG="R_Rear_Light" YAW=128 PITCH=0 ROLL=0 X=-17 Y=13 Z=15.1
// rotator: P=0 Y=32768 R=0
#exec MESH ATTACHNAME  MESH=Body_Darkcar_SK BONE="BL_WheelTranslation_jnt" TAG="L_Rear_Light" YAW=128 PITCH=0 ROLL=0 X=-17 Y=-13 Z=15.1
// rotator: P=0 Y=32768 R=0
