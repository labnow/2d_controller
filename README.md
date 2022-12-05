# demo algorithm

纵向控制器算法用c实现，编译成shared library，通过Carla python api在Carla simulator内验证

longitudinal PID controller implemented in c
simulate in Carla via python api

## usage

```bash
# terminal 1
./CarlaUE4.sh /Game/Maps/RaceTrack -windowed -carla-server -benchmark -fps=30

# terminal 2
python3 module_7.py
```

## files structure

```bash
.
├── carla # carla python api
├── carla_controller_interface
│   ├── controller2d.py # controller interface
│   ├── cutils.py
│   ├── module_7.py
│   ├── options.cfg
│   └── racetrack_waypoints.txt
├── pid_controller # pid algorithm
│   ├── PID.c
│   ├── PID.h
│   ├── pid.so
│   ├── PID_Test.c
│   └── python_call_c_function.py
```
