class Body_Octane_SK extends Actor;

#exec MESH MODELIMPORT MESH=Body_Octane_SK MODELFILE=Body_Octane_SK.psk
#exec MESH ORIGIN      MESH=Body_Octane_SK X=-0 Y=-0 Z=-0 YAW=0 PITCH=0 ROLL=0
// rotator: P=0 Y=0 R=0
#exec MESH SCALE       MESH=Body_Octane_SK X=1 Y=1 Z=1

#exec MESH ATTACHNAME  MESH=Body_Octane_SK BONE="chassis_jnt" TAG="AntennaSocket" YAW=0 PITCH=0 ROLL=0 X=-25.8564 Y=-18.1061 Z=23
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Octane_SK BONE="chassis_jnt" TAG="FrontSocket" YAW=0 PITCH=0 ROLL=0 X=78.0077 Y=0 Z=-1.5
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Octane_SK BONE="chassis_jnt" TAG="HatSocket" YAW=0 PITCH=246 ROLL=0 X=19.8932 Y=0 Z=29.5543
// rotator: P=63038 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Octane_SK BONE="chassis_jnt" TAG="RocketBoost" YAW=0 PITCH=0 ROLL=0 X=-48.5055 Y=0 Z=9
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Octane_SK BONE="chassis_jnt" TAG="BoostEmitterLeft" YAW=0 PITCH=0 ROLL=0 X=-48 Y=-9 Z=9
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Octane_SK BONE="chassis_jnt" TAG="BoostEmitterRight" YAW=0 PITCH=0 ROLL=0 X=-48 Y=9 Z=9
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Octane_SK BONE="chassis_jnt" TAG="AmbBoost_L" YAW=0 PITCH=0 ROLL=0 X=-46 Y=-14.6 Z=10.5
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Octane_SK BONE="chassis_jnt" TAG="AmbBoost_R" YAW=0 PITCH=0 ROLL=0 X=-46 Y=14.6 Z=10.5
// rotator: P=0 Y=0 R=0
#exec MESH ATTACHNAME  MESH=Body_Octane_SK BONE="root_jnt" TAG="Underglow" YAW=0 PITCH=0 ROLL=0 X=0 Y=0 Z=0
// rotator: P=0 Y=0 R=0
