Mount (gnome-mount) options in nautilus
#######################################
:date: 2008-10-13 22:28
:author: infram
:category: Misc
:tags: gnome-mount, linux, mount options, nautilus
:slug: mount-gnome-mount-options-in-nautilus
:status: published

My portable music player is formatted with hfsplus. The linux hfsplus
mount this default readonly. To mount it writable you have to mount with
the force option. I tried it as root on the console with the following
mount options "rw,uid=1000,gid=1000,force". This worked. Now I want to
make it the default for this device. I opened nautilus on the device as
non root user and added these options to the mount preferences. On a new
connect I got the error message: Wrong mount options. I tried
"gnome-mount -vvv -b -d /dev/" on console. gnome-mount is the tool used
to mount the devices. I got the debug message that there are not allowed
mount options. I read the man pages and found out that uid is set by
gnome-mount itself and rw isn't allowed with uid. So I removed rw, uid,
gid options so that only force is added. Now the ipod with hfsplus is
mounted writable on connecting to the computer.

Update: By looking through the gnome-mount code I find out that you can
set the uid option like *uid=* and this is replaced with *uid=<id of the
current user>*.
