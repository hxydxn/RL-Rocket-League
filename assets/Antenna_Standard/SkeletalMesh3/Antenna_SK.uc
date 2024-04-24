class Antenna_SK extends Actor;

#exec MESH MODELIMPORT MESH=Antenna_SK MODELFILE=Antenna_SK.psk
#exec MESH ORIGIN      MESH=Antenna_SK X=-0 Y=-0 Z=-0 YAW=0 PITCH=0 ROLL=0
// rotator: P=0 Y=0 R=0
#exec MESH SCALE       MESH=Antenna_SK X=1 Y=1 Z=1

#exec MESH ATTACHNAME  MESH=Antenna_SK BONE="Bone004" TAG="TopperSocket" YAW=64 PITCH=0 ROLL=192 X=9.5 Y=0 Z=0
// rotator: P=0 Y=16384 R=49152
