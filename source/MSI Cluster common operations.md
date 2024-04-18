# MSI Cluster common operations

## Basics

```shell
pwd # show the current content
du -sh # show the used storage
space (keyboard) # next page
enter (keyboard) # fast next page 
ctrl+c # exit
cd # change the path
more # check files
less # check files
mkdir # create a folder
ls # list files
mv # move file or folder
cp # copy file or folder
rm # delete file or folder

module list # currently loaded module files
module avail # view all of the loadable software
module load fileName # load a file/software
softwareName # launch a software
```



## Disk usage and files counting

```shell
#t data usage 
du -sh
-s: summary
-h: humman read (add unit after number)

#t count number
find dir_exmaple -type f | wc -l # count all files in this dir recursively
-type f: file
```



## Task management

```shell
squeue --me # show only yr job info
squeue --al # show all job info
squeue -u yourUserName # show job info of this usr
sbatch .bshFile # submit a job to scheduler
scancel jobID # del a job
sacct -j jobID # view accounting info
scontrol show job jobID # view more detailed info (usually this can be replaced by the command above
```

### Apply for a interactive-job

```shell
srun -n 2 -t 24:00:00 --mem=32gb --cpus-per-task=4 --pty bash #specify an 24-hour wall time limit, 32G memory and 2 processor cores (=4 hardware threads)
srun -n 1 -t 24:00:00 --mem=32gb --x11 --pty bash # x11 means display GUI by default.
srun -n 1 -t 24:00:00 -p v100 --mem=32gb --gres=gpu:v100:1 --pty bash
```

### Submit a job

```shell
#!/bin/bash -l
#SBATCH --time=2:00:00
#SBATCH --ntasks=1
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=your@email.com
#SBATCH -p v100
#SBATCH --gres=gpu:v100:1 
#SBATCH --mem=32gb 
#SBATCH --output=probMap10.out
#SBATCH --error=probMap10.err

cd xxx/xxx/xxx
source activate xxx_environment
python xxx.py
```

